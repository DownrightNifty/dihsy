#!/usr/bin/env python3

# usage: ./generate_site.py [-C]
# -C: don't cleanup files
# 
# NOTE: this is super hacky. i almost think my goal for this project was to implement my
# own static site generator in the shittiest way possible or something. i definitely
# should've used a pre-existing solution, but it was fun to do everything manually :)
# 
# converts dihsy_converted.html -> index_generated.html
# 
# the document body structure of dihsy_converted.html is as follows:
# <h1>...</h1>
# [content for section 1]
# <h1>...</h1>
# [content for section 2]
# 
# NOTE: html insertions aren't escaped so don't insert untrusted data :)

from lxml.html import parse, HtmlElement, document_fromstring, tostring
from lxml.html import Element as _HtmlElement
from lxml.etree import _ElementTree
import os
import sys
import string

type fstr = str # str to be used with format()
def eprint(*args, **kwargs): return print(*args, **kwargs, file=sys.stderr)

# input filename
HTML_FN = "dihsy_converted.html"

# sections within groups must be consecutive
SECTION_GROUPS = {
    "eu-sideloading": "\"Sideloading\" in the EU"
}

PLACEHOLDERS: dict[str, fstr] = {
    "big-rss-btn": '<p><button title="RSS button" id="big-rss-btn" class="rss-btn button-unstyled"><i id="big-rss-icon" class="labeled-icon fa-solid fa-square-rss"></i></button><span class="icon-label"><a type="application/atom+xml" download href="/feed.xml" id="subscribe-link">{label}</a></span></p>'
}

SECTION_GROUP_START: fstr = """
<div class="section-div">
<h1 id="{id}" class="page-heading"><button title="Collapse/expand" class="button-unstyled collapse-btn"><i class="minus-icon fa-solid fa-fw fa-angle-down"></i></button><a href="#{id}"><span>{title}</span></a></h1>
""".strip() + "\n"

SECTION_GROUP_END: fstr = """
</div>
""".strip() + "\n"

SECTION_START = """
<div class="section-div">
""".strip() + "\n"

SECTION_END = """
</div>
""".strip() + "\n"

class Section:
    def __init__(self, heading: HtmlElement, elements: list[HtmlElement]):
        self.heading: HtmlElement = heading
        self.elements: list[HtmlElement] = elements

# extracts kwargs from an fstr
def extract_kwargs(s: fstr):
    items = {}

    class Extractor(dict):
        def __getitem__(self, key):
            items[key] = None
            return ''

    e = Extractor()
    s.format_map(e)

    return items

# basic implementation that preserves only alphanumerics and spaces
def title_to_id(title):
    title = title.lower()

    # preserve only alphanumerics and spaces
    new_title = ""
    for c in title:
        if c in string.ascii_lowercase + string.digits + " ":
            new_title += c
    title = new_title

    title = title.replace(" ", "-")
    return title

# return single element from `s` if applicable, or a `root` element with the elements from `s`
def str2el(s: str) -> HtmlElement:
    # returns an <html> element with a <body> containing the elements from `s`
    html_el: HtmlElement = document_fromstring(s)
    # root is <body>
    root: HtmlElement = html_el[0]
    root.tag = 'root'
    if len(root) == 1:
        return root[0]
    return root

def el2str(el: HtmlElement, pretty_print=False, strip_root=True) -> str:
    out: str = tostring(el, encoding='utf-8', pretty_print=pretty_print).decode('utf-8').strip()
    return out

# NOTE: pretty hacky impl
def inner_html(el: HtmlElement) -> str:
    tail = el.tail
    el.tail = None
    attrs = el.items()
    el.attrib.clear()

    ret = (
        el2str(el)
            .removeprefix(f"<{el.tag}>")
            .removesuffix(f"</{el.tag}>")
    )

    el.tail = tail
    for attr in attrs:
        el.set(attr[0], attr[1])
    return ret

def outer_html(el: HtmlElement) -> str:
    tail = el.tail
    el.tail = None
    ret = el2str(el)
    el.tail = tail
    return ret

def clear_inner_html(el: HtmlElement):
    el.text = ''
    for child in el:
        child.drop_tree()

# [parse args]
if not len(sys.argv) in (1, 2):
    eprint("error")
    sys.exit(1)

cleanup = True
try:
    cleanup = sys.argv[1]
except IndexError:
    pass

if cleanup != True and cleanup in ("-C", "--no-cleanup"):
    cleanup = False

doc: _ElementTree = parse(HTML_FN)

root: HtmlElement = doc.getroot()
body: HtmlElement = root[1]

# [operate on dihsy_converted.html]

# [rename generated id which conflicts with an h1's id]
fn_sect: HtmlElement = body.cssselect('section#footnotes')[0]
fn_sect.set('id', 'foonotes-section')

# [remove <hr> above footnotes]
fn_sect[0].drop_tree()

# [replace all footnotes with a better format]
footnotes: list[HtmlElement] = body.cssselect('.footnote-ref')
for footnote in footnotes:
    # footnote looks like: <a><sup></sup></a>
    fn_text = footnote[0].text
    # delete the sup
    footnote[0].drop_tree()
    # replace with raw text inside the link
    footnote.text = '[' + fn_text + ']'

# [style blockquotes]
blockquotes: list[HtmlElement] = body.cssselect('blockquote')
for bq in blockquotes:
    # italicize all paragraphs inside the blockquote
    children: list[HtmlElement] = bq.cssselect('p')
    for p in children:
        p_inner_html = inner_html(p)
        p.drop_tree()
        new_p = str2el(f'<p><i>{p_inner_html}</i></p>')
        bq.append(new_p)

    # create a <div> around the blockquote
    bqp: HtmlElement = bq.getparent()
    idx = bqp.index(bq)
    bq.drop_tree()

    div: HtmlElement = _HtmlElement('div')
    div.classes.add('bq-div')
    div.append(bq)
    bqp.insert(idx, div)

# [insert external link icons]
links: list[HtmlElement] = body.cssselect("a")
for link in links:
    href = link.get("href")
    if href:
        if href.startswith("#"):
            # link.classes.add("internal-link")
            pass
        else:
            # link.classes.add("external-link")

            # replace this link with a <span> containing the link AND an icon
            new_link = str2el('<span>' + outer_html(link) + '<i class="external-link-icon fa-solid fa-arrow-right fa-rotate-by" style="--fa-rotate-angle: -45deg;"></i>' + '</span>')
            new_link.tail = link.tail

            link.getparent().replace(link, new_link)

# [replace placeholders with content]
ph_els: list[HtmlElement] = body.cssselect(".PLACEHOLDER")
for ph_el in ph_els:
    ph_id = ph_el.get('data-id')
    el_src = PLACEHOLDERS[ph_id]
    ph_kwargs: dict = extract_kwargs(el_src)

    for kwarg in ph_kwargs:
        ph_kwargs[kwarg] = ph_el.get(f"data-{kwarg}")
        if not ph_kwargs[kwarg]:
            ph_kwargs[kwarg] = ''
    
    el_src = el_src.format(**ph_kwargs)
    el = str2el(el_src)
    ph_el.getparent().replace(ph_el, el)

# [find sections]

sections: list[Section] = []
section: Section = Section(heading=body[0], elements=[])

child: HtmlElement
for i, child in enumerate(body[1:]):
    if child.tag == "h1":
        # start of new section
        sections.append(section)
        section = Section(heading=child, elements=[])
        continue
    section.elements.append(child)
    if i == len(body[1:]) - 1:
        # chop off what's left
        sections.append(section)
        section = Section(heading=child, elements=[])
        continue

# [reconstruct document]

f = open("out.html", "w", encoding='utf-8')

current_group_id = None
i = 0
for s in sections:
    # all headings need to be made into links as well
    sh: HtmlElement = s.heading
    shp: HtmlElement = sh.getparent()

    sh_group_id = sh.get("data-group", default=None)

    if current_group_id != sh_group_id and i != 0:
        # no longer inside group
        current_group_id = None
        f.write(SECTION_GROUP_END)

    sh_id = sh.get("id")
    sh.set('class', 'page-heading')
    sh_html = inner_html(sh)
    sh_html = f'<button title="Collapse/expand" class="button-unstyled collapse-btn"><i class="minus-icon fa-solid fa-fw fa-angle-down"></i></button><a href="#{sh_id}"><span>' + sh_html + '</span></a>'

    new_heading_base = str2el(sh_html)
    clear_inner_html(sh)
    for el in new_heading_base:
        sh.append(el)

    if not current_group_id and sh_group_id in SECTION_GROUPS:
        # start a new group
        title = SECTION_GROUPS[sh_group_id]
        f.write(SECTION_GROUP_START.format(id=title_to_id(title), title=title))
        current_group_id = sh_group_id

    f.write(SECTION_START)
    f.write(el2str(sh))
    for child in s.elements:
        if child.tag == "table":
            f.write("<div class=\"table-div\">\n")
        f.write(el2str(child))
        if child.tag == "table":
            f.write("</div>\n")
    f.write(SECTION_END)
    i += 1

f.close()

# [concat templates to generate final document]

# read the file we just wrote (lol)
f = open("out.html", "r")
out_html = f.read()
f.close()
os.unlink("out.html")

f = open("index_p1.template.html", "r")
p1_html = f.read()
f.close()

f = open("index_p2.template.html", "r")
p2_html = f.read()
f.close()

f = open("index_generated.html", "w")

f.write(p1_html)
f.write(out_html)
f.write(p2_html)

f.close()

if cleanup:
    os.unlink("dihsy_converted.html")

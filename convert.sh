#!/bin/bash
set -e
# should be executed from the project directory

pandoc ./dihsy.md -o ./pandoc_out.html --wrap none --from markdown-smart
cat ./pandoc_p1.template.html ./pandoc_out.html ./pandoc_p2.template.html > ./dihsy_converted.html
rm ./pandoc_out.html

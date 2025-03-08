#!/bin/bash

# usage: build.sh [-C] [-W] [-v]
# should be executed from the project directory
# -C: don't cleanup files
# -W: don't watch for changes and rebuild automatically
# -v: verbose

set -e

WATCHED_FILES=(./dihsy.md ./index_p1.template.html ./index_p2.template.html)
OUT_DIR="$PWD/out"

osx=false
if [[ $(uname) == "Darwin" ]]; then osx=true; fi

# cross platform function to get mtime of files
mtime() {
    if [[ $osx == "true" ]]; then
        stat -f '%m' "$@"
    else
        stat -c '%Y' "$@"
    fi
}

build() {
    if [[ $verbose == true ]]; then echo "building"; fi

    # converts markdown -> HTML with pandoc (generating dihsy_converted.html)
    ./convert.sh

    # generates index_generated.html (and deletes dihsy_converted.html)
    if [[ $cleanup == false ]]; then
        ./generate_site.py "-C"
    else
        ./generate_site.py
    fi

    # create directory for site files
    rm -rf "$OUT_DIR"
    mkdir "$OUT_DIR"
    cp ./index_generated.html "$OUT_DIR"/index.html
    cp -r ./font-awesome "$OUT_DIR"
    cp -r ./assets "$OUT_DIR"
    cp -r ./news "$OUT_DIR"
    cp ./feed.xml "$OUT_DIR"
    cp ./script.js "$OUT_DIR"
    cp ./style.css "$OUT_DIR"
    cp ./CNAME "$OUT_DIR"
    cp ./.nojekyll "$OUT_DIR"
    
    cp ./.gitignore "$OUT_DIR"
}

# parse args
cleanup=true
watch=true
verbose=false
for arg in "$@"; do
    if [[ $arg == "-C" || $arg == "--no-cleanup" ]]; then
        cleanup=false
    elif [[ $arg == "-W" || $arg == "--no-watch" ]]; then
        watch=false
    elif [[ $arg == "-v" || $arg == "--verbose" ]]; then
        verbose=true
    fi
done

build

if [[ $watch == true ]]; then
    last_mod=$(mtime "${WATCHED_FILES[@]}")
    while true; do
        sleep 1
        mod=$(mtime "${WATCHED_FILES[@]}")
        if [[ "$last_mod" != "$mod" ]]; then
            last_mod=$mod
            build
        fi
    done
fi

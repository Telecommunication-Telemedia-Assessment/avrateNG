#!/bin/bash

if [[ "$(pandoc --version | grep " 2\."| wc -l)" = "1" ]]; then
    # version 2 of pandoc is a bit bitchy
    pandoc -f markdown-latex_macros -t beamer slides.md -o slides.pdf
else
    pandoc -t beamer slides.md -o slides.pdf
fi


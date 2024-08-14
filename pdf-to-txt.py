#!/usr/bin/env python

import pypdf
import sys
from os import path

if len(sys.argv) < 3:
    print("Error: requires 3 args")
    print("Correct usage: pdf-to-txt.py <input> <output>")
    exit()

input = sys.argv[1]
output = sys.argv[2]

if not path.exists(input):
    print("Error: No input")
    exit()
#if not path.exists(output):
    #print("Error: No output")
    #exit()

with open(input, 'rb') as pdf_file:
    pdf_reader = pypdf.PdfReader(input)

    text = ''

    length = 0

    for page_n in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_n]
        c_text = page.extract_text()
        text += c_text
        if len(c_text) > length:
            length = len(c_text)

    print(f"Max column length: {length}")

with open(output, 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)

with open(output, 'r', encoding='utf-8') as txt_file:
    lines = sum(1 for _ in txt_file)
    print(f"Line count: {lines}")

print("All done! <3")

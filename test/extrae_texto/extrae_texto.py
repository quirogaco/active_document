#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import pprint, datetime

from parent_import import parentdir
#word_plantilla = parentdir.parentdir.librerias.plantillas.word.word_plantilla

import pdfminer
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


archivo = "D:\\gestor_2021\\test\\ocr_pdfa\\sale_pdfa.pdf"
archivo = "D:\\FB0000002493.pdf"
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1

"""
print("inicia 1")
ini1 = datetime.datetime.now()
gran_texto1 = ""
pages_count = 0
with open(archivo, 'rb') as f:
    parser = PDFParser(f)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    pages = resolve1(doc.catalog['Pages'])
    pages_count = pages.get('Count', 0)

print("pages_count:", pages_count)

paginas = []
for page in range(pages_count):
    texto = pdfminer.high_level.extract_text(archivo, page_numbers=[page], maxpages=1)
    paginas.append(texto)
    gran_texto1 += texto
    #print(pdfminer.high_level.extract_text(archivo, page_numbers=[page], maxpages=1))
    #print("page:", page)
termina1 = datetime.datetime.now()- ini1
print(termina1)
"""


#"""
print("")
print("inicia 2")
ini2 = datetime.datetime.now()
gran_texto2 = ""
texto_lista = []
i     = 0
for page_layout in extract_pages(archivo):
    i += 1    
    pagina = ""
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            texto = element.get_text()            
            pagina += texto
            gran_texto2 += texto
    texto_lista.append(pagina)
    #print("PAGINA:", i)
termina2 = datetime.datetime.now()- ini2
print(termina2)
#"""

print("")
print("")
#print("tamaño:", len(gran_texto1), len(gran_texto2))
#print("tiempo:", termina1, termina2)
print(gran_texto2)
#"""
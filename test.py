import numpy as np

from pylatex import *
from pylatex.utils import *
import os

def makeCircledText(text):
    with doc.create(TikZ()):
            doc.append(TikZNode(options=TikZOptions('shape=circle', 'draw','inner sep=2pt', 'font=\\bfseries'), text=text))
            

if __name__ == "__main__":
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
    doc = Document(geometry_options=geometry_options)

    with doc.create(Section("First MC")):
        doc.append("Q1. Patient Symptoms: ")
        doc.append(HorizontalSpace("10mm"))

        makeCircledText("A")
        doc.append(HorizontalSpace("2mm"))
        makeCircledText("B")
        doc.append(HorizontalSpace("2mm"))
        makeCircledText("C")
        doc.append(HorizontalSpace("2mm"))
        makeCircledText("D")

    doc.generate_pdf('full', clean_tex=False)



import streamlit as st
from PIL import Image  # Import image from pillow to open images

from pdfstructure.hierarchy.parser import HierarchyParser
from pdfstructure.source import FileSource
from pdfstructure.printer import PrettyStringPrinter
from pdfstructure.model.document import StructuredPdfDocument
from pdfstructure.hierarchy.traversal import traverse_level_order

import tkinter as tk
from tkinter import filedialog

import PyPDF2
import json


def user_input() -> None:
    """
    This function runs the Streamlit library and opens up the browser. It let user choose a pdf and
    identify and categorize by title, subtitle, paragraphs and more.
    """
    # Set Title of Web Page
    st.set_page_config(page_title="Greyled - Book Import Tool")

    # Title
    st.title("Greyled - Book Import Tool")

    st.text("Early prototype by Yehyun Lee")
    st.text("Web page written and hosted by Yehyun Lee")
    # This un-indent is needed. Due to st.text reading function tab as indent of texts.
    st.text("""Copyright and Usage Information
===============================
This page is provided for the Greyled. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for this project,
please consult Greyled.

This page is Copyright (c) 2023 Greyled.""")

    # Display Image
    img = Image.open("greyled.png")
    st.image(img, width=400)

    # File picker button
    st.title('Import Book')
    st.write('Choose a PDF file')


    # uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    # print(uploaded_file.name)

    clicked = st.button('Import Book')
    if clicked:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        file_path = st.text_input('Selected file:', filedialog.askopenfilename(master=root))

        parser = HierarchyParser()
        source = FileSource(file_path)
        document = parser.parse_pdf(source)

        stringExporter = PrettyStringPrinter()
        prettyString = stringExporter.print(document)

        st.text(prettyString)

        # sections = [e for e in traverse_level_order(document, max_depth=2)]
        # st.text(sections)


if __name__ == '__main__':
    user_input()

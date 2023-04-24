import streamlit as st
from PIL import Image  # Import image from pillow to open images

from pdfstructure.hierarchy.parser import HierarchyParser
from pdfstructure.source import FileSource
from pdfstructure.printer import PrettyStringPrinter
from pdfstructure.model.document import StructuredPdfDocument
from pdfstructure.hierarchy.traversal import traverse_level_order

import tkinter as tk
from tkinter import filedialog

import fitz

import PyPDF2
import json

import part2_classification

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

    # clicked = st.button('Import Book')
    # if clicked:
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    file_path = st.text_input('Selected file:', filedialog.askopenfilename(master=root))

    # parser = HierarchyParser()
    # source = FileSource(file_path)
    # document = parser.parse_pdf(source)
    #
    # stringExporter = PrettyStringPrinter()
    # prettyString = stringExporter.print(document)
    #
    # st.text(prettyString)
    #
    # st.text(part2_classification.classification(prettyString))


    # Create a document object
    doc = fitz.open('C:/Users/glad7/Downloads/Yehyun Lee Resume.pdf')  # or fitz.Document(filename)

    # Extract the number of pages (int)
    print('page', doc.page_count)

    # the metadata (dict) e.g., the author,...
    print('metadata', doc.metadata)

    ###############################################################
    # Get the page by their index
    page = doc.load_page(0)
    # page = doc[0]

    # read a Page
    text = page.get_text()
    print(text)

    # Render and save the page as an image
    pix = page.get_pixmap()
    pix.save(f"page-{page.number}.png")

    # get all links on a page
    links = page.get_links()
    print(links)

    # Render and save all the pages as images
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        pix.save("page-%i.png" % page.number)

    # get the links on all pages
    for i in range(doc.page_count):
        page = doc.load_page(i)
        link = page.get_links()
        print(link)

    edit = st.button('Edit')


if __name__ == '__main__':
    user_input()

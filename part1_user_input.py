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
    global page
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

    if 'result' not in st.session_state:
        st.session_state.result = None

    file_path = ''
    clicked = st.button('Import Book')
    if clicked:
        try:
            # import easygui
            # file_path = easygui.fileopenbox(title='Add File', default="*.pdf")
            # st.write(file_path)

            root = tk.Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            file_path = st.text_input('Selected file:', filedialog.askopenfilename(master=root))
        finally:
            st.session_state.result = file_path

    if st.session_state.result:
        st.subheader('Classified')
        parser = HierarchyParser()
        source = FileSource(st.session_state.result)
        document = parser.parse_pdf(source)
        stringExporter = PrettyStringPrinter()
        prettyString = stringExporter.print(document)
        data = part2_classification.classification(prettyString)

        object_types = st.multiselect('Select Type of Objects', ['Big Elements', 'Paragraphs', 'Bullet Points'])
        if 'Big Elements' in object_types:
            st.text('Big Elements')
            st.write(data['big_elements'])
        if 'Paragraphs' in object_types:
            st.text('Paragraphs')
            st.write(data['paragraphs'])
        if 'Bullet Points' in object_types:
            st.text('Bullet Points')
            st.write(data['bullet_points'])

        doc = fitz.open(st.session_state.result)  # or fitz.Document(filename)
        st.subheader('Original Check')
        st.write('Total pages: ', doc.page_count)
        # the metadata (dict) e.g., the author,...
        st.write('Metadata: ', doc.metadata)
        selected_page = st.selectbox('Select Page Number', list(range(1, doc.page_count + 1))) - 1
        # Get the page by their index
        page = doc.load_page(selected_page)  # page = doc[page]

        st.subheader("Texts")
        # read a page
        text = page.get_text()
        st.text(text)

        st.subheader("Links")
        # get all links on a page
        link = page.get_links()
        st.text(link)

        st.subheader("Links on All Pages")
        # get the links on all pages
        save_links = []
        for i in range(doc.page_count):
            page = doc.load_page(i)
            links = page.get_links()
            save_links.extend(links)
        st.text(save_links)


if __name__ == '__main__':
    user_input()

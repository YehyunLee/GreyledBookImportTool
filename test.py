# # import pdfplumber
# #
# # with pdfplumber.open("C:/Users/glad7/Downloads/Yehyun Lee Resume.pdf") as pdf:
# #    first_page = pdf.pages[0]
# #    print(first_page.objects)
# #
# # p0 = pdf.pages[0]
# # p0.extract_words()
#
# # import pymupdf
# # The import name for this library is fitz
# import fitz
#
# # Create a document object
# doc = fitz.open('C:/Users/glad7/Downloads/Yehyun Lee Resume.pdf')  # or fitz.Document(filename)
#
# # Extract the number of pages (int)
# print('page', doc.page_count)
#
# # the metadata (dict) e.g., the author,...
# print('metadata', doc.metadata)
#
# ###############################################################
# # Get the page by their index
# page = doc.load_page(0)
# # page = doc[0]
#
# # read a Page
# text = page.get_text()
# print(text)
#
# # Render and save the page as an image
# pix = page.get_pixmap()
# pix.save(f"page-{page.number}.png")
#
# # get all links on a page
# links = page.get_links()
# print(links)
#
# # Render and save all the pages as images
# for i in range(doc.page_count):
#   page = doc.load_page(i)
#   pix = page.get_pixmap()
#   pix.save("page-%i.png" % page.number)
#
# # get the links on all pages
# for i in range(doc.page_count):
#   page = doc.load_page(i)
#   link = page.get_links()
#   print(link)

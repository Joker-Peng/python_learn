import pymupdf
pdf_document = pymupdf.open('2.pdf')
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text = page.get_text()
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        with open(f"test{page_num + 1}_{img_index + 1}.{image_ext}", "wb") as f:
            f.write(image_bytes)
    print(text)
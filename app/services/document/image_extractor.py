import fitz
import os


def extract_images(pdf_path, output_folder="images"):

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(pdf_path)

    image_paths = []

    for page_number in range(len(pdf)):

        page = pdf[page_number]

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]

            pix = fitz.Pixmap(pdf, xref)

            filename = f"{page_number+1}_{img_index+1}.png"

            filepath = os.path.join(
                output_folder,
                filename
            )

            pix.save(filepath)

            image_paths.append(filepath)

            pix = None

    pdf.close()

    return image_paths
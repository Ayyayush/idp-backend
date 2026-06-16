import easyocr
import os

from pdf2image import convert_from_path

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

POPPLER_PATH = r"C:\Users\Aayu0\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def extract_text_from_image(file_path):

    extension = file_path.split(".")[-1].lower()

    if extension == "pdf":

        pages = convert_from_path(
            file_path,
            poppler_path=POPPLER_PATH
        )

        text = ""

        for index, page in enumerate(pages):

            temp_image = f"temp_page_{index}.jpg"

            page.save(
                temp_image,
                "JPEG"
            )

            result = reader.readtext(
                temp_image,
                detail=0
            )

            text += "\n".join(result) + "\n"

            os.remove(temp_image)

        return text

    else:

        result = reader.readtext(
            file_path,
            detail=0
        )

        return "\n".join(result)
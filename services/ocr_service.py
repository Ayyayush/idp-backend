import os

import easyocr

from dotenv import load_dotenv
from pdf2image import convert_from_path

load_dotenv()

reader = easyocr.Reader(
    ["en"],
    gpu=False
)

POPPLER_PATH = os.getenv(
    "POPPLER_PATH"
)


def extract_text_from_image(file_path):

    extension = file_path.split(".")[-1].lower()

    if extension == "pdf":

        if POPPLER_PATH:

            pages = convert_from_path(
                file_path,
                poppler_path=POPPLER_PATH
            )

        else:

            pages = convert_from_path(
                file_path
            )

        text = ""

        for index, page in enumerate(pages):

            temp_image = (
                f"temp_page_{index}.jpg"
            )

            page.save(
                temp_image,
                "JPEG"
            )

            result = reader.readtext(
                temp_image,
                detail=0
            )

            text += (
                "\n".join(result)
                + "\n"
            )

            os.remove(
                temp_image
            )

        return text

    result = reader.readtext(
        file_path,
        detail=0
    )

    return "\n".join(result)
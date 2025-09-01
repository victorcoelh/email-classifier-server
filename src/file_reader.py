from fastapi import UploadFile
from pypdf import PdfReader


async def get_text_from_file(file: UploadFile) -> str:
    if not file.filename:
        raise ValueError("Arquivo inválido")
    
    match file.filename.split(".")[-1]:
        case "pdf":
            return get_text_from_pdf(file)
        case "txt":
            return await get_text_from_txt(file)
        case _:
            raise ValueError("Arquivo em formato inválido: envie um .pdf ou .txt")

def get_text_from_pdf(file: UploadFile) -> str:
    reader = PdfReader(file.file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()
    return text

async def get_text_from_txt(file: UploadFile) -> str:
    return (await file.read()).decode("utf-8")

from pdf2image import convert_from_path

class ConverterPdfToJpg:
    def __init__(self):
        pass
    def convert(self, pdfUrl: str) -> list[str]:
        pages = convert_from_path(pdfUrl)
        jpgUrls = []
        for i in range(len(pages)):
            jpgUrls.append(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.{i}.jpg');
            pages[i].save(jpgUrls[i], 'JPEG')
        return jpgUrls


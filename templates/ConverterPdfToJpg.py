from pdf2image import convert_from_path
import os
import os.path


class ConverterPdfToJpg:
    def __init__(self):
        pass
    
    def convert(self, pdfUrl: str) -> list[str]:
        jpgUrls = []
        if (os.path.isfile(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.0.jpg')):
            print("local")
            jpgUrls.append(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.0.jpg');
            i = 1
            while os.path.isfile(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.{i}.jpg'):
                jpgUrls.append(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.{i}.jpg');
                i=i+1;
        else:
            print("site")
            pages = convert_from_path(pdfUrl)
            for i in range(len(pages)):
                jpgUrls.append(f'img/{pdfUrl[pdfUrl.rfind("/")+1:]}.page.{i}.jpg');
                pages[i].save(jpgUrls[i], 'JPEG')
        return jpgUrls


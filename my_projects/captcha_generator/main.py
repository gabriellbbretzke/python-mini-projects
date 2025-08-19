from PIL import Image
from captcha.image import ImageCaptcha
from io import BytesIO

def main() -> None:
    text: str = 'Hello'

    captcha: ImageCaptcha = ImageCaptcha(width=400,
                                         height=220,
                                        #  fonts=['Arial',
                                        #        'Times New Roman',
                                        #        'Calibri'],
                                         font_sizes=(40, 70, 100)) #NOQA: Type hint was done wrong
    # captcha.write(text, 'captcha.png')

    data: BytesIO = captcha.generate(text)
    image: Image = Image.open(data)
    image.show('Sample Captcha')

if __name__ == '__main__':
    main()
from captcha.image import ImageCaptcha
import numpy as np
import random
import string


class generate_captcha:
    def __init__(self, width=30,
                 heigth=160,
                 characters=string.digits + string.ascii_uppercase + string.ascii_lowercase,
                 num=4):
        self.width = width
        self.heigth = heigth;
        self.num = num
        self.characters = characters
        self.classes=len(characters)
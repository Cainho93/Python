from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 280, height = 90)
nome = 'manuella'
data = image.generate(nome)

image.write(nome, 'CAPTCHA.png')



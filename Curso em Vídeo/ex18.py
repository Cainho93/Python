import math
an=float(input('Digite um ângulo: '))
sin=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin,cos,tan))
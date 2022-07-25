from urllib.parse import urlparse, parse_qs 

link = 'https://www.google.com/search?q=hashtag+treinamentos&oq=hashtag+&aqs=chrome.1.69i57j0i433i512j0i512j0i131i433i512j0i433i512j0i131i433i512j46i175i199i512j0i433i512l2j0i512.9594j0j7&sourceid=chrome&ie=UTF-8'

link_tratado = urlparse(link)
parametros = parse_qs(link_tratado.query)
#print(parametros)
print(parametros['q'])
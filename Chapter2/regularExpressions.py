from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html = urlopen('https://www.pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    img_regex_expr = "\.\./img/gifts/img[0-9]*\.jpg"
    for img in bs.find_all('img', src=re.compile(img_regex_expr)):
        print(img['src'])

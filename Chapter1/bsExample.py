from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    # bs1 = BeautifulSoup(html, 'html.parser')
    bs1 = BeautifulSoup(html.read(), 'html.parser')
    print(bs1.prettify())
    print("Printing H1, in different ways")
    print(bs1.h1)
    print(bs1.html.h1)
    print(bs1.html.body.h1)

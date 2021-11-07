from urllib.request import urlopen

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = urlopen('https://www.pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    for tag in bs.find_all(lambda tag: len(tag.attrs) == 2):
        print(tag)

    print(list(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting')))

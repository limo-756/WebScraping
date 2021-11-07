import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
    bs = BeautifulSoup(html, 'html.parser')

    # A simple crawler that output all the links
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link['href'])

    # Shows all the wikipedia links that are on Kevin Bacon and not wikipedia internal pages
    wikipedia_external_url_regex = '^/wiki/((?!:).)*$'
    for link in bs.find('div', id='bodyContent').find_all('a', href=re.compile(wikipedia_external_url_regex)):
        if 'href' in link.attrs:
            print(link['href'])

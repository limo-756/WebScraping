import datetime
import random
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_all_links_on_page(page):
    html = urlopen('http://en.wikipedia.org{}'.format(page))
    bs = BeautifulSoup(html, 'html.parser')
    wikipedia_external_url_regex = '^/wiki/((?!:).)*$'
    return bs.find('div', id='bodyContent').find_all('a', href=re.compile(wikipedia_external_url_regex))


if __name__ == '__main__':
    link = '/wiki/Kevin_Bacon'

    random.seed(datetime.datetime.now())
    for i in range(100):
        if link is None:
            print('Link is none, exiting')
            break
        print("Searching link ", link)
        links = get_all_links_on_page(link)
        if len(links) == 0:
            print('Encountered empty page. Exiting')
            break
        link = links[random.randint(0, len(links) - 1)]['href']

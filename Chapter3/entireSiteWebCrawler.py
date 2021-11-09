from urllib.request import urlopen

from bs4 import BeautifulSoup

pages = set()


def is_valid_url(page):
    try:
        urlopen(page)
        return True
    except Exception:
        pages.add(page)
        return False


def get_pages(page):
    print("Visiting ", page)

    html = urlopen(page)
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs and is_valid_url(link['href']) and link['href'] not in pages:
            pages.add(link['href'])
            get_pages(link['href'])


if __name__ == '__main__':
    get_pages('https://www.flock.com/')

from urllib.request import urlopen
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


def main():
    html = urlopen('https://www.python.org/')
    bs = BeautifulSoup(html, 'html.parser')
    image_location = bs.find('img', {'class': 'python-logo'})['src']
    urlretrieve('https://www.python.org/' + image_location, '/Users/anurag.sh/workspace/SQLDump/temp/logo.jpg')


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    req = requests.get('https://timesofindia.indiatimes.com/')
    bs = BeautifulSoup(req.text, 'html.parser')

    # find tags under other tags
    print(bs.select("div > a")[0])

    # find siblings of an element
    print(bs.select(".col_l_6 ~"))


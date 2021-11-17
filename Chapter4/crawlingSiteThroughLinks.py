import re

import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, title, body, url):
        self.url = url
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return 'url={},\ntitle={},\nbpdy={}'.format(self.url, self.title, self.body)


class Website:
    def __init__(self, name, url, target_pattern, absolute_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.target_pattern = target_pattern
        self.absolute_url = absolute_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    def __init__(self, site) -> None:
        self.site = site
        self.visited = set()

    def get_page(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safe_get(self, page_obj, selector):
        selected_elements = page_obj.select(selector)
        if selected_elements is not None and len(selected_elements) > 0:
            return '\n'.join([elem.get_text() for elem in selected_elements])
        else:
            return ''

    def parse(self, url):
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, self.site.title_tag)
            body = self.safe_get(bs, self.site.body_tag)

            if title != '' or body != '':
                print(Content(title, body, url))

    def crawl(self):
        bs = self.get_page(self.site.url)
        target_pages = bs.find_all('a', href=re.compile(self.site.target_pattern))

        for target_page in target_pages:
            target_page = target_page['href']
            print(target_page)
            if target_page is not None and target_page not in self.visited:
                self.visited.add(target_page)
                if not self.site.absolute_url:
                    target_page = '{}{}'.format(self.site.url, target_page)

                self.parse(target_page)

if __name__ == '__main__':
    times_of_india = Website('Times of India', 'https://timesofindia.indiatimes.com/', '(/world)', False, 'h1', '._3YYSt.clearfix')
    Crawler(times_of_india).crawl()
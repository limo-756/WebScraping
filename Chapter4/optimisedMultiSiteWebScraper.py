import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return 'url={},\ntitle={},\nbpdy={}'.format(self.url, self.title, self.body)


class Website:
    def __init__(self, name, url, title_tag, body_tag) -> None:
        self.name = name
        self.url = url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:

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

    def parse(self, site, url):
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)

            if title != '' and body != '':
                print(Content(url, title, body))


if __name__ == '__main__':
    crawler = Crawler()
    siteData = [
        ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
        ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
        ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
        ['New York Times', 'http://nytimes.com', 'h1', 'p.story-content']
    ]
    websites = []
    for row in siteData:
        websites.append(Website(row[0], row[1], row[2], row[3]))
    crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
    crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
    crawler.parse(websites[2],
                  'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
    crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')

import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, topic, title, body, url):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return 'topic={},\nurl={},\ntitle={},\nbpdy={}'.format(self.topic, self.url, self.title, self.body)


class Website:
    def __init__(self, name, url, search_url, resulting_listing, result_url, absolute_url, title_tag, body_tag) -> None:
        self.name = name
        self.url = url
        self.search_url = search_url
        self.resulting_listing = resulting_listing
        self.result_url = result_url
        self.absolute_url = absolute_url
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
        child_obj = page_obj.select(selector)
        if child_obj is not None and len(child_obj) > 0:
            return child_obj[0].get_text()
        else:
            return ''

    def search(self, topic, site):
        bs = self.get_page(site.search_url + topic)
        search_results = bs.select(site.resulting_listing)

        for index, result in zip(range(1), search_results):
            print("Processing search result {} for topic {} on site {}".format(index, topic, site.name))
            url = result.select(site.result_url)[0].attrs["href"]

            if site.absolute_url:
                bs = self.get_page(url)
            else:
                bs = self.get_page(site.url + url)

            if bs is None:
                print("Something wrong with page or url. Skipping!")
                return

            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)

            if title != '' or body != '':
                print(Content(topic, title, body, url))


def main():
    crawler = Crawler()
    site_data = [
        ['Times of India', 'https://timesofindia.indiatimes.com/',
         'https://timesofindia.indiatimes.com/topic/', 'div.content',
         'a', False, 'h1', '._3YYSt.clearfix'],
        # ['Reuters', 'https://www.reuters.com/',
        #  'https://www.reuters.com/site-search/?query=',
        #  '.SearchResults__item___3jzYEE', 'a.MediaStoryCard__legal___2PIixq',
        #  False, 'h1', 'div.ArticleBody__container___D-h4BJ p'],
        ['Brookings', 'http://www.brookings.edu',
         'https://www.brookings.edu/search/?s=',
         'div.list-content article', 'h4.title a', True, 'h1',
         'div.post-body']
    ]

    sites = []
    for row in site_data:
        sites.append(Website(row[0], row[1], row[2],
                             row[3], row[4], row[5], row[6], row[7]))
    topics = ['modi']
    for topic in topics:
        print("GETTING INFO ABOUT: " + topic)
        for targetSite in sites:
            crawler.search(topic, targetSite)


if __name__ == '__main__':
    main()

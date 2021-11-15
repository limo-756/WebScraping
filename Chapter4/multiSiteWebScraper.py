import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return 'url={},\ntitle={},\nbpdy={}'.format(self.url, self.title, self.body)


def get_page(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def scrape_ny_times(url):
    bs = get_page(url)
    title = bs.find("h1").text
    lines = bs.find_all("p", {"class": "story-content"})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)


def scraping_brookings(url):
    bs = get_page(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class", "post-body"}).text
    return Content(url, title, body)


if __name__ == '__main__':
    content = scraping_brookings('https://www.brookings.edu/blog/future-development'
                                 '/2018/01/26/delivering-inclusive-urban-access-3-unc'
                                 'omfortable-truths/')
    print(content)

    url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
    content = scrape_ny_times(url)
    print(content)

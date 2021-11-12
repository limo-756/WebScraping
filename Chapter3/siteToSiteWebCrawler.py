import datetime
import random
import re
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup


# Retrieves a list of all internal links found on a page
def get_internal_links(bs, include_url):
    include_url = '{}://{}'.format(urlparse(include_url).scheme, urlparse(include_url).netloc)
    internal_links = []

    # Finds all links that begin with a "/" or begin with include_url and end in anything
    # Eg: /people/Adam, http://abc.com/aboutus
    for link in bs.find_all('a', href=re.compile('^(/|.*' + include_url + ')')):
        if link['href'] is not None and link['href'] not in internal_links:
            if link['href'].startswith('/'):
                internal_links.append(include_url + link['href'])
            else:
                internal_links.append(link['href'])

    return internal_links


# Retrieves a list of all external links found on a page
def get_external_links(bs, exclude_url):
    external_links = []

    # Find all links that start with http and do not contain current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + exclude_url + ').)*$')):

        if link['href'] is not None and link['href'] not in external_links:
            external_links.append(link['href'])

    return external_links


def is_valid_page(page):
    try:
        html = urlopen(page)
        BeautifulSoup(html, 'html.parser')
        return True
    except (HTTPError, URLError):
        return False


def get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bs = BeautifulSoup(html, 'html.parser')
    external_links = get_external_links(bs, urlparse(starting_page).netloc)

    if len(external_links) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(starting_page).scheme, urlparse(starting_page).netloc)
        internal_links = get_internal_links(bs, domain)
        for page in internal_links:
            if not is_valid_page(page):
                continue
            return get_random_external_link(page)
    else:
        for page in external_links:
            if not is_valid_page(page):
                continue
            return page


def follow_external_links_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print('Random external link is: {}'.format(external_link))
    follow_external_links_only(external_link)


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    follow_external_links_only('https://stackoverflow.com')

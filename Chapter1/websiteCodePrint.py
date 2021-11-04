from urllib.request import urlopen

if __name__ == '__main__':
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    print(html.read())

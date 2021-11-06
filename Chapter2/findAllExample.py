from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    names = bs.find_all("span", {'class': 'green'}, True)
    for name in names:
        print(name.get_text())

    all_headers = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    print("### ALL HEADERS ###")
    print(all_headers)

    print("### What is the count of phrase 'the prince' ?")
    the_prince_cnt = len(bs.find_all(text='the prince'))
    print(the_prince_cnt)

    print("### All tags that hv attr id=title and class=text")
    title_tag = bs.find_all(id='title', class_='text')
    print(title_tag)

    print('#### ALL Span tags with red and green class #####')
    all_red_green_tag = bs.find_all('span', {'class': {'green', 'red'}})
    print(all_red_green_tag)


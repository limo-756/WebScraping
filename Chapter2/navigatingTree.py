from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = urlopen('https://www.pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    print('### All Children of table giftList ###')
    for child in bs.find('table', id='giftList').children:
        print('--------')
        print(child)
        print('--------')

    print('\n\n\n')
    print('### All Desendents of table giftList ###')
    for descendant in bs.find('table', id='giftList').descendants:
        print('--------')
        print(descendant)
        print('--------')

    print('Printing all the siblings of header rows')
    # print(bs.find('table', {'id': 'giftList'}).tr)
    # Prints the title row of the table
    for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

    print("Calling sibling in the middle of the table")
    for sibling in bs.find('tr', {'id': 'gift3'}).next_siblings:
        print(sibling)

    print('Find the price of item, given you hv image')
    print(bs.find('img', src="../img/gifts/img3.jpg").parent.previous_sibling.get_text())

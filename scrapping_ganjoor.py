from bs4 import BeautifulSoup
import requests
import time

t_start = time.time()
print ('Program started ...')
def beyt_scrapper(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    beyts_soup = soup.find_all('div', class_=('m1', 'm2'))
    if not beyts_soup:
        print("this link is not a poem, might be a daftar")
        daftar_scrapper(link)
    global book_list
    for mesra in beyts_soup:
        book_list.append(mesra.text.replace("\u200c"," "))



def daftar_scrapper(daftar_page):
    r = requests.get(daftar_page)
    soup = BeautifulSoup(r.content, "html.parser")
    daftar_soup = soup.find_all('a')
    for link in daftar_soup:
        if link.has_attr('href'):
            if link['href'].startswith(daftar_page) and link['href'] != daftar_page:
                hekayat_link = link['href']
                print("parsing this page: "+hekayat_link)
                beyt_scrapper(hekayat_link)


book_list = []
daftar_list = []


def book_scrapper(book_page):
    r = requests.get(book_page)
    soup = BeautifulSoup(r.content, "html.parser")
    book_soup = soup.find_all('a')
    for link in book_soup:
        if link.has_attr('href'):
            if link['href'].startswith(book_page) and link['href'] != book_page:
                daftar_link = link['href']
                daftar_scrapper(daftar_link)

book_link = 'https://ganjoor.net/shabestari/'
#daftar_link = 'https://ganjoor.net/khayyam/robaee/'


book_scrapper(book_link)
#daftar_scrapper(daftar_link)

print("Scraping is finished ...")
print("Outputing the book to IO ...")

with open('shabestari.txt', 'w', encoding="utf8")as bk:
    bk.write("\n".join(book_list))

print("Book is outputed ...")
t_end = time.time()
print("The whole book is scrapped within {} seconds".format(t_end-t_start))
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
# url = "https://quotes.toscrape.com/author/Albert-Einstein/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
authors = soup.find_all('small', class_='author')
quotes = soup.find_all('div', class_='quote')


for quote in quotes:
    authors = quote.find_all('a', class_='tag')
    for t in authors : 
      tag =  t.text.strip()
      print(tag)
# for quote in quotes:
#     fullname = quote.find('span',class_='author')
#     print(fullname)
# first_paragraph = soup.find("p")
# знайти всі теги <p> на сторінці
# all_paragraphs = soup.find_all("p")
# next_sibling = soup.find("span", attrs={"class": "tag-item"})
# author_links = soup.find_all('a', href=lambda link: link and link.startswith("/author/"))
# next_page_link = soup.find('div', attrs={"class": "pager"})
# next_page_link = soup.find("nav", attrs={"class": "next"})
# next_page_url = url + next_page_link['href']
# print(next_page_link)
# next_link = soup.find('li', class_='next')
# l= next_link.find('a').get('href')
# for link in soup.find_all('a'):
    # print(link.get('href'))
# print(quotes)
# print(first_paragraph)
# print(quotes)
# print(all_paragraphs)

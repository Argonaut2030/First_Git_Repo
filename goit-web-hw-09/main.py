import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

def scrape_author_data(url):
  """
  Scrapes author data from the given URL and returns a dictionary.

  Args:
      url: The URL of the author details page.

  Returns:
      A dictionary containing the scraped data or None if scraping fails.
  """
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    author_details = {}
    author_title = soup.find('h3', class_='author-title').text.strip()
    author_description_block = soup.find('div', class_='author-description')
    description = author_description_block.text.strip()
    born_date = soup.find('span', attrs={"class": "author-born-date"}).text.strip()
    born_location = soup.find('span', attrs={"class": "author-born-location"}).text.strip()
    
    author_details['fullname'] = author_title
    author_details['born_date'] = born_date
    author_details['born_location'] = born_location   
    author_details['description'] = description
    return author_details

  except Exception as e:
    print(f"Error scraping author data from {url}: {e}")
    return None
  
def scrape_quotes_data(url):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes_list =[]
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
       quote_details = {}
       author = quote.find('small', class_='author').text.strip()
       quote_text =  quote.find('span', class_='text').text.strip()
       tags = []
       tags_html = quote.find_all('a', class_='tag')
       for t in tags_html : 
         tag =  t.text.strip()
         tags.append(tag)
       quote_details['tags'] = tags
       quote_details['author'] = author
       quote_details['quote'] = quote_text
       quotes_list.append(quote_details)
    return quotes_list
    
  except Exception as e:
    print(f"Error scraping quotes data from {url}: {e}")
    return None
  
def scrape_page(url, data, data2):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all author links on the page
    author_links = soup.find_all('a', href=lambda link: link and link.startswith("/author/"))
    for link in author_links:
        author_url = urljoin(url, link['href'])
        author_data = scrape_author_data(author_url)
        if author_data:
            data.append(author_data)
    quote_data = scrape_quotes_data(url)
    if quote_data:
       data2.extend(quote_data)
    # Find the "Next" link and recursively scrape the next page
    next_page_link = soup.find('li', class_='next')
    if next_page_link:
        next_page_url = urljoin(url,next_page_link.find('a').get('href'))
        scrape_page(next_page_url, data, data2)




def main():
  """
  Scrapes data from the main page and child page (author details) and writes it to a JSON file.
  """
  main_page_url = "https://quotes.toscrape.com/"  # Replace with the actual website URL
  authors_data = []
  quotes_data = []
  scrape_page(main_page_url, authors_data, quotes_data)


  # Write data to JSON file
  if authors_data:
    with open('authors.json', 'w', encoding='utf-8') as outfile:
      json.dump(authors_data, outfile,ensure_ascii=False, indent=4)
    print("Author data scraped successfully and written to authors.json")
  if quotes_data:
    with open('quotes.json', 'w', encoding='utf-8') as outfile:
      json.dump(quotes_data, outfile, ensure_ascii=False, indent=4)
    print("Author data scraped successfully and written to quotes.json")

if __name__ == "__main__":
  main()



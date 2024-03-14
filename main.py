import requests
from bs4 import BeautifulSoup

url = "https://www.bloomberght.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
div = soup.find('div', class_="container")

category_links = div.find_all('a')

for link in category_links:
     category_link = url + link.get('href')
     category_response = requests.get(category_link)
     category_soup = BeautifulSoup(category_response.content, "html.parser")
     category_div = category_soup.find('div', class_="box-row widget-box-news type1")

     if category_div:
          news_links = category_div.find_all('a')

          for news_link in news_links:
               if(news_link.get('href')[0]=='/'):
                    page_link = url + news_link.get('href')
                    page_response = requests.get(page_link)
                    page_soup = BeautifulSoup(page_response.content, "html.parser")
                    page_div = page_soup.find('h1', class_="title")
                    results = page_div.find_all('span')
                    for result in results:
                         print(result.text)
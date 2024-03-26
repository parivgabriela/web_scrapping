import csv
import requests
from bs4 import BeautifulSoup

# import mysql.connector

URL= "https://www.goodreads.com/list/show/9440.100_Best_Books_of_All_Time_The_World_Library_List"
URL_ = '100_Best_Books_of_all_time.html'
try:
    response=requests.get(URL,timeout=5)
    response.raise_for_status()    
except requests.Timeout:
    print("the request has reached")
except requests.RequestException as e:
    print(f"request failed:{e}")

soup = BeautifulSoup(response.text, "html.parser")
books = []


content = soup.find('table', class_ ='tableList')
rows = content.find_all('tr', attrs={'itemscope': ''})


for article in rows:
    title = article.find('span').text
    data_author = article.find('a', attrs={'class': 'authorName'})
    link_book = data_author.get('href')
    author = data_author.text
    rates = article.find('span', attrs={'class': 'minirating'}).text
    
    separated = rates.split()
    rate = separated[0]
    rating = separated[4]

    books.append({
        'title': title,
        'author': author,
        'url': link_book,
        'rate': rate,
        'rating': rating
    })

header = ['title', 'author', 'url', 'rate', 'rating']
with open('good-reads.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(books)

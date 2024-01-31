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

# class="tableList js-dataTooltip

content = soup.find('table', class_ ='tableList')
rows = content.find_all('tr', attrs={'itemscope': ''})

#rows =rows content.find_all('span', attrs={'itemprop': 'name'})

for article in rows:
    # title = article.find('bookTitle')
    print("\n##############inicio##############")
    title = article.find('span').text
    author = article.find('a', attrs={'class': 'authorName'}).text
    #rate
    #rating
    #genre
    #first_published
    
    #a_tag = article.find('a', class_ = 'bookTitle')
    #url = a_tag['href']
    # text = article.find_all('span', attrs={'itemprop': 'name'})
    #title = next.text
    #precio=a_tag

    #precio_tag = article.find_next('span',class_='woocommerce-Price-amount')
    #if precio_tag: 
    #    preciotxt= precio_tag.bdi.text.replace('$','').replace('=','').replace(',','.').replace('\xa','.') # modificacion de caracteres
    #    precio_nro= float(preciotxt)

    #libros.append({
    #    'titulo': titulo,
    #    'url':url,
    #    'precio_pesos': precio_nro
    #})
    print(article)

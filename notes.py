import requests
from bs4 import BeautifulSoup
# scraping

res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.body)
# print(soup.body.contents)

# print(soup.find_all('div'))
# print(soup.find_all('a'))

# print(soup.find('a'))

# print(soup.a)

# print(soup.find(id='score_20514755'))

# CSS selector --->
# print(soup.select('#score_20514755'))
# CSS selector --->

# .titlelink  .storylink  esta es la clase

# Obtener el primer articulo
# print(soup.select('.titlelink')[0])

links = soup.select('.titlelink')[0]
votes = soup.select('.score')

# print(votes[0])


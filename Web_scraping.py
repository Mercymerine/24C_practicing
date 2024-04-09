import requests
from bs4 import BeautifulSoup

results = requests.get('https://www.jumia.co.ke/sporting-goods/')
print(results.status_code)

#print(results.headers) #acceses http header of the webpage to verify that we have indeed accessed the correct page

src = results.content
#print(src)

#Access links
soup = BeautifulSoup(src, 'html.parser')
links = soup.find_all('a')
#print(links)
#print('\n')

#Accessing links with the word About
for link in links:
    if 'About' in link.text:
        print(link)
        print(link.attrs['href'])


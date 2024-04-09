import requests
from bs4 import BeautifulSoup
import re
import csv

def get_url(url):
    #url = 'https://www.jumia.co.ke/hair-care-d/'
    response = requests.get(url)
    #print(response.content)

    soup = BeautifulSoup(response.content, 'html.parser')

    with open('discount.csv', 'w', newline='') as csvfile:
        discounts = soup.find_all('div', class_='bdg _dsct _sm')
        def find_discount():
                for discount in discounts:
                    print(discount.text)
'''
    writer = csv.writer(csvfile)
    writer.writerow(['Discount'])
    for discount in (find_discount()):
        writer.writerow ([discount.text])
'''
get_url('https://www.jumia.co.ke/hair-care-d/')
                
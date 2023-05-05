import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A1000100-2500000%2Cp_n_condition-type%3A8609960031&pd_rd_r=6b825fb0-e103-400e-b5fe-3c2dca315a0e&pd_rd_w=3WK35&pd_rd_wg=zPJxY&pf_rd_p=6e9c5ebb-d370-421b-8375-bf50155e0300&pf_rd_r=ZR7H4MMSMYJ2PTHZJPA5&ref=tile2_10to20K' # replace with the URL of the website you want to scrape

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = []

for product in soup.find_all('div', class_='puis-include-content-margin'):
    name = product.find('h2', class_='a-spacing-none').text.strip()
    price = product.find('span', class_='a-price').text.strip()
    #description = product.find('p', class_='product-description').text.strip()
    image_url = product.find('img')['src']

    products.append({
        'name': name,
        'price': price,
        #'description': description,
        'image_url': image_url
    })

print(products)

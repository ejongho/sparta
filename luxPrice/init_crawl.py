import requests
from bs4 import BeautifulSoup
import numpy as np


# def get_random_ua():
#     random_ua = ''
#     ua_file = 'ua_file.txt'
#     try:
#         with open(ua_file) as f:
#             lines = f.readlines()
#         if len(lines) > 0:
#             prng = np.random.RandomState()
#             index = prng.permutation(len(lines) - 1)
#             idx = np.asarray(index, dtype=np.integer)[0]
#             random_proxy = lines[int(idx)]
#     except Exception as ex:
#         print('Exception in random_ua')
#         print(str(ex))
#     finally:
#         return random_ua

# fake_ua = get_random_ua()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
data = requests.get('https://www.mclabels.com/pages/brands', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
print(soup)

brands = soup.select('div.text-bottom')

for brand in brands:
    # print(brand)
    a_tag = brand.text
    # print(a_tag)

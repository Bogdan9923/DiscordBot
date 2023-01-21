from return_code_dict import returnCodeDict
from bs4 import BeautifulSoup
import requests
import random
import json
import Constants


def get_google_img(query):
    url = "https://www.bing.com/images/search?q=" + str(query)
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    html = requests.get(url, headers=header)

    soup = BeautifulSoup(html.text, 'html.parser')
    a_class = "iusc"
    all_images = soup.findAll('a', class_=a_class)

    numberof_img = len(all_images)
    if numberof_img == 0:
        return Constants.constant_url_default_image
    img_idx = random.randrange(numberof_img)
    selected_img = all_images[img_idx]
    image_src = json.loads(selected_img['m'])['murl']

    if not image_src:
        return Constants.constant_url_default_image

    return image_src


def getImageOf(argument):
    if not argument:
        image = Constants.constant_url_default_image
    else:
        image = get_google_img(''.join(argument))

    return image, returnCodeDict['link']

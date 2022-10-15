from return_code_dict import returnCodeDict
from bs4 import BeautifulSoup
import requests
from PIL import Image
import random

saved_image_name = 'downloaded_image.jpg'
def get_google_img(query):

    url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"

    html = requests.get(url)

    soup = BeautifulSoup(html.content, 'html.parser')

    all_images = soup.findAll('img')

    image_src = None

    rand_idx = random.randint(0, len(all_images)-1)


    while not 'https:' in all_images[rand_idx]['src']:
        rand_idx = random.randint(0, len(all_images))
    else:
        image_src = all_images[rand_idx]['src']


    im = Image.open(requests.get(image_src, stream=True).raw)

    im = im.convert('RGB')

    im.save(saved_image_name)

    if not image_src:
        return 'default_image.jpg'

    return saved_image_name

def getImageOf(argument):

    if not argument:
        image = 'default_image.jpg'
    else:
        image = get_google_img(''.join(argument))

    return image, returnCodeDict['file']
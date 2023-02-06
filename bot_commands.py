import random
from search_image_online import search_online_image
from openAI_chat import query_response
from openAI_image import image_response


def hello():
    return 'Hello !'


def say(text):
    return '{}'.format(text)


def welcome(text):
    return 'Hello {}, welcome to the chat!'.format(text)


def choose(items):
    if items == 'You have no choice':
        return items

    lst = items.split(' ')
    random_idx = random.randint(0, len(lst) - 1)
    text = 'I think "{}" is the way to go.'.format(lst[random_idx])
    return text


def search_img(search):
    return search_online_image(search)


def askai(prompt):
    return query_response(prompt)


def create(prompt):
    return image_response(prompt)

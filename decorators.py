import requests


def consult_animal(function):
    def wrapper(sound):
        if sound == 'meow':
            response = requests.get('https://cat-fact.herokuapp.com/facts')
            print(response.content)
        elif sound == 'woof':
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            print(response.content)
        else:
            return function('Ups')
    return wrapper

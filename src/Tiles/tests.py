import requests as rq

import json


def get_data():
    data = {
        'tile': {
            'author': 'God@gmail.com',
            'title': 'Test tile',
            'type': 'medium',
            'styles': {
                'background': '#b756d',
                'border': '3px solid #00b8a9',
            },
            'elements': [
                {
                    'content_type': 'Text',
                    'columns': '6',
                    'rows': '2',
                    'text': 'Some testing text',
                }
            ],
        }
    }
    return data


def post():
    url = 'http://127.0.0.1:5000/tiles/create-tile/'
    data = get_data()

    response = rq.post(
        url,
        json.dumps(data),
    )
    return response.json()


def get(element_id=1):
    url = f'http://127.0.0.1:5000/tiles/get-tile/{element_id}/'

    response = rq.get(
        url,

    )
    if response.status_code == 404:
        return 'incorrect url\npage notfound'
    return response.json()


if __name__ == '__main__':
    print(get())

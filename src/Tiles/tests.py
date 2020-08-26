import requests as rq

import json


def get_data():
    data = {
        'tile': {
            'author': 'God@mail.ru',
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


def run():
    url = 'http://127.0.0.1:5000/tiles/create-tile/'
    data = get_data()

    response = rq.post(
        url,
        json.dumps(data),
    )
    return response.json()


if __name__ == '__main__':
    print(run())

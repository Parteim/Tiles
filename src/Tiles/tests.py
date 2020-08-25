import requests as rq

import json


def get_data():
    data = {
        'tile': {
            'author': '',
            'title': '',
            'styles': {
                'background': '',
                'border': '',
                'tile': '',
            },
            'elements': [
                {
                    'tile': '',
                    'content_type': '',
                    'columns': '',
                    'rows': '',
                    'text': '',
                }
            ],
        }
    }
    return data


def run():
    url = 'http://127.0.0.1:5000/tiles/create-tile/'
    data = {
        'username': 'Biba',
        'age': 20,
    }

    response = rq.post(
        url,
        json.dumps(data),
    )
    return response.json()


if __name__ == '__main__':
    print(run())

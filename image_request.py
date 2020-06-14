import requests
import json
import argparse

HOST_NAME = 'localhost'
REQUEST_URL = 'http://' + HOST_NAME + ':1219/modelfr'
REQUEST_URL_2 = 'http://' + HOST_NAME + ':1121/modelat'


def send_image_request(image_path):
    URL = image_path + '/shot.jpg'

    # res = requests.post(REQUEST_URL, data={'ip': URL}).json()
    # return print(res)
    # requests.post(
    #     REQUEST_URL, data={'ip': URL})
    requests.post(
        REQUEST_URL_2, data={'ip': URL})
    return -1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()
    send_image_request(args.path)

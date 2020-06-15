import requests
import json
import argparse


HOST_NAME = '34.80.62.248'
REQUEST_URL = 'http://' + HOST_NAME + ':1219/modelfr'
REQUEST_URL_2 = 'http://' + HOST_NAME + ':1121/modelat'


def send_image_request(image_path, ip, model):
    URL = image_path + '/shot.jpg'
    if model == 'at':
        REQUEST_URL = 'http://' + ip + ':1121/modelat'
    else:
        REQUEST_URL = 'http://' + ip + ':1219/modelfr'
    requests.post(
        REQUEST_URL, data={'ip': URL})
    return -1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='ipwebcam path')
    parser.add_argument('--ip', required=True, help='request ip')
    parser.add_argument('--model', required=True, help='at or fr')
    args = parser.parse_args()
    send_image_request(args.path, args.ip, args.model)

import requests
import json
import argparse


def send_image_request(image_path, ip, model):
    URL = image_path + '/shot.jpg'
    if model == 'at':
        REQUEST_URL = 'http://' + ip + ':1121/modelat'
    else:
        REQUEST_URL = 'http://' + ip + ':1219/modelfr'
    # result = requests.post(
    #     REQUEST_URL, data={'ip': URL}).json
    result = requests.get(
        REQUEST_URL, params={'ip': URL}).ip
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help='ipwebcam path')
    parser.add_argument('--ip', required=True, help='request ip')
    parser.add_argument('--model', required=True, help='at or fr')
    args = parser.parse_args()
    while True:
        a = send_image_request(args.path, args.ip, args.model)
        print(a)

import csv
import json
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_response():
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': '2',
    }
    url = base_url + urlencode(params)

    try:
        response = requests.get(url, headers=headers, timeout=1)
        print(response.text)
    except:
        print('error')

    json_response = json.loads(response.text)
    # print(json_response)

    cards = json_response['data']['cards']

    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for single_card in cards:
            blog_content = single_card['mblog']
            content = blog_content['text']
            time = blog_content['created_at'] if blog_content['created_at'] is not None else 'unknown'
            doc = pq(content)
            doc.find('br').remove()
            text_content = doc.text()

            writer.writerow([time, text_content])

if __name__ == '__main__':
    get_response()
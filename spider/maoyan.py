import requests


def get_single_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    return None


def main():
    url = 'http://maoyan.com/board/4'
    html = get_single_page(url)
    print(html)


main()
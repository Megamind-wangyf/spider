#coding: utf-8
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
}
# 这里要加浏览器标识信息，否则知乎会禁止抓取
r = requests.get("https://www.xicidaili.com/nt/", headers=headers)


soup = BeautifulSoup(r.text, 'lxml')
ips = soup.findAll('tr')
# f = open("../src/proxy","w")

proxy_list = []
for x in range(1, len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    print('fdsfds', tds[1], tds[2])
    ip_temp = 'http://'+tds[1].contents[0]+":"+tds[2].contents[0]
    # print tds[2].contents[0]+"\t"+tds[3].contents[0]
    # f.write(ip_temp)
    proxy_list.append(ip_temp)



run_times = 100000

for i in range(run_times):
    for item in proxy_list:
        proxies = {
            'http': item,
            'https': item,
        }
        print(proxies)
        try:
            requests.get('https://blog.csdn.net/qq_43355223', proxies=proxies, timeout=1)
            print('ok')
        except:
            continue
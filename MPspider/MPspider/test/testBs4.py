import re

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    MPname = ['GQ实验室']
    query = ''
    for query in MPname:
        query.encode()
        query_url = 'http://weixin.sogou.com/weixin?type=1&' \
                    's_from=input&query=' + query + '&ie&=utf8&_sug_=n&_sug_type_'

        pagecode = requests.get(query_url).text

    bs = BeautifulSoup(pagecode, 'lxml')
    res = bs.find_all(attrs={'class': 'tit'})
    for tag in res:
        print(tag.contents[1])

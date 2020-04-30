from __future__ import print_function
import urllib3
from bs4 import BeautifulSoup, SoupStrainer, Comment
import re
import warnings

warnings.filterwarnings('ignore')
DestPathPic = 'C:\\Users\\wjyzG\\Desktop\\yuuri\\pic\\'

for m in ['201201', '201202', '201203', '201204', '201205', '201206', '201207', '201208', '201209', '201210', '201211',
          '201212',
          '201301', '201302', '201303', '201304', '201305', '201306', '201307', '201308', '201309', '201310', '201311',
          '201312',
          '201401', '201402', '201403', '201404', '201405', '201406', '201407', '201408', '201409', '201410', '201411',
          '201412',
          '201501', '201502', '201503', '201504', '201505', '201506', '201507', '201508', '201509', '201510', '201511',
          '201512',
          '201601', '201602', '201603', '201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611',
          '201612',
          '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711',
          '201712',
          '201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811',
          '201812',
          '201901', '201902', '201903', '201904', '201905', '201906', '201111', '201112']:

    url = 'http://blog.nogizaka46.com/yuuri.saito/?d=' + str(m)
    http = urllib3.PoolManager()
    response = http.request('GET', url, timeout=5)

    print(m, "response状态：", response.status)

    soup = BeautifulSoup(response.data, "lxml")
    id_check = soup.find(id="sheet")

    # 爬取博客页数

    page_check = soup.find(class_='paginate')
    page_all = re.findall('\xa0(.*?)\xa0', str(page_check))
    page = len(page_all)
    if page == 0:
        page = 1

    print(m, '共有', page, '页')

    k = 1
    while k <= page:
        url = 'http://blog.nogizaka46.com/yuuri.saito/?p=' + str(k) + '&d=' + str(m)
        response = http.request('GET', url, timeout=5)
        soup = BeautifulSoup(response.data, "lxml")
        id_check = soup.find(id="sheet")

        pic = id_check.find_all('img')

        import re

        pic_url = re.findall('https.*?j.*?g', str(id_check))
        pic_name = []
        for i in pic_url:
            try:
                temp = re.findall('20.*?/.*?/.*', i)
                temp[0] = temp[0].replace('/', '_')
                pic_name.append(temp[0])
            except Exception:
                pass

        # 保存图片

        import requests

        i = 0
        for url in pic_url:
            try:
                Pic = requests.get(url)
                fp = open(DestPathPic + str(m) + '\\' + pic_name[i], "wb")  # 保存文件
                fp.write(Pic.content)  # 将文件写入到指定的目录文件夹下
                fp.close()
                i = i + 1
            except Exception:
                pass
        print(m, '_', k, "pic_finish")

        k += 1

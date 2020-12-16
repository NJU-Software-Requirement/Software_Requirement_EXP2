import requests as rq
from bs4 import BeautifulSoup
from threading import Thread

url = 'https://bugs.eclipse.org/bugs/show_bug.cgi?id=567040'
proxy = {
    'http': '127.0.0.1:23334',
    'https': '127.0.0.1:23334'
}
count = 10
max = 569686
# r = rq.get(url, allow_redirects=False, proxies=proxy)

# bf = BeautifulSoup(r.text, 'html.parser')
# print(bf)
#fw = open('test.txt', 'w', encoding='utf-8')
# fw.write(str(bf))
'''
Table = bf.find('td', class_='bz_show_bug_column', id='bz_show_bug_column_1')
print(Table)
print('---------------------------------------------------------------')
print(Table.find_all('td')[6].get_text())
'''

error_urllist = []
res = []

for i in range(569686, 559686, -1):
    url = 'https://bugs.eclipse.org/bugs/show_bug.cgi?id={}'.format(i)
    r = rq.get(url, allow_redirects=False, proxies=proxy)
    bf = BeautifulSoup(r.text, 'html.parser')
    if bf.find('div', id='error_msg', class_='throw_error'):
        print("Error ID :" + url)
        error_urllist.append(i)
    else:
        # print(r.status_code, r.url)
        Table = bf.find('td', class_='bz_show_bug_column', id='bz_show_bug_column_1')
        title = bf.find('span', id='short_desc_nonedit_display').string
        product = Table.find_all('td')[4].get_text().replace('\n', '')
        component = Table.find_all('td')[6].get_text().replace(' ', '').replace('\n', ' ').split('  (showotherbugs)')[0]
        imp = Table.find_all('td')[10].get_text().replace(' ', '').replace('\n', ' ')
        res.append([str(i), title, product, component, imp.split()[0] + ' ' + imp.split()[1]])

print(len(res))
fw = open('data.txt', 'w', encoding='utf-8')
for item in res:
    tmp = ' '.join(item)
    fw.write(tmp + '\n')
fw.close()

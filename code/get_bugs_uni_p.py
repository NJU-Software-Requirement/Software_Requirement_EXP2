import requests as rq
from bs4 import BeautifulSoup
from threading import Thread
import json
import time

proxy = {
    'http': '127.0.0.1:23334',
    'https': '127.0.0.1:23334'
}
error_urllist = []
res = {}
th_count = 0

bugs_count = [0, 0, 0, 0, 0]

def my_sum(arr):
    res = 0
    for i in arr:
        res += i
    return res

def get_bug(i): 
    global th_count
    global bugs_count
    global error_urllist
    for id in range(i, i + 300):
        try:
            url = 'https://bugs.eclipse.org/bugs/show_bug.cgi?id={}'.format(id)
            r = rq.get(url, allow_redirects=False, proxies=proxy, timeout=5)
            # r = rq.get(url, allow_redirects=False, timeout=5)
            # r = rq.get(url, allow_redirects=False)
            bf = BeautifulSoup(r.text, 'html.parser')
            if bf.find('div', id='error_msg', class_='throw_error'):
                print("Error ID: " + id)
                error_urllist.append(id)
            else:
                # print(id)
                # print(r.status_code, r.url)
                Table = bf.find('td', class_='bz_show_bug_column',id='bz_show_bug_column_1')
                # title = bf.find('span', id='short_desc_nonedit_display').string
                title = bf.find('span', id='short_desc_nonedit_display').get_text().replace('  ', ' ')
                product = Table.find_all('td')[4].get_text().replace('\n', '')
                comp = Table.find_all('td')[6].get_text().replace('\n', '').split('  (show other bugs)')[0]
                imp = Table.find_all('td')[10].get_text().replace(' ', '').replace('\n', ' ')
                imp = imp.split()[0] + ' ' + imp.split()[1]
                if imp.split()[0] == 'P1':
                    if bugs_count[0] < 3000 and my_sum(bugs_count) < 10000:
                        bugs_count[0] += 1
                        temp = {'title': title, 'product': product,
                                'component': comp, 'importance': imp}
                        res[id] = temp
                    elif my_sum(bugs_count) >= 100000:
                        break
                elif imp.split()[0] == 'P2':
                    if bugs_count[1] < 3000 and my_sum(bugs_count) < 10000:
                        bugs_count[1] += 1
                        temp = {'title': title, 'product': product,
                                'component': comp, 'importance': imp}
                        res[id] = temp
                    elif my_sum(bugs_count) >= 100000:
                        break
                elif imp.split()[0] == 'P3':
                    if bugs_count[2] < 3000 and my_sum(bugs_count) < 10000:
                        bugs_count[2] += 1
                        temp = {'title': title, 'product': product,
                                'component': comp, 'importance': imp}
                        res[id] = temp
                    elif my_sum(bugs_count) >= 100000:
                        break
                elif imp.split()[0] == 'P4':
                    if bugs_count[3] < 3000 and my_sum(bugs_count) < 10000:
                        bugs_count[3] += 1
                        temp = {'title': title, 'product': product,
                                'component': comp, 'importance': imp}
                        res[id] = temp
                    elif my_sum(bugs_count) >= 100000:
                        break
                elif imp.split()[0] == 'P5':
                    if bugs_count[4] < 3000 and my_sum(bugs_count) < 10000:
                        bugs_count[4] += 1
                        temp = {'title': title, 'product': product,
                                'component': comp, 'importance': imp}
                        res[id] = temp
                    elif my_sum(bugs_count) >= 100000:
                        break
        except:
            print('Network Error!', id)
        time.sleep(0.5)
    th_count += 1
    print('OK!', th_count)


# ts = [Thread(target=get_bug, args=(i,)) for i in range(569686, 559686, -100)]
ts = [Thread(target=get_bug, args=(i,)) for i in range(1, 60001, 300)]

for t in ts:
    t.start()
for t in ts:
    t.join()

print('Finish!')
print(len(res))

fw = open('data_uni_p_more.json', 'w', encoding='utf-8')
json.dump(res, fw, indent=4)
fw.close()
'''
fw = open('data_20K.txt', 'w', encoding='utf-8')
for item in res:
    tmp = str(item) + ' '.join(list(res[item].values()))
    fw.write(tmp + '\n')
fw.close()
'''
'''
fw = open('error_uni_p.txt', 'w', encoding='utf-8')
for item in error_urllist:
    fw.write(str(item) + '\n')
fw.close()
'''
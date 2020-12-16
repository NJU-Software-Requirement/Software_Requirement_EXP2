import requests as rq
from bs4 import BeautifulSoup
from threading import Thread
import json
import time

proxy = {
    'http': '127.0.0.1:10809',
    'https': '127.0.0.1:10809'
}

api_url = 'https://api.github.com/repos/microsoft/vscode/issues?state=closed&sort=created&direction=asc&per_page=100&labels=feature-request&page={}'
html_url = 'https://github.com/microsoft/vscode/issues/{}'
header = {'Authorization': 'token 163da4d768880c42e809078e8fe5cffb2b80a263'}
res = []


# for i in range(100):

def get_issue(begin):
    # r = rq.get(api_url.format(i + 1), headers=header, proxies=proxy)
    for i in range(begin, begin + 25):
        r = rq.get(api_url.format(i + 1), headers=header)
        r_json = r.json()
        for issue in r_json:
            number = issue['number']
            comments = issue['comments']
            title = issue['title']
            body = issue['body']
            labels = []
            for label in issue['labels']:
                labels.append(label['name'])
            emojis = {}
            # rsp = rq.get(html_url.format(number), allow_redirects=False, proxies=proxy)
            rsp = rq.get(html_url.format(number))
            if rsp.status_code != 200:
                print(number, rsp.status_code)
            bf = BeautifulSoup(rsp.text, 'html.parser')
            if bf.find('div', class_='comment-reactions-options'):
                # print(number)
                table = bf.find('div', class_='comment-reactions-options')
                for emoji in table.find_all('button'):
                    emojis[emoji.contents[1]['alias']] = emoji.contents[2].strip()
            res.append({'ID': number, 'title': title, 'body': body, 'comments': comments, 'labels': labels, 'emojis': emojis})
            time.sleep(3)
        print('page ' + str(i + 1))


ts = [Thread(target=get_issue, args=(i,)) for i in range(0, 100, 25)]
for t in ts:
    t.start()
for t in ts:
    t.join()

print('Finish!')

fw = open('issues.json', 'w', encoding='utf-8')
json.dump(res, fw, indent=4)
fw.close()

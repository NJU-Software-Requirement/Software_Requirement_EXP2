import pickle
import json
import time
import requests as rq
from bs4 import BeautifulSoup


proxy = {
    'http': '127.0.0.1:10809',
    'https': '127.0.0.1:10809'
}

url = 'https://github.com/microsoft/vscode/issues/{}'

fr = open('issues.json', 'r', encoding='utf-8')
issues = json.load(fr)
fr.close()
'''
fr = open('issues.json', 'r', encoding='utf-8')
issues = json.load(fr)
fr.close()
'''


count = 1
for issue in issues:
    print('count:', count)
    if issue['status'] == 0:
        while True:
            id = issue['ID']
            # print(id)
            r = rq.get(url.format(id))
            if r.status_code == 200:
                emojis = {}
                bf = BeautifulSoup(r.text, 'html.parser')
                if bf.find('div', class_='comment-reactions-options'):
                    # print(number)
                    table = bf.find('div', class_='comment-reactions-options')
                    for emoji in table.find_all('button'):
                        emojis[emoji.contents[1]['alias']] = emoji.contents[2].strip()
                issue['emojis'] = emojis
                issue['status'] = 1
                fw = open('issues.json', 'w', encoding='utf-8')
                json.dump(issues, fw, indent=4)
                fw.close()
                break
            # time.sleep(2)
    count += 1

print('Finish!')
fw = open('issues.json', 'w', encoding='utf-8')
json.dump(issues, fw, indent=4)
fw.close()

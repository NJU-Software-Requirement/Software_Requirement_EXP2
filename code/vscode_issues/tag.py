import pickle
import json
import time
import requests as rq
from bs4 import BeautifulSoup

fr = open('issues_bak.json', 'r', encoding='utf-8')
issues = json.load(fr)
fr.close()

for issue in issues:
    if len(issue['emojis']) > 0:
        issue['status'] = 1
    else:
        issue['status'] = 0

fw = open('issues_bak.json', 'w', encoding='utf-8')
json.dump(issues, fw, indent=4)
fw.close()

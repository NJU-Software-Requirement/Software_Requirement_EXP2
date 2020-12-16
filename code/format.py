import json

exchange = {
    '\u00b4': "'",
    '\u201c': "'",
    '\u201d': "'",
    '\u2018': "'",
    '\u2019': "'",
    '\uff08': '(',
    '\uff09': ')',
    '\uff1f': '?',
    '\u00a0': ' ',
    '\u200b': '',
    '\u2026': '...',
    '\u3010': '[',
    '\u3011': ']',
    '\u20ac': '',
    '\u00e9': 'e',
    '\ufffd': '',
    '\uff0c': '',
    '\uff01': '',
    '\u00e3': 'a',
    '\u3001': "'",
    '\u00e7': ''
}

fr = open('data_uni_more.json', 'r', encoding='utf-8')
data = json.load(fr)
fr.close()

fr = open('stopword.txt', 'r', encoding='utf-8')
stoplist = fr.read().splitlines()
fr.close()

res = []
for item in data.values():
    title = item['title']
    for ch in title:
        if ch >= '\u4e00' and ch <= '\u9fff':
            title = title.replace(ch, '')
    for key in exchange:
        title = title.replace(key, exchange[key])
    temp = title + ' ' + item['product'] + ' ' + item['component']
    temp = temp.lower()
    temp = temp.split()
    for word in stoplist:
        if word in temp:
            temp.remove(word)
    temp = ' '.join(temp)
    imp = item['importance'].split()[1]
    if imp == 'critical':
        imp = 'blocker'
    if imp == 'trivial':
        imp = 'enhancement'
    res.append({imp: temp})

fw = open('bugs_uni_more.json', 'w', encoding='utf-8')
json.dump(res, fw, indent=4)
fw.close()

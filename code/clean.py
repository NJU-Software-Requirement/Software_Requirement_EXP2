import json

fr = open('data.json', 'r', encoding='utf-8')
data = json.load(fr)
fr.close()
for item in data.values():
    item['component'] = item['component'].strip()
    item['title'] = item['title'].replace('  ', ' ')
fw = open('data.json', 'w', encoding='utf-8')
json.dump(data, fw, indent=4)
fw.close()
fw = open('data.txt', 'w', encoding='utf-8')
for item in data:
    tmp = str(item) + ' ' + ' '.join(list(data[item].values()))
    fw.write(tmp + '\n')
fw.close()

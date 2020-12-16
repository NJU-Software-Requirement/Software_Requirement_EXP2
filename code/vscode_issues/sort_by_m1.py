import json


def judge(issue):
    pass


fr = open('issues.json', 'r', encoding='utf-8')
issues = json.load(fr)
fr.close()
res = {}
for issue in issues:
    res[issue['ID']] = [issue['comments'], issue['emojis'], issue['title']]
sort_res = sorted(res.items(), key=lambda item: item[1][0], reverse=True)
fw = open('sort_issues_m1.txt', 'w', encoding='utf-8')
for issue in sort_res:
    emoji_str = ''
    # print(issue[1])
    for emoji in issue[1][1]:
        emoji_str += emoji + ': ' + issue[1][1][emoji] + '||'
    tmp = 'ID:' + str(issue[0]) + '----' + 'Comment: ' + str(issue[1][0]) + '----' + emoji_str
    fw.write(tmp + '\n')
fw.close()

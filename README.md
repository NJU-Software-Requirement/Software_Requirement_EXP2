# Software_Requirement_EXP2
我们的实验即将完成，肝报告ing
```
Software_Requirement_EXP2
 |----code                              实验代码
 |----data                              实验数据
 |----img                               实验图片
 |----README.md                         您现在看到的文件
 ```
 
### data文件夹结构

```
data
 |----data.json                         bugzilla最近提出的近10000个bug的数据
 |----data2.json                        bugzilla最早提出的近5000个bug的数据
 |----data_20k.json                     bugzilla最早提出的近9000个bug的数据
 |----data_uni.json                     bugzilla最早提出的、按照严重性分类较为均匀的近8000个bug的数据
 |----data_uni_more.json                bugzilla最早提出的、按照严重性分类较为均匀的10000个bug的数据
 |----data_uni_p.json                   bugzilla最早提出的、按照优先级分类较为均匀的近7000个bug的数据
 |----data_uni_p_more.json              bugzilla最早提出的、按照优先级分类较为均匀的10000个bug的数据
 |----bugs.json                         将data.json中bug按照优先级分类的深度学习数据
 |----bugs2.json                        将data2.json中bug按照优先级分类的深度学习数据
 |----bugs_20k.json                     将data_20k.json中bug按照严重性分类的深度学习数据
 |----bugs_b.json                       将data.json中bug按照严重性分类的深度学习数据
 |----bugs_uni.json                     将data_uni.json中bug按照严重性分类的深度学习数据
 |----bugs_uni_more.json                将data_uni_more.json中bug按照严重性分类的深度学习数据
 |----issues.json                       github上关于vscode的具有'feature-request'标签的9900个issue的数据
 |----issues_bak.json                   github上关于vscode的具有'feature-request'标签的9900个issue的不完全数据
 |----sort_issues_m1.txt                将issues.json中issue按照评论数排序
 |----stopword.txt                      停用词表
 |----val_sorted.json                   将每条bug数据计算出一个val值进行排序（val计算方法见报告）
 |----val_sorted.csv                    内容同上，保存成csv方便浏览
```

### code 文件夹结构

```
code
 |----NLP
 |     |----bert-base-uncased
 |     |----data
 |     |     |----bugs.json
 |     |----dataloader.py
 |     |----main.py
 |     |----main_bak.py
 |----vscode-issues
 |     |----get_data.py
 |     |----re_get.py
 |     |----sort_by_m1.py
 |     |----tag.py
 |----clean.py
 |----format.py
 |----get_bugs.py
 |----get_bugs_uni.py
 |----get_bugs_uni_p.py
 |----get_bugs_v2.py
 |----dataClean0.py
```


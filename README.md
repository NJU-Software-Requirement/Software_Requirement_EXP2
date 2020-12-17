# Software_Requirement_EXP2
我们的实验即将完成，肝报告ing

### data文件夹结构

```
data
 |----data.json				bugzilla最近提出的近10000个bug的数据
 |----data2.json			bugzilla最早提出的近5000个bug的数据
 |----data_20k.json			bugzilla最早提出的近9000个bug的数据
 |----data_uni.json			bugzilla最早提出的、按照严重性分类较为均匀的近8000个bug的数据
 |----data_uni_more.json		bugzilla最早提出的、按照严重性分类较为均匀的10000个bug的数据
 |----data_uni_p.json			bugzilla最早提出的、按照优先级分类较为均匀的近7000个bug的数据
 |----data_uni_p_more.json		bugzilla最早提出的、按照优先级分类较为均匀的10000个bug的数据
 |----bugs.json				将data.json中bug按照优先级分类的深度学习数据
 |----bugs2.json			将data2.json中bug按照优先级分类的深度学习数据
 |----bugs_20k.json			将data_20k.json中bug按照严重性分类的深度学习数据
 |----bugs_b.json			将data.json中bug按照严重性分类的深度学习数据
 |----bugs_uni.json			将data_uni.json中bug按照严重性分类的深度学习数据
 |----bugs_uni_more.json		将data_uni_more.json中bug按照严重性分类的深度学习数据
 |----issues.json			github上关于vscode的具有'feature-request'标签的9900个issue的数据
 |----issues_bak.json			github上关于vscode的具有'feature-request'标签的9900个issue的不完全数据
 |----sort_issues_m1.txt		将issues.json中issue按照评论数排序
 |----stopword.txt			停用词表
 |----val_sorted.json 将每条bug数据计算出一个val值进行排序（val计算方法见报告）
 |----val_sorted.csv 内容同上，保存成csv方便浏览
```


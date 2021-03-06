text = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
#将字符串中的better替换为worse
string1 = text.replace("better","worse")

#将含有ea的单词剔除
list1 = string1.split()
list2 = []
list3 = []
for i in list1:                        #将特殊字符清洗掉
    string2 = i.strip(",.*!-")
    list2.append(string2)
for i in list2:
    if "ea" not in i:
        list3.append(i)

#将字母进行大小写转换
list4 = []
for i in list3:
    string3 = i.swapcase()
    list4.append(string3)

#将所有字母按升序排列
list4.sort()
print(list4)
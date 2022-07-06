import pandas as pd

#資料索引

'''
data = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])
'''

'''
print(data)
'''

#觀察資料

'''
print('資料型態', data.dtype)
print('資料數量', data.size)
print('資料索引', data.index)
'''

#取得資料

'''
print(data[2]) #根據順序，印出第三個數
print(data["e"]) #根據索引，印出第五個數
'''

#數字運算

'''
print('最大值', data.max())
print('最小值', data.min())
print('總和', data.sum())
print('標準差', data.std())
print('中位數', data.median())
print('最大三個數\n', data.nlargest(3))
print('最小兩個數\n', data.nsmallest(2))
'''

#字串運算


data = pd.Series(['你好', 'Iam', 'Pig'])


'''
print(data.str.upper())
print(data.str.lower())
'''

'''
print(data.str.len()) #算出每個字串的長度
'''

'''
print(data.str.cat(sep = " ")) #把字串串起來，sep為字串之間的符號(可省略)
'''

'''
print(data.str.contains("I")) #搜尋字串
'''


print(data.str.replace('你好', 'Hello')) #取代字串
import pandas as pd 

#資料索
data = pd.DataFrame({
    "name" : ["amy", "cassie", "lisa"],
    "salary" : [30000, 100000, 50000]
}, index = ['a', 'b', 'c']) #index可省略

'''
print(data)
'''

#觀察資料
'''
print("資料數量", data.size)
print("資料形狀(列, 欄)", data.shape)
print("資料索引", data.index)
'''

#取得列(橫)的series資料
'''
print("取得第二列", data.iloc[1], sep = "\n") #以sep值將自串連起來 #根據順序
print()
print("取得第b列", data.loc["b"], sep = "\n") #根據索引
'''

#取得欄(直)的series資料
'''
print("取得name欄位", data["name"], sep = "\n")
'''

'''
names = data["name"] #創建name的series資料
print(names.str.upper(), sep = "\n") #把names轉大寫
'''

'''
salaries = data["salary"]
print(salaries.mean()) #取得薪水平均值
'''

#建立新欄位

data["age"] =[15, 20, 30]
data["rank"] = pd.Series([3, 6, 1], index = ['a', 'b', 'c'])
data["cp"] = data["salary"] / data["age"]
print(data)
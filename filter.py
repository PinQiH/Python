import pandas as pd 

#series篩選練習
'''
data = pd.Series([30, 15, 20])
print(data)
'''

'''
condition = [True, False, True]
'''

'''
condition = data > 18
print(condition)
filtereddata = data[condition]
print(filtereddata)
'''

'''
data = pd.Series(["您好", "python", "pandas"])
print(data)
'''

'''
condition = [False, True, True]
'''

'''
condition = data.str.contains("p")
print(condition)
filtereddata = data[condition]
print(filtereddata)
'''

#dataframe篩選練習
data = pd.DataFrame({
    "name" : ["amy", "bob", "charles"],
    "salary" : [30000, 50000, 40000]
})
print(data)

'''
condition = [False, True, True]
'''

'''
condition = data["salary"] >= 40000
'''

condition = data["name"] == "amy"
print(condition)
filtereddata = data[condition]
print(filtereddata)
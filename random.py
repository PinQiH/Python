#random
import random

'''
data = random.choice([1, 5, 6, 10, 20]) #隨機取一個數
print(data)
'''

'''
data = random.sample([1, 5, 6, 10, 20], 3) #隨機取多個數
print(data)
'''

'''
data = [1, 5, 8, 20]
random.shuffle(data) #隨機調換順序
print(data)
'''

'''
data = random.random() #0~1隨機取數
print(data)
'''

'''
data = random.uniform(0.0, 1.0) #數字間隨機取數
print(data)
'''

'''
data = random.normalvariate(100, 10) #常態分布(平均, 標準差)
print(data)
'''
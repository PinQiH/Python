#模擬退火演算法

import numpy as np 
from sklearn.metrics.pairwise import euclidean_distances
import math
import random
from random import shuffle
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
from itertools import permutations

#設定參數
t0 = 500 #起始溫度
tmin = 0.1 #最低溫度，意味著迭代結束的溫度點
k = 40 #每次降溫階段中內循環的運算次數
N = 5. #為城市點數量，根據 N 決定生成 N*N 的距離矩陣
coolnum = 0.98 #於每次迭代過程中的衰退速率

#生成距離矩陣
distmap = np.array([(0, 38, 19, 19, 18),
                    (38, 0, 38,	30,	43),
                    (19, 38, 0,	43,	40),
                    (19, 30, 43, 0, 10),
                    (18, 43, 40, 10, 0),])

#計算總距離
def TtotalDistance(Route0):
    distance = sum([distmap[Route0[i],Route0[i+1]] for i in range(len(Route0)-1)])
    return distance
    
#為判斷是否能求出最佳解，採用窮舉法(Method of exhaustion)
def exhaustive(Route0):
    Route1 = Route0
    special_start = []
    permutDis = []
    eveans = list(permutations(Route1, 6))
    for i in range(len(eveans)):
        if eveans[i][0] == Route0[0] and eveans[i][-1] == Route0[-1]:
            special_start.append(eveans[i])
    for i in range(len(special_start)):
        dis = TtotalDistance(special_start[i])
        permutDis.append(dis)
    smallest_distance = min(permutDis)
    arr = permutDis.index(smallest_distance)
    smallest_route = special_start[arr]
    return smallest_route, smallest_distance

#產生新路徑
def Inversion(Route0):
    Copy = Route0.copy()
    place  = random.sample([1,2,3,4],2) #起點跟終點固定
    Copy[place[0]],Copy[place[1]] = Copy[place[1]],Copy[place[0]] #每次交換 2 個城市的先後順序來產生一新路徑
    return Copy

#初始化路徑
Route0 = random.sample(range(0, 5), 5)
Route0.append(Route0[0]) 
total_distance = TtotalDistance(Route0)
print('Initial Route: ', Route0)
print('Initial distance: ', total_distance)
print('===============================================')
print('By using method of exhustive, can get the min distance below: ')
print("Smallest num by exhaustive: ", exhaustive(Route0))

evetime_distance = []
evetime_route = []

t = t0

while True:
    if t <= tmin:
        break
    for times in range(k):
        new_Route = Inversion(Route0)
        new_distance = TtotalDistance(new_Route)
        diff = new_distance - total_distance
        if diff <= 0:
            Route0 = new_Route
            total_distance = new_distance
        else:
            prob = math.exp(-diff/t)
            randnum = random.uniform(0,1)
            if randnum < prob:
                Route0 = new_Route
                total_distance = new_distance
            else:
                Route0 = Route0
                total_distance = total_distance
    evetime_route.append(Route0)
    evetime_distance.append(total_distance)
    t = t * coolnum

print('Final Route: ',evetime_route[-1])
print('Final Distance: ',evetime_distance[-1])

plt.figure(figsize = (15,8))
plt.xlabel("Iteration",fontsize = 15)
plt.ylabel("Distance",fontsize = 15)

plt.plot(evetime_distance,linewidth = 2.5, label = "Everytime smallest distance", color = 'r')
plt.legend()
plt.show()

#2-opt

import numpy as np
import random
from random import shuffle
import matplotlib.pyplot as plt
from itertools import permutations

#在這裡設定迭代停止條件，要多嘗試一些不同數值，最好設定大一點
MAXCOUNT = 422

#資料在這裡輸入，依次鍵入每個城市的座標
cities = np.array([(0, 38, 19, 19, 18),
                   (38, 0, 38, 30, 43),
                   (19, 38, 0, 43, 40),
                   (19, 30, 43, 0, 10),
                   (18, 43, 40, 10, 0),])

def calPathDist(indexList):
    distance = sum([cities[indexList[i], indexList[i+1]] for i in range(len(indexList)-1)])
    return distance    

#path1長度比path2短則返回true
def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False
    
def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]
    
def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath
    
def updateBestPath(bestPath):
    count = 0
    evetime_distance = []
    evetime_route = []
    while count < MAXCOUNT:
        evetime_distance.append(calPathDist(bestPath))
        evetime_route.append(bestPath.tolist())
        #print(calPathDist(bestPath))
        #print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath, evetime_distance, evetime_route
    
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
        dis = calPathDist(special_start[i])
        permutDis.append(dis)
    smallest_distance = min(permutDis)
    arr = permutDis.index(smallest_distance)
    smallest_route = special_start[arr]
    return smallest_route, smallest_distance

def opt2():
    Route0 = random.sample(range(0, 5), 5)
    Route0.append(Route0[0]) 
    total_distance = calPathDist(Route0)
    print('Initial Route: ', Route0)
    print('Initial distance: ', total_distance)
    print('===============================================')
    print('By using method of exhustive, can get the min distance below: ')
    print("Smallest num by exhaustive: ", exhaustive(Route0))

    #隨便選擇一條可行路徑
    bestPath = np.arange(0, len(cities))
    bestPath = np.append(bestPath, 0)
    bestPath, evetime_distance , evetime_route = updateBestPath(bestPath)

    #print(evetime_route)
    #print(evetime_distance)

    print('Final Route: ', evetime_route[-1])
    print('Final Distance: ', evetime_distance[-1])

    plt.figure(figsize = (15,8))
    plt.xlabel("Iteration", fontsize = 15)
    plt.ylabel("Distance", fontsize = 15)

    plt.plot(evetime_distance, linewidth = 2.5, label = "Everytime smallest distance", color = 'r')
    plt.legend()
    plt.show()
    
opt2()

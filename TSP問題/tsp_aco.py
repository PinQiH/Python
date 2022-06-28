import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import random
from itertools import permutations

antcount = 100 #螞蟻數量
citycount = 5 #城市數量
alpha= 1 #信息速重要程度因子
beta = 2 #啟發函數重要程度因子
rho = 0.1 #揮發速度
iter = 0 #迭代初始值
maxiter = 422 #最大迭代次數
Q = 1

cityname = ['0', '1', '2', '3', '4']

#距離矩陣
distance = np.array([(0.1, 38, 19, 19, 18),
                     (38, 0.1, 38, 30, 43),
                     (19, 38, 0.1, 43, 40),
                     (19, 30, 43, 0.1, 10),
                     (18, 43, 40, 10, 0.1),])

#距離倒數矩陣
etable = 1.0 / distance

#初始信息矩陣
pheromonetable = np.ones((citycount, citycount))

#候選集列表，存放100隻螞蟻的路徑
candidate = np.zeros((antcount, citycount)).astype(int)

#每次迭代後的相應最佳路徑
pathbest = np.zeros((maxiter, citycount))

#每次迭代後的最佳路徑距離
distancebest = np.zeros(maxiter)

#所有螞蟻的路徑距離
lengthall = []

#所有螞蟻路徑
candidateall = []

while iter < maxiter:
    #螞蟻初始點
    if antcount <= citycount:
        candidate[:, 0] = np.random.permutation(range(citycount))[:antcount]
    else:
        m = antcount - citycount
        n = 2
        candidate[:citycount, 0] = np.random.permutation(range(citycount))[:]
        while m > citycount:
            candidate[citycount * (n - 1):citycount * n, 0] = np.random.permutation(range(citycount))[:]
            m = m - citycount
            n = n + 1
        candidate[citycount * (n - 1):antcount, 0] = np.random.permutation(range(citycount))[:m]
    length = np.zeros(antcount) #每次迭代的n個螞蟻距離值

    #選擇下一個城市
    for i in range(antcount):
        unvisit = list(range(citycount)) #沒有訪問的城市編號
        visit = candidate[i, 0] #第i個螞蟻的第1個城市
        unvisit.remove(visit) #移除已去過的第一個城市
        for j in range(1, citycount):
            protrans = np.zeros(len(unvisit)) #每次都更新沒訪問的城市列表
            for k in range(len(unvisit)):
                protrans[k] = np.power(pheromonetable[visit][unvisit[k]], alpha) * np.power(etable[visit][unvisit[k]], (alpha + 1)) #計算信息素等等

            cumsumprobtrans = (protrans / sum(protrans)).cumsum()
            cumsumprobtrans -= np.random.rand()
            
            k = unvisit[list(cumsumprobtrans > 0).index(True)]

            candidate[i, j] = k #下一個城市的索引值
            unvisit.remove(k)
            length[i] += distance[visit][k]
            visit = k #更改出發點
        length[i] += distance[visit][candidate[i, 0]] #最後一個城市的距離也要加進去

    lengtha = length.tolist()
    lengthall.append(lengtha)

    candidatea = candidate.tolist()
    candidateall.append(candidatea)

    if iter == 0:
        distancebest[iter] = length.min()
        pathbest[iter] = candidate[length.argmin()].copy()
    else:
        if length.min() > distancebest[iter - 1]:
            distancebest[iter] = distancebest[iter - 1]
            pathbest[iter] = pathbest[iter - 1].copy()
        else:
            distancebest[iter] = length.min()
            pathbest[iter] = candidate[length.argmin()].copy()
    
    #信息訴的增加量矩陣
    changepheromonetable = np.zeros((citycount, citycount))
    for i in range(antcount):
        for j in range(citycount - 1):
            changepheromonetable[candidate[i, j]][candidate[i][j + 1]] += Q / length[i]
        changepheromonetable[candidate[i, j + 1]][candidate[i, 0]] += Q / length[i]

    pheromonetable = (1 - rho) * pheromonetable + changepheromonetable
    iter += 1

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

def calPathDist(indexList):
    caldistance = sum([distance[indexList[i], indexList[i+1]] for i in range(len(indexList)-1)])
    return caldistance   

route0 = pathbest[0].tolist()
route0.append(route0[0])
route00 = list(map(int, route0))

routecandidate = candidateall[0][0]
routecandidate.append(routecandidate[0])

print('Initial Route: ', routecandidate)
print('Initial distance: ', lengthall[0][0])
print('===============================================')
print('By using method of exhustive, can get the min distance below: ')
print("Smallest num by exhaustive: ", exhaustive(route00))

ppathbest = pathbest[-1] + 1
route = ppathbest.tolist()
route.append(route[0])
routebest = list(map(int, route))

print('Final Route: ', routebest)
print('Final Distance: ', distancebest[-1])

plt.figure(figsize = (15,8))
plt.xlabel("Iteration", fontsize = 15)
plt.ylabel("Distance", fontsize = 15)

plt.plot(distancebest, linewidth = 2.5, label = "Everytime smallest distance", color = 'r')
plt.legend()
plt.show()

plt.figure(figsize = (15,8))
plt.xlabel("Ants", fontsize = 15)
plt.ylabel("Distance", fontsize = 15)

plt.title('First Iteration')
plt.plot(lengthall[0], linewidth = 2.5, label = "Every ants distance", color = 'r')
plt.legend()
plt.show()

plt.figure(figsize = (15,8))
plt.xlabel("Ants", fontsize = 15)
plt.ylabel("Distance", fontsize = 15)

plt.title('200th Iteration')
plt.plot(lengthall[199], linewidth = 2.5, label = "Every ants distance", color = 'r')
plt.legend()
plt.show()

plt.figure(figsize = (15,8))
plt.xlabel("Ants", fontsize = 15)
plt.ylabel("Distance", fontsize = 15)

plt.title('422th Iteration')
plt.plot(lengthall[-1], linewidth = 2.5, label = "Every ants distance", color = 'r')
plt.legend()
plt.show()
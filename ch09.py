#1
'''
soldier0 = {'tag' : 'red', 'score' : 3}
print('你剛打死', soldier0['tag'], '小兵', '可以得到', soldier0['score'], '分')
'''

#2
'''
fruits = True
fruits = {'西瓜' : 15, '香蕉' : 20, '水蜜桃' : 25}
while fruits:
    key = input()
    if key == 'q':
        break
    elif key in fruits:
        print("%s 已在字典中" % key)
        break
    else:
        value = input()
        fruits[key] = value
        print("新字典 =", fruits)
        break
'''

#3
'''
armys = []
for soldier_number in range(10):
    soldier = {'tag' : 'red', 'score' : 3, 'speed' : 'slow'}
    armys.append(soldier)
for soldier in armys[-3:]:
    soldier['tag'] = 'green'
    soldier['score'] = 10
    soldier['speed'] = 'fast'
print(armys)
'''

#4
'''
travel = {'台北' : {
               0 : '淡水',
               1 : '九份'
               },
          '桃園' : {
               0 : '大溪',
               1 : '莊敬'
               }
        }
for place, spot in travel.items():
    print('地點=', place)
    print(spot[0])
    print(spot[1])
'''
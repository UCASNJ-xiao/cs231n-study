import numpy as np
import matplotlib.pyplot as plt

train_data = np.array([[1,2],[4,2],[3,8],[9,3],[3,3],[6,3],[7,5],[1,9]])
#8个训练点坐标
train_class = ["cat","dog","bird","dog","cat","cat","bird","dog"]
#8个训练点类别
train_point = np.array([2,3])
#训练测试点坐标

distance = []
#创建一个空列表
for point in train_data:
    d = np.sqrt(np.sum((train_point - point) ** 2))
    #欧式距离公式
    distance.append(d)
    #将8个距离值放入空列表

k = 1
#knn算法中k=1的情况

distance_idx = distance.index(min(distance))
#在distance列表中找到最小值的索引，赋值distance_idx
print(f"k=1时最近的类别为{train_class[distance_idx]}")
#最小值的索引也是train_class的索引，利用索引取出类别



k = 5
#knn算法中k=5的情况

distance_sorted = sorted(distance)
#给列表排序，排序后的列表叫distance_sorted

# distance0 = distance.index(distance_sorted[0])
# distance1 = distance.index(distance_sorted[1])
# distance2 = distance.index(distance_sorted[2])
# distance3 = distance.index(distance_sorted[3])
# distance4 = distance.index(distance_sorted[4])
#以上是不用for循环

c1 = 0
c2 = 0
c3 = 0
#初始化

for num in range(k):
    distance_num = distance.index(distance_sorted[num])
#将排序后的前5个距离值在distance列表中找到对应索引值，赋值distance_num
    print(f"k=5时最近的类别分别为{train_class[distance_num]}")
#将对应的索引值放到训练点的类别中，输出相应的类别
    if train_class[distance_num] == "cat":
        c1 += 1
    elif train_class[distance_num] == "dog":
        c2 += 1
    else:
        c3 += 1
#如果是cat，c1加1，dog是c2加1，其他情况（bird）是c3加1

class_num = [c1,c2,c3]
#将类别出现的次数组成列表，命名为class_num

class_k5 = class_num.index(max(class_num))
#取出列表中最大值的索引，赋值class_k5

class_type = ["cat","dog","bird"]
#按照cat,dog,bird的顺序组成列表，命名class_type

print(f"k=5经knn算法后的类别为{class_type[class_k5]}")
#在class_type列表中找到class_k5所对应的类别，输出

#下面是画图描点的程序
marker = ["o",'D','v']
#描点的形状
coral = ["red","orange","blue"]
#描点的颜色
n = 0
#初始化
class_index = {'cat': 0,'dog': 1,'bird':2}
#创建一个字典，（key，value)
for draw_point in train_data:

    key = train_class[n]
    #将train_class中的类别依次取出，赋值key
    x = draw_point[0]
    #x=依次取出点的横坐标
    y = draw_point[1]
    #y=依次取出点的纵坐标

    plt.plot(x, y, marker= marker[class_index[key]], color=coral[class_index[key]],linewidth=0.1,markersize=13)
    #在字典中找到key所对应的value，再到marker中找到value对应的描点的形状和颜色
    n += 1
    #依次取出所描点的类别

plt.plot(train_point[0],train_point[1],marker= "+", color="black",linewidth=0.1,markersize=13)
#将训练测试点坐标描出来
plt.show()
#画图







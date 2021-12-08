import random
def w_rate(w:int)->float:
    return 0.88,0.25
def getE(rate:tuple)->float:
    return rate[0]-0.5*rate[1]
def get_nextwr(win_size:int,nums):
    nextW=[]
    nextR=[]
    for i in range(nums):
        w=random.randint(win_size-10,win_size+10)
        nextW.append(w)
        nextR.append(w_rate(i))
    return nextW,nextR
def get_pBest(list_rate:list,list_w:list):
    temp_max=-99
    max_index=-1
    for i in range(10):
        temp_e=getE(list_rate[i])
        if temp_e>temp_max:
            temp_max=temp_e
            max_index=i
    return list_w[max_index]
if __name__=="__main__":
    # todo 初始化窗口
    # list_winsize=[random.randint(10,50) for i in range(10)]
    list_winsize=[10, 15, 24, 49, 25, 49, 50, 40, 27, 44]
    # list_rate=[(round(random.random(),3),round(random.random(),3)) for _ in range(10)]
    list_rate=[(0.375, 0.736), (0.41, 0.212), (0.047, 0.998), (0.133, 0.094), (0.244, 0.34), (0.885, 0.762), (0.85, 0.902), (0.653, 0.813), (0.304, 0.511), (0.313, 0.22)]
    print("——————————————————————————————————————————————————")
    print("大小",list_winsize)
    temp=0
    for i in range(10):
        gbest=get_pBest(list_rate=list_rate,list_w=list_winsize)
        print("gbest",gbest)
        if temp==gbest:
            break
        temp=gbest
        list_winsize,list_rate=get_nextwr(gbest,10)
        print("大小",list_winsize)
        print("——————————————————————————————————————————————————")
    print(gbest)
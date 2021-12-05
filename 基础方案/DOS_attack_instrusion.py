import csv
import math
import random
# 数据处理部分
Ta_packet = 1000  # 攻击块总数
Tn_packet = 55838  # 正常块总数

def function_E(Ra,Rn,Rt)->float:
    """
    能量函数
    """
    C1 = 1
    C2 = 0.5
    C3 = 1
    return Ra * C1 - Rn * C2 - Rt * C3

def cal_entro(dos_data:list,window_size:int,k:int,div:int,label:list):
    """
    input:
        dosdata：数据 
        window_size:窗口大小
        K,div:用于判断信息熵的范围
    output:
        Ra:检测率
        Rn:误报率
    """
    dos_data_dic={}
    H_i=0
    # 计算范围区间
    range_0,range_1=3.0-k*div,3.0+k*div
    true_count,false_count=0,0
    Da,Dn=0,0 # 攻击块数量，正常块数目
    Ra,Rn=0,0
    Rt=0
    Ta,Tn=Ta_packet/window_size,Tn_packet/window_size
    # 一个window_size的信息熵
    w_count=0
    for size in range(0,len(dos_data)//window_size,1):
        w_count+=1
        for i in range(size*window_size,(size+1)*window_size):
            if label[i]=='BENIGN':
                true_count+=1
            else:
                false_count+=1
            dos_data_dic[dos_data[i]]=dos_data_dic.get(dos_data[i],0)+1
        print(dos_data_dic)
        for num in dos_data_dic.values():
            P_i=float(num/window_size)
            H_i+=P_i*math.log((1/P_i),2)
            H_ws=H_i
        
        # 判断一个窗口滑动窗口的信息熵的范围
        if H_ws<range_0 or H_ws>range_1:
        # 处于入侵检测
        # 统计true or false
            if true_count>false_count:
                Da+=1
                Ra=float(Da/Ta)*100
                # print('检测率=',Ra)
            else:
                Dn+=1
                Rn=float(Dn/Tn)*100
                # print('误报率=',Rn)
        H_i=0
        dos_data_dic={}

        print(f'第{w_count}窗口的信息熵是{H_ws}')
    print('检测率',Ra,end=' ')
    print('误报率',Rn)

    return Ra,Rn,Rt  

def simulatedAnnealing(dos_data,label,T,cool):
    k_best=1.0
    div_best=random.random()
    W_best = random.randint(5, 70)
    Ra,Rn,Rt=cal_entro(dos_data,W_best,k_best,div_best,label)
    e_best = function_E(Ra, Rn, Rt)
    e_prev = function_E(Ra, Rn, Rt) - 1
    while T > 0.0001 and e_prev < e_best:
    # row 7 in paper
        div_next = random.random()
        W_next = random.randint(W_best - 10, W_best + 10)
        Ra,Rn,Rt=cal_entro(dos_data,W_best,k_best,div_best,label)
        e_next = function_E(Ra, Rn, Rt)
        p = pow(math.e, -abs(e_next - e_prev) / float(T))
        if random.random() < p:
            div_prev = div_next
            W_prev = W_next
            e_prev = e_next
            if e_prev > e_best:
                div_best = div_prev
                W_best = W_prev
                e_best = e_prev

        # cool down
        T = T * cool

    return div_best, W_best

if __name__=='__main__':
    source_ip=[]
    lable_list=[]
    with open('data11_26.csv','r',encoding='utf-8') as file:
        read_csv=csv.reader(file)
        for row in read_csv:
            # 读取源地址ip和目的地址ip,以及标签
            source_ip.append(row[1])
            # source_port.append(row[1])
            # destina_ip.append(row[2])
            # destina_port.append(row[3])
            # time_stamp.append(row[5])
            lable_list.append(row[-1])
    # 模拟退火
    print(len(source_ip))
    # a,n,t=cal_entro(source_ip,50,1.0,0.2,lable_list)
    # print(a,n,t)
    div,window_size=simulatedAnnealing(dos_data=source_ip,label=lable_list,T=1000,cool=0.99)
    print(f'div={div},windows={window_size}')
    

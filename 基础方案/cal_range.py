import csv

if __name__=="__main__": 
    source_ip=[]
    label_list=[]
    with open('data11_26.csv','r',encoding='utf-8') as file:
        read_csv=csv.reader(file)
        for row in read_csv:
            # 读取源地址ip和目的地址ip,以及标签
            source_ip.append(row[1])
            # source_port.append(row[1])
            # destina_ip.append(row[2])
            # destina_port.append(row[3])
            # time_stamp.append(row[5])
            label_list.append(row[-1])
    # 模拟退火
    print(len(source_ip))
    # a,n,t=cal_entro(source_ip,50,1.0,0.2,lable_list)
    # print(a,n,t)
    div,window_size=simulatedAnnealing(dos_data=source_ip,label=lable_list,T=1000,cool=0.99)
    print(f'div={div},windows={window_size}')
    
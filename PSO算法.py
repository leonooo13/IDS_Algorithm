import random
# windows->ra,rn ->能量函数
class PSO:
    # 定义粒子个数,随机定义粒子位置
    def __init__(self,n) -> None:
        self.num=n
        self.grain_place=[(round(random.random(),3),round(random.random(),3)) for _ in range(n)]        
        self.grain_speed=[(round(random.random(),3),round(random.random(),3)) for _ in range(n)] 
        self.p_best=self.grain_place
        self.g_best=(0,0)
        temp_max=-999
        for i in self.grain_place:
            energy=self.engfunc(i)
            if energy>temp_max:
                temp_max=energy
                self.g_best=i
        # print(self.p_best)
        # print(self.g_best)
    # 目标方程
    def engfunc(self,x:tuple):
        return x[0]-0.5*x[1]
    # 更新粒子的位置和速度
    def update(self,v:list,x:list,p_best:list,g_best:tuple)->tuple[list,list]:
        w=0.5#权重系数
        c1,c2=2.0,2.0 #加速系数
        # r1,r2[0,1]随机数
        r1=round(random.random(),2)
        r2=round(random.random(),2)
        x_update=[]
        v_update=[]
        for i in range(self.num):
            v1_update=w*v[i][0]+c1*r1*(p_best[i][0]-x[i][0])+c2*r2*(g_best[0]-x[i][0])
            v2_update=w*v[i][1]+c1*r1*(p_best[i][1]-x[i][1])+c2*r2*(g_best[1]-x[i][1])
            v_update.append((round(v1_update,3),round(v2_update,3)))
            # print(v1_update)
            x1_update=x[i][0]+v1_update
            x2_update=x[i][1]+v2_update
            if x1_update>1 or x2_update>1:
                x1_update=1
                x2_update=1
            elif x1_update<0 or x2_update<0:
                x1_update=0
                x2_update=0
            x_update.append((round(x1_update,3),round(x2_update,3)))
        return x_update,v_update
    def get_best(self,x_new:list,x_old:list):
        p_best=[]
        g_best=()
        temp_max=-999
        # print('xnew',x_new)
        # print(x_old)
        for i in range(self.num):
            if self.engfunc(x_new[i])<self.engfunc(x_old[i]):
                p_best.append(x_new[i])
            else:
                p_best.append(x_old[i])
            # print("pbest的最后",p_best[-1])
            if self.engfunc(p_best[i])>temp_max:
                temp_max=self.engfunc(p_best[i])
                g_best=p_best[i]
        return g_best,p_best

            

if __name__=='__main__':
    # 初始化窗口
    win_best=random.randint(5,70)
    # win_best=50
    # 初始化粒子个数
    val_pso=PSO(10)
    #初始化粒子位置和速度
    v_new=val_pso.grain_speed
    x_new=val_pso.grain_place
    print("粒子开始速度",v_new)
    print("粒子开始位置",x_new)
    p_best=val_pso.p_best# 局部最优
    g_best=val_pso.g_best# 全局最优
    print("开始的局部最优",p_best)
    print("开始的全局最优",g_best)
    print("————————————————————————————————————————————————————————")
    # 迭代循环
    before_gbest=g_best
    x_old=x_new
    count=0
    while 1:
        win_next = random.randint(win_best - 10, win_best + 10)
        x_new,v_new=val_pso.update(v_new,x_new,p_best,g_best)
        print("X:",x_new)
        print("V:",v_new)
        g_best,p_best=val_pso.get_best(x_new=x_new,x_old=x_old)
        print("g_best",g_best)
        print("p_best",p_best)
        x_old=x_new
        count+=1
        if val_pso.engfunc(g_best)>val_pso.engfunc(before_gbest):
            win_best=win_next
        if g_best==before_gbest:
            break
        before_gbest=g_best
        # g_best_list.append(g_best)
        print(count,"————————————————————————————————————————————————————————")
    print(win_best)
    print(g_best)
    print(p_best)
    # print(g_best_list)
    # val_ener=val_pso.engfunc(g_best)
    # print(val_ener)

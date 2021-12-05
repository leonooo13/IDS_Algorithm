import random
class PSO:
    # 定义粒子个数,随机定义粒子位置
    def __init__(self,n) -> None:
        self.num=n
        self.grain_place=[(round(random.random(),3),round(random.random(),3)) for _ in range(n)]        
        self.grain_speed=[(round(random.random(),3),round(random.random(),3)) for _ in range(n)] 
        self.p_best=self.grain_place
        self.g_best=(0,0)
        temp_max=0
        for i in self.grain_place:
            energy=self.engfunc(i)
            if energy>temp_max:
                temp_max=energy
                self.g_best=i
        # print(self.p_best)
        # print(self.g_best)
    def engfunc(self,x:tuple):
        return x[0]-0.5*x[1]
    def update(self,v:list,x:list,p_best:list,g_best:tuple)->tuple[list,list]:
        w=0.5#权重系数
        c1,c2=2.0,2.0 #加速系数
        # r1,r2[0,1]随机数
        r1=round(random.random(),2)
        r2=round(random.random(),2)
        x_update=[]
        v_update=[]
        for i in range(self.num):
            # print('v',v[i])
            # print(p_best[i])
            # print(g_best)
            # print('v',v[i][0])
            v1_update=w*v[i][0]+c1*r1*(p_best[i][0]-x[i][0])+c2*r2*(g_best[0]-x[i][0])
            v2_update=w*v[i][1]+c1*r1*(p_best[i][1]-x[i][1])+c2*r2*(g_best[1]-x[i][1])
            v_update.append((v1_update,v2_update))
            # print(v1_update)
            x1_update=x[i][0]+v1_update
            x2_update=x[i][1]+v2_update
            x_update.append((round(x1_update,3),round(x2_update,3)))
        # print('x_update',x_update)
        return x_update,v_update
    def get_best(self,x_new:list,x_old:list):
        p_best=[]
        temp_max=0
        # print('xnew',x_new)
        # print(x_old)
        for i in range(self.num):
            if self.engfunc(x_new[i])<self.engfunc(x_old[i]):
                p_best.append(x_new[i])
            else:
                p_best.append(x_old[i])
            if self.engfunc(p_best[-1])>temp_max:
                temp_max=self.engfunc(p_best[-1])
                g_best=p_best[-1]
        return g_best,p_best
            

if __name__=='__main__':
    val_pso=PSO(10)
    v=val_pso.grain_speed
    x_old=val_pso.grain_place
    p_best=val_pso.p_best
    g_best=val_pso.g_best
    # 开始遍历
    for i in range(2):
        x_new,v=val_pso.update(v,x_old,p_best,g_best)
        g_best,p_best=val_pso.get_best(x_new=x_new,x_old=x_old)
        x_old=x_new
    print(g_best)
    # print(p_best)

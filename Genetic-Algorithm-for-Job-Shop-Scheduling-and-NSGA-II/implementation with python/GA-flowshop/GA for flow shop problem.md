# Solving flow shop scheduling problem with genetic algorithm

*POLab* <br>
*[cheng-man wu](https://www.linkedin.com/in/chengmanwu)*<br>
*2018/07/14*
<br>

## :black_nib: Foreword <br>

Here to explain how to use GA to solve the flow shop problem, the following will first introduce the flow shop problem, then describe the solution problem and coding principle description of this example, and finally explain the concept according to each program block.

### :arrow_down_small: What is a flow shop problem? <br>

To put it simply, the flow shop problem is that there are n workpieces and m machines. The order of processing of each workpiece on the machine is the same. As shown in the figure below, the workpiece 1 first enters the machine 1 and then the machine 2 And the workpiece 2 follows the step of the workpiece 1, and is processed in the same machine sequence, and the other workpieces are deduced by analogy.

<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/1 .png" width="450" ​​height="180">
</div>
<br>

Therefore, it is assumed that there are 3 workpieces and 2 machines, and the processing time of each workpiece in each machine is as shown in the lower left figure. The processing order of the workpiece is first to machine A and then to machine B, assuming that The result of the schedule is <br>
Job 1->Job 2->Job 3, so you can get the Gantt chart as shown in the lower right figure.

<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/2 .png" width="570" height="250">
</div>
<br>

## :black_nib: Description of the problem <br>
This example is a single-machine flow shop problem with 20 workpieces. The scheduling goal is **Total weighted tardiness**. The workpiece information is shown below.

<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/3 .png" width="650" height="180">
</div>
<br>

### :arrow_down_small: Schedule Targets <br>
Since the goal of this example is to minimize total weighted tardiness, in addition to having to know the processing time of each workpiece on each machine, the due date and weight of each workpiece must be known. <br>

:bulb: The formula for the total weighted delay time is as follows:<br>

<c<sub>i</sup></sub>: Completion time of the workpiece i, d<sub>i</sup></sub>: the due date of the workpiece i (Due date), T<sub>i</sup></sub>: Tardiness time of workpiece i, <br>
w<sub>i</sup></sub>: Weight of artifact i >
- Calculate the delay time of each workpiece first. If it is done early, the delay time is 0 <br>

**T<sub>i</sup></sub> = max {0,c<sub>i</sup></sub> - d<sub>i</sup></sub>}**

- Calculate the sum of the weighted delay times of all the workpieces. From the formula we can know that when the weight of the workpiece is larger, we should complete those workpieces with larger weights as soon as possible, otherwise the total weighted delay time will be too large. In terms of scheduling goals, this is not a good schedule.

<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/4 .png" width="80" height="60">

In addition, there is another version of the flow shop program. The main difference with this article is the difference in the solution target. The other version aims to minimize the total idle time (Idle time), which is the example Gantt chart above. The part of the gray area, which is expected to be discharged, can minimize the idle time of the main machine.

### :arrow_down_small: Coding Principles <br>

The coding method here is very simple. Each chromosome represents a set of scheduling results. Therefore, if there are five workpieces in the flow shop problem, each chromosome is composed of five genes, each gene is Representing an artifact, in the program, each chromosome is stored via a list, as shown below:<br>

Chromosome 1 => [0,1,2,3,4] <br>
Chromosome 2 => [1,2,0,3,4] <br>
Chromosome 2 => [4,2,0,1,3] <br>
........<br>

## :black_nib: Program Description <br>

This is mainly for the important blocks in the program. Some details are not included. Please refer to [Complete Code] if necessary (https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop -Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/GA_flowshop_tardyjob.py) or [sample file] ((https://wurmen.github.io/Genetic-Algorithm-for- Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/GA-flowshop/Example.html))

### :arrow_down_small: Import the required kits <br>

```python
# importing required modules
Import numpy as np
Import time
Import copy
```

### :arrow_down_small: Initial Settings <br>
This area mainly contains reading files or data settings, as well as some parameter settings.
```python
''' ================= initialization setting =========================
Num_job=20 # number of jobs

p = [10, 10, 13, 4, 9, 4, 8, 15, 7, 1, 9, 3, 15, 9, 11, 6, 5, 14, 18, 3]
d=[50,38,49,12,20,105,73,45,6,64,15,6,92,43,78,21,15,50,150,99]
w=[10,5,1,5,10,1,5,10,5,1,5,10,10,5,1,10,5,5,1,5]
# raw_input is used in python 2
Population_size=int(input('Please input the size of population: ') or 30) # default value is 30
Crossover_rate=float(input('Please input the size of Crossover Rate: ') or 0.8) # default value is 0.8
Mutation_rate=float(input('Please input the size of Mutation Rate: ') or 0.1) # default value is 0.1
Mutation_selection_rate=float(input('Please input the mutation selection rate: ') or 0.5)
Num_mutation_jobs=round(num_job*mutation_selection_rate)
Num_iteration=int(input('Please input number of iteration: ') or 2000) # default value is 2000


Start_time = time.time()

```

### :arrow_down_small: Generate initial solution <br>
According to the size of the above-mentioned group, the initial group is generated in a random manner.
```python
'''----- generate initial population -----'''
Tbest=999999999999999
Best_list, best_obj=[],[]
Population_list=[]
For i in range(population_size):
    Random_num=list(np.random.permutation(num_job)) # generate a random permutation of 0 to num_job-1
    Population_list.append(nxm_random_num) # add to the population_list2.
```

### :arrow_down_small: 交配 <br>

這裡的交配方式是透過指定位置的方式進行交配，執行的步驟如下：
1. 透過隨機選擇方式，將基因數一半的位置設為固定不變，以下圖為例，共有六個工件進行排序，生成兩個親代，在此選定2、5、6為工件順序不變的位置。
2. 將 Parent 1 工件不變的位置，複製產生 Child 2 ，接著 Child 2 與 Parent 2 進行比對。
3. 將 parent 2 與child2不重複的工件，依序填入 Child 2 剩餘的位置，形成新的子代。 Child 1 的形成方式如 Child 2 所示。
<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/5.png" width="400" height="325">
</div>
<br>

```python
    '''-------- crossover --------'''
	parent_list=copy.deepcopy(population_list)
    offspring_list=copy.deepcopy(population_list)
    S=list(np.random.permutation(population_size)) # generate a random sequence to select the parent chromosome to crossover
    
    for m in range(int(population_size/2)):
        crossover_prob=np.random.rand()
        if crossover_rate>=crossover_prob:
            parent_1= population_list[S[2*m]][:]
            parent_2= population_list[S[2*m+1]][:]
            child_1=['na' for i in range(num_job)]
            child_2=['na' for i in range(num_job)]
            fix_num=round(num_job/2)
            g_fix=list(np.random.choice(num_job, fix_num, replace=False))
            
            for g in range(fix_num):
                child_1[g_fix[g]]=parent_2[g_fix[g]]
                child_2[g_fix[g]]=parent_1[g_fix[g]]
            c1=[parent_1[i] for i in range(num_job) if parent_1[i] not in child_1]
            c2=[parent_2[i] for i in range(num_job) if parent_2[i] not in child_2]
            
            for i in range(num_job-fix_num):
                child_1[child_1.index('na')]=c1[i]
                child_2[child_2.index('na')]=c2[i]
            offspring_list[S[2*m]]=child_1[:]
            offspring_list[S[2*m+1]]=child_2[:]
```
### :arrow_down_small: 突變 <br>
此方法是透過基因位移的方式進行突變，突變方式如下:<br>
1. 依據 mutation selection rate 決定染色體中有多少百分比的基因要進行突變，假設每條染色體有六個基因， mutation selection rate 為0.5，則有3個基因要進行突變。
2. 隨機選定要位移的基因，假設選定5、2、6 (在此表示該位置下的基因要進行突變)
3. 進行基因移轉，移轉方式如圖所示。
<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/6.png" width="450" height="250">
</div>
<br>

```python
'''--------mutatuon--------'''   
    for m in range(len(offspring_list)):
        mutation_prob=np.random.rand()
        if mutation_rate >= mutation_prob:
            m_chg=list(np.random.choice(num_job, num_mutation_jobs, replace=False)) # chooses the position to mutation
            t_value_last=offspring_list[m][m_chg[0]] # save the value which is on the first mutation position
            for i in range(num_mutation_jobs-1):
                offspring_list[m][m_chg[i]]=offspring_list[m][m_chg[i+1]] # displacement
            
            offspring_list[m][m_chg[num_mutation_jobs-1]]=t_value_last # move the value of the first mutation position to the last mutation position
```
### :arrow_down_small: 適應值計算 <br>
計算每個染色體也就是每個排程結果的總加權延遲，並將其記錄，以利後續選擇時能比較
```python
    '''--------fitness value(calculate tardiness)-------------'''
    total_chromosome=copy.deepcopy(parent_list)+copy.deepcopy(offspring_list) # parent and offspring chromosomes combination
    chrom_fitness,chrom_fit=[],[]
    total_fitness=0
    for i in range(population_size*2):
        ptime=0
        tardiness=0
        for j in range(num_job):
            ptime=ptime+p[total_chromosome[i][j]]
            tardiness=tardiness+w[total_chromosome[i][j]]*max(ptime-d[total_chromosome[i][j]],0)
        chrom_fitness.append(1/tardiness)
        chrom_fit.append(tardiness)
        total_fitness=total_fitness+chrom_fitness[i]
```

### :arrow_down_small: 選擇  <br>
這裡採用輪盤法 (Roulette wheel) 的選擇機制
```python
    '''----------selection----------'''
    pk,qk=[],[]
    
    for i in range(population_size*2):
        pk.append(chrom_fitness[i]/total_fitness)
    for i in range(population_size*2):
        cumulative=0
        for j in range(0,i+1):
            cumulative=cumulative+pk[j]
        qk.append(cumulative)
    
    selection_rand=[np.random.rand() for i in range(population_size)]
    
    for i in range(population_size):
        if selection_rand[i]<=qk[0]:
			population_list[i]=copy.deepcopy(total_chromosome[0])
        else:
            for j in range(0,population_size*2-1):
                if selection_rand[i]>qk[j] and selection_rand[i]<=qk[j+1]:
					population_list[i]=copy.deepcopy(total_chromosome[j+1]) 
                    break
```

### :arrow_down_small: 比較 <br>
先比較每個染色體的總加權延遲 (chrom_fit) ，選出此輪找到的最好解 (Tbest_now) ，接著在跟目前為止找到的最好解 (Tbest) 進行比較，一旦這一輪的解比目前為止找到的解還要好，就替代 Tbest 並記錄該解所得到的排程結果
```python
    '''----------comparison----------'''
    for i in range(population_size*2):
        if chrom_fit[i]<Tbest_now:
            Tbest_now=chrom_fit[i]
			sequence_now=copy.deepcopy(total_chromosome[i])
    
    if Tbest_now<=Tbest:
        Tbest=Tbest_now
		sequence_best=copy.deepcopy(sequence_now)
    
    job_sequence_ptime=0
    num_tardy=0
    for k in range(num_job):
        job_sequence_ptime=job_sequence_ptime+p[sequence_best[k]]
        if job_sequence_ptime>d[sequence_best[k]]:
            num_tardy=num_tardy+1
```
### :arrow_down_small: Mutant <br>
This method is to mutate by means of gene displacement, and the mutation method is as follows:<br>
1. According to the mutation selection rate, determine how many genes in the chromosome are to be mutated. If there are six genes per chromosome and the mutation selection rate is 0.5, then 3 genes will be mutated.
2. Randomly select the gene to be displaced, assuming 5, 2, 6 are selected (here, the gene at this position is to be mutated)
3. Perform gene transfer and transfer as shown.
<br>
<div align=center>
<img src="https://github.com/wurmen/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/6 .png" width="450" ​​height="250">
</div>
<br>

```python
'''--------mutatuon--------'''
    For m in range(len(offspring_list)):
        Mutation_prob=np.random.rand()
        If mutation_rate >= mutation_prob:
            M_chg=list(np.random.choice(num_job, num_mutation_jobs, replace=False)) # chooses the position to mutation
            T_value_last=offspring_list[m][m_chg[0]] # save the value which is on the first mutation position
            For i in range(num_mutation_jobs-1):
                Offspring_list[m][m_chg[i]]=offspring_list[m][m_chg[i+1]] # displacement
            
            Offspring_list[m][m_chg[num_mutation_jobs-1]]=t_value_last # move the value of the first mutation position to the last mutation position
```
### :arrow_down_small: Adaptive Value Calculation <br>
Calculate the total weighted delay for each chromosome, which is the result of each schedule, and record it for comparison in subsequent selections.
```python
    '''--------fitness value(calculate tardiness)-------------'''
    Total_chromosome=copy.deepcopy(parent_list)+copy.deepcopy(offspring_list) # parent and offspring chromosomes combination
    Chrom_fitness,chrom_fit=[],[]
    Total_fitness=0
    For i in range(population_size*2):
        Ptime=0
        Tardiness=0
        For j in range(num_job):
            Ptime=ptime+p[total_chromosome[i][j]]
            Tardiness=tardiness+w[total_chromosome[i][j]]*max(ptime-d[total_chromosome[i][j]],0)
        Chrom_fitness.append(1/tardiness)
        Chrom_fit.append(tardiness)
        Total_fitness=total_fitness+chrom_fitness[i]
```

### :arrow_down_small: Select <br>
Here, the Roulette wheel selection mechanism is adopted.
```python
    '''----------selection----------'''
    Pk,qk=[],[]
    
    For i in range(population_size*2):
        Pk.append(chrom_fitness[i]/total_fitness)
    For i in range(population_size*2):
        Cumulative=0
        For j in range(0,i+1):
            Cumulative=cumulative+pk[j]
        Qk.append(cumulative)
    
    Selection_rand=[np.random.rand() for i in range(population_size)]
    
    For i in range(population_size):
        If selection_rand[i]<=qk[0]:
Population_list[i]=copy.deepcopy(total_chromosome[0])
        Else:
            For j in range(0,population_size*2-1):
                If selection_rand[i]>qk[j] and selection_rand[i]<=qk[j+1]:
Population_list[i]=copy.deepcopy(total_chromosome[j+1])
                    Break
```

### :arrow_down_small: Compare <br>
First compare the total weighted delay (chrom_fit) of each chromosome, select the best solution found in this round (Tbest_now), and then compare it with the best solution (Tbest) found so far, once the solution of this round is found so far The solution is better, replace Tbest and record the result of the solution.
```python
    '''----------comparison----------'''
    For i in range(population_size*2):
        If chrom_fit[i]<Tbest_now:
            Tbest_now=chrom_fit[i]
Sequence_now=copy.deepcopy(total_chromosome[i])
    
    If Tbest_now<=Tbest:
        Tbest=Tbest_now
Sequence_best=copy.deepcopy(sequence_now)
    
    Job_sequence_ptime=0
    Num_tardy=0
    For k in range(num_job):
        Job_sequence_ptime=job_sequence_ptime+p[sequence_best[k]]
        If job_sequence_ptime>d[sequence_best[k]]:
            Num_tardy=num_tardy+1
```
### :arrow_down_small: Results <br>
After the end of all iterations, the best schedule result (sequence_best) found in all iterations, its total weighted delay time, average weighted delay time per workpiece, how many workpiece delays, and program execution time are output.
```python
'''----------result----------'''
Print("optimal sequence",sequence_best)
Print("optimal value:%f"%Tbest)
Print("average tardiness:%f"%(Tbest/num_job))
Print("number of tardy:%d"%num_tardy)
Print('the elapsed time:%s'% (time.time() - start_time))
```

### :arrow_down_small: Gantt Chart <br>
```python
'''--------plot gantt chart-------'''
import pandas as pd
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.offline as offline
import datetime

j_keys=[j for j in range(num_job)]
j_count={key:0 for key in j_keys}
m_count=0
j_record={}
for i in sequence_best:
   gen_t=int(p[i])
   j_count[i]=j_count[i]+gen_t
   m_count=m_count+gen_t
   
   if m_count<j_count[i]:
       m_count=j_count[i]
   elif m_count>j_count[i]:
       j_count[i]=m_count
   start_time=str(datetime.timedelta(seconds=j_count[i]-p[i])) # convert seconds to hours, minutes and seconds

   end_time=str(datetime.timedelta(seconds=j_count[i]))
   j_record[i]=[start_time,end_time]
       

df=[]
for j in j_keys:
   df.append(dict(Task='Machine', Start='2018-07-14 %s'%(str(j_record[j][0])), Finish='2018-07-14 %s'%(str(j_record[j][1])),Resource='Job %s'%(j+1)))

# colors={}
# for i in j_keys:
#     colors['Job %s'%(i+1)]='rgb(%s,%s,%s)'%(255/(i+1)+0*i,5+12*i,50+10*i)

fig = ff.create_gantt(df, colors=['#008B00','#FF8C00','#E3CF57','#0000CD','#7AC5CD','#ED9121','#76EE00','#6495ED','#008B8B','#A9A9A9','#A2CD5A','#9A32CD','#8FBC8F','#EEC900','#EEE685','#CDC1C5','#9AC0CD','#EEA2AD','#00FA9A','#CDB38B'], index_col='Resource', show_colorbar=True, group_tasks=True, showgrid_x=True)
py.iplot(fig, filename='GA_flow_shop_scheduling_tardyjob', world_readable=True)
```
## :black_nib: Reference <br>
- António Ferrolho and Manuel Crisóstomo. “Single Machine Total Weighted Tardiness Problem with Genetic Algorithms” 
- N. Liu, Mohamed A. Abdelrahman, and Snni Ramaswamy. “A Genetic Algorithm for the Single Machine Total Weighted Tardiness Problem”

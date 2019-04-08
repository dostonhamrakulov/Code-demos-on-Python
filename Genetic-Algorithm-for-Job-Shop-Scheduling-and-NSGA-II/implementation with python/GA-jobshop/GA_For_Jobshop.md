# Solving Job shop scheduling problem with genetic algorithm

*2018/12/01*
<br>

## :black_nib: Foreword <br>

Here to explain how to use GA to solve the Job shop problem, the following will first introduce the Job shop problem, then describe the solution problem and coding and decoding instructions of this example, and finally conceptually according to each program block. explain

### :arrow_down_small: What is a Job shop problem? <br>

The biggest difference between the Jop shop problem and the Flow shop problem is that, unlike the Flow shop problem, the order of processing each workpiece on the machine is the same. In the Job shop problem, each workpiece has its own machine processing. The order is as shown below:<br>
This is a 3x3 Job shop problem
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/1.png" width="650" height="250">
</div>
<br>

## :black_nib: Description of the problem <br>
This example is a 10x10 Job shop problem with 10 workpieces and 10 machines. Each workpiece has a different processing order on each machine. The scheduling goal is to minimize the total completion time (Makespan). The machining sequence of the workpiece is presented in sequence, and each workpiece passes through 10 machining operations. The following table records the processing machine for each workpiece in each machining operation and the processing time required <br>

- Processing time
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/2.png" width="650" height="300">
</div>
<br>
<br>

- Machine sequence
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/3.png" width="650" height="300">
</div>
<br>

### :arrow_down_small: Schedule Targets <br>
The goal of this example is to minimize the total completion time (Makespan), that is, to minimize the execution time of the entire schedule. Take the previous example as an example. The completion time of this example is the completion time of Job 3 at machine 1. Because Job 3 is the last one of all artifacts for this schedule result, so the completion time of this schedule is the point in time when Job 3 is completed.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/4.png" width="450" ​​height="180">
</div>
<br>

### :arrow_down_small: Encoding and Decoding <br>
Here, the chromosomal coding method of the Job shop scheduling problem proposed by [Gen-Tsujimura-Kubota's Method (1994, 1997)] (https://ieeexplore.ieee.org/document/400072/) is mainly referred to. <br>

The concept of this method is to represent the chromosome as the processing sequence of a set of workpieces. One gene represents the processing of a workpiece. According to the number of times the workpiece appears on the chromosome, the current processing of each workpiece is known, and then the processing of each workpiece is processed. The machine and processing time are used to schedule. <br>

Suppose now that there is a job shop scheduling problem with N workpieces M machines, that one chromosome will be composed of N x M genes, because each workpiece will only be processed once per machine. It is processed by the M machine, so each workpiece will appear M times in the chromosome. Here is an example of the 3 x 3 Job shop problem.<br>

O<sub>ijk</sup></sub> means the workpiece i uses the kth machine in the job program j

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/5.png" width="780" height="420">
</div>
<br>

## :black_nib: Program Description <br>

This is mainly for the important blocks in the program. Some details are not included. Please refer to [Complete Code] if necessary (https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop -Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-jobshop/GA_jobshop_makespan.py) or [sample file] (https://wurmen.github.io/Genetic-Algorithm-for-Job -Shop-Scheduling-and-NSGA-II/implementation%20with%20python/GA-jobshop/Example1.html)

### :arrow_down_small: Import the required kits <br>

```python
'''==========Solving job shop scheduling problem by gentic algorithm in python======='''
# importing required modules
Import pandas as pd
Import numpy as np
Import time
```

### :arrow_down_small: Initial Settings <br>
This area mainly contains reading files or data settings, as well as some parameter settings.
```python
''' ================= initialization setting =========================


Pt_tmp=pd.read_excel("JSP_dataset.xlsx",sheet_name="Processing Time",index_col =[0])
Ms_tmp=pd.read_excel("JSP_dataset.xlsx",sheet_name="Machines Sequence",index_col =[0])

Dfshape=pt_tmp.shape
Num_mc=dfshape[1] # number of machines
Num_job=dfshape[0] # number of jobs
Num_gene=num_mc*num_job # number of genes in a chromosome

Pt=[list(map(int, pt_tmp.iloc[i])) for i in range(num_job)]
Ms=[list(map(int,ms_tmp.iloc[i])) for i in range(num_job)]




# raw_input is used in python 2
Population_size=int(input('Please input the size of population: ') or 30) # default value is 30
Crossover_rate=float(input('Please input the size of Crossover Rate: ') or 0.8) # default value is 0.8
Mutation_rate=float(input('Please input the size of Mutation Rate: ') or 0.2) # default value is 0.2
Mutation_selection_rate=float(input('Please input the mutation selection rate: ') or 0.2)
Num_mutation_jobs=round(num_gene*mutation_selection_rate)
Num_iteration=int(input('Please input number of iteration: ') or 2000) # default value is 2000
    
Start_time = time.time()

```

### :arrow_down_small: Generate initial solution <br>
According to the above-mentioned population size, the initial population is generated in a random manner, and each chromosome has 10 x 10 = 100 genes.
```python
'''----- generate initial population -----'''
Tbest=999999999999999
Best_list, best_obj=[],[]
Population_list=[]
For i in range(population_size):
    Nxm_random_num=list(np.random.permutation(num_gene)) # generate a random permutation of 0 to num_job*num_mc-1
    Population_list.append(nxm_random_num) # add to the population_list
    For j in range(num_gene):
        Population_list[i][j]=population_list[i][j]%num_job # convert to job number format, every job appears m times

```

### :arrow_down_small: Mating <br>

At first, a set of random sequences for selecting the parental chromosomes will be generated first, and then two or two will be taken out from the sequence, and the mating rate will be used to determine whether or not to mate. If necessary, the two-point mating method is used to generate Two offspring and replace the original mother chromosome

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/6.png" width="450" height="300">
</div>
<br>

```python
    '''-------- two point crossover --------'''
	parent_list=copy.deepcopy(population_list) # preserve the original parent chromosomes
    offspring_list=copy.deepcopy(population_list)
    S=list(np.random.permutation(population_size)) # generate a random sequence to select the parent chromosome to crossover

    for m in range(int(population_size/2)):
        crossover_prob=np.random.rand()
        if crossover_rate>=crossover_prob:
            parent_1= population_list[S[2*m]][:]
            parent_2= population_list[S[2*m+1]][:]
            child_1=parent_1[:]
            child_2=parent_2[:]
            cutpoint=list(np.random.choice(num_gene, 2, replace=False))
            cutpoint.sort()

            child_1[cutpoint[0]:cutpoint[1]]=parent_2[cutpoint[0]:cutpoint[1]]
            child_2[cutpoint[0]:cutpoint[1]]=parent_1[cutpoint[0]:cutpoint[1]]
            offspring_list[S[2*m]]=child_1[:]
            offspring_list[S[2*m+1]]=child_2[:]
```
### :arrow_down_small: Fix <br>
This example is a 10 x 10 Job shop problem, so each artifact appears on the chromosome 10 times, but because of the above mating action, the number of artifacts in some chromosomes will be less than 10 or greater than 10, and Forming an infeasible scheduling solution, so it is necessary to repair the infeasible chromosomes to make it a viable schedule.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/7.png" width="450" ​​height="285">
</div>
<br>

```python
    '''----------repairment-------------'''
    For m in range(population_size):
        Job_count={}
        Larger,less=[],[] # 'larger' record jobs appear in the chromosome more than m times, and 'less' records less than m times.
        For i in range(num_job):
            If i in offspring_list[m]:
                Count=offspring_list[m].count(i)
                Pos=offspring_list[m].index(i)
                Job_count[i]=[count,pos] # store the above two values ​​to the job_count dictionary
            Else:
                Count=0
                Job_count[i]=[count,0]
            If count>num_mc:
                Larger.append(i)
            Elif count<num_mc:
                Less.append(i)
                
        For k in range(len(larger)):
            Chg_job=larger[k]
            While job_count[chg_job][0]>num_mc:
                For d in range(len(less)):
                    If job_count[less[d]][0]<num_mc:
                        Offspring_list[m][job_count[chg_job][1]]=less[d]
                        Job_count[chg_job][1]=offspring_list[m].index(chg_job)
                        Job_count[chg_job][0]=job_count[chg_job][0]-1
                        Job_count[less[d]][0]=job_count[less[d]][0]+1
                    If job_count[chg_job][0]==num_mc:
                        Break
```
### :arrow_down_small: Mutant <br>

The mutation method used here is [Flow shop] (https://github.com/dostonhamrakulov/Code-demos-on-Python/tree/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/GA-flowshop) The same example of -flowshop/GA%20for%20flow%20shop%20problem.md) is a mutation by means of gene displacement. The mutation method is as follows:<br>
1. According to the mutation selection rate, determine how many genes in the chromosome are to be mutated. If there are six genes per chromosome and the mutation selection rate is 0.5, then 3 genes will be mutated.
2. Randomly select the gene to be displaced, assuming 5, 2, 6 are selected (here, the gene at this position is to be mutated)
3. Perform gene transfer and transfer as shown.
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/implementation%20with%20python/GA-flowshop/picture/6.png" width="450" ​​height="250">
</div>
<br>

```python
'''--------mutatuon--------'''
    For m in range(len(offspring_list)):
        Mutation_prob=np.random.rand()
        If mutation_rate >= mutation_prob:
            M_chg=list(np.random.choice(num_gene, num_mutation_jobs, replace=False)) # chooses the position to mutation
            T_value_last=offspring_list[m][m_chg[0]] # save the value which is on the first mutation position
            For i in range(num_mutation_jobs-1):
                Offspring_list[m][m_chg[i]]=offspring_list[m][m_chg[i+1]] # displacement
            
            Offspring_list[m][m_chg[num_mutation_jobs-1]]=t_value_last # move the value of the first mutation position to the last mutation position
  
```
### :arrow_down_small: Adaptive Value Calculation <br>

Calculate the completion time of the scheduling results formed by each chromosome and record them for comparison in subsequent selections<br>

:bulb: It should be noted here that since this is a minimization problem, the fitness value calculated for each chromosome, that is, the completion time, must be recorded in a reciprocal manner (chrom_fitness), so that when the roulette method is used later, Only the chromosomes with the shorter completion time can be selected, but there is still another record of the completion time (chrom_fit) of each chromosome, so that the final solution can be directly compared to the best solution of this round.
```python
    '''--------fitness value(calculate makespan)-------------'''
    total_chromosome=copy.deepcopy(parent_list)+copy.deepcopy(offspring_list) # parent and offspring chromosomes combination
    chrom_fitness,chrom_fit=[],[]
    total_fitness=0
    for m in range(population_size*2):
        j_keys=[j for j in range(num_job)]
        key_count={key:0 for key in j_keys}
        j_count={key:0 for key in j_keys}
        m_keys=[j+1 for j in range(num_mc)]
        m_count={key:0 for key in m_keys}

        for i in total_chromosome[m]:
            gen_t=int(pt[i][key_count[i]])
            gen_m=int(ms[i][key_count[i]])
            j_count[i]=j_count[i]+gen_t
            m_count[gen_m]=m_count[gen_m]+gen_t

            if m_count[gen_m]<j_count[i]:
                m_count[gen_m]=j_count[i]
            elif m_count[gen_m]>j_count[i]:
                j_count[i]=m_count[gen_m]

            key_count[i]=key_count[i]+1

        makespan=max(j_count.values())
        chrom_fitness.append(1/makespan)
        chrom_fit.append(makespan)
        total_fitness=total_fitness+chrom_fitness[m]
```
### :arrow_down_small: Select <br>

Here, the Roulette wheel selection mechanism is used<br>

```python
    '''----------selection(roulette wheel approach)----------'''
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
First compare the completion time of each chromosome (chrom_fit), select the best solution (Tbest_now) found in this round, and then compare it with the best solution (Tbest) found so far, once the solution of this round is found so far. If the solution is better, replace Tbest and record the result of the solution.
```python
     '''----------comparison----------'''
    For i in range(population_size*2):
        If chrom_fit[i]<Tbest_now:
            Tbest_now=chrom_fit[i]
            Sequence_now=copy.deepcopy(total_chromosome[i])
    
    If Tbest_now<=Tbest:
        Tbest=Tbest_now
        Sequence_best=copy.deepcopy(sequence_now)
```

### :arrow_down_small: Results <br>
After the end of the iteration, output the best schedule result (sequence_best) found in all iterations, the completion time of the result, and the program execution time.

```python
'''----------result----------'''
Print("optimal sequence",sequence_best)
Print("optimal value:%f"%Tbest)
Print('the elapsed time:%s'% (time.time() - start_time))
```
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/8.JPG" width="700" height="350">
</div>
<br>

### :arrow_down_small: Gantt Chart <br>
Use python plotly package to draw the Gantt chart. For detailed installation methods, please refer to [Plotly official website] (https://plot.ly/python/getting-started/)
```python
'''--------plot gantt chart-------'''
import pandas as pd
import plotly.plotly as py
import plotly.figure_factory as ff
import datetime

m_keys=[j+1 for j in range(num_mc)]
j_keys=[j for j in range(num_job)]
key_count={key:0 for key in j_keys}
j_count={key:0 for key in j_keys}
m_count={key:0 for key in m_keys}
j_record={}
for i in sequence_best:
    gen_t=int(pt[i][key_count[i]])
    gen_m=int(ms[i][key_count[i]])
    j_count[i]=j_count[i]+gen_t
    m_count[gen_m]=m_count[gen_m]+gen_t

    if m_count[gen_m]<j_count[i]:
        m_count[gen_m]=j_count[i]
    elif m_count[gen_m]>j_count[i]:
        j_count[i]=m_count[gen_m]

    start_time=str(datetime.timedelta(seconds=j_count[i]-pt[i][key_count[i]])) # convert seconds to hours, minutes and seconds
    end_time=str(datetime.timedelta(seconds=j_count[i]))

    j_record[(i,gen_m)]=[start_time,end_time]

    key_count[i]=key_count[i]+1


df=[]
for m in m_keys:
    for j in j_keys:
        df.append(dict(Task='Machine %s'%(m), Start='2018-07-14 %s'%(str(j_record[(j,m)][0])), Finish='2018-07-14 %s'%(str(j_record[(j,m)][1])),Resource='Job %s'%(j+1)))

fig = ff.create_gantt(df, index_col='Resource', show_colorbar=True, group_tasks=True, showgrid_x=True, title='Job shop Schedule')
py.iplot(fig, filename='GA_job_shop_scheduling1', world_readable=True)
```
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/9.JPG" width="650" height="350">
</div>
<br>

## :black_nib: Reference <br>
- [Wu, Min-You, Multi-Objective Stochastic Scheduling Optimization: A Study of Auto Parts Manufacturer in Taiwan](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi?o=dnclcdr&s=id=%22104NCKU5621001%22.&searchmode=basic)
- [Chin-Yi Tseng, Intelligent Manufacturing Systems](https://github.com/PO-LAB/Intelligent-Manufacturing-Systems)
- [
M. Gen, Y. Tsujimura, E. Kubota, Solving job-shop scheduling problem using genetic algorithms, Proc. of the 16th Int. Conf. on Computer and Industrial Engineering, Ashikaga, Japan (1994), pp. 576-579](https://ieeexplore.ieee.org/document/400072/)
- Chia-Yen Lee (2017), Meta-Heuristic Algorithms-Genetic Algorithms & Particle Swarm Optimization, Intelligent Manufacturing Systems course

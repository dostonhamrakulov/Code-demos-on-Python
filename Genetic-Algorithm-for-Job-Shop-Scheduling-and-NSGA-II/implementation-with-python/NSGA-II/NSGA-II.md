# Solving Job shop scheduling problem with Nondominated Sorting Genetic Algorithm II


*2018/07/15*
<br>

## :black_nib: Description of the problem <br>
This example is a 10x10 Jop shop problem, a total of 10 workpieces and 10 sets of machines, this problem is a multi-objective scheduling problem, a total of two targets are minimized total completion time (Makespan) and total weighted early time and delay time (total weighted Earliness and tardiness, TWET), the workpiece information is shown in the following table, the workpiece information is presented with the workpiece processing operating procedures, each workpiece will go through 10 machining operations, the following table records the workpiece in each processing operating procedures of the processing machine and processing time, There is also the priority and expiration time of each workpiece <br>

- Processing time  
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/NSGA-II/picture/1.png" width="650" height="300">
</div>
<br>
<br>

- Machine sequence
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/NSGA-II/picture/2.png" width="650" height="300">
</div>
<br>

-  Priority and Due date
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/NSGA-II/picture/3.png" width="200" height="300">
</div>
<br>

### :arrow_down_small: Scheduling target <br>
This example is a multi-objective scheduling problem, with a total of two targets being the minimum total completion time (Makespan) and the total weighted early time and delay time (total weighted earliness and tardiness, TWET), which are conflict targets, makes The sooner Pan expects to be completed, the better, but TWET hopes that the better the completion time, the better, too early or too late to complete will give the penalty value, so there must be a trade-off between the two solutions.
<br>

### :arrow_down_small: Coding and decoding  <br>
The encoding here is the same as the previous introduction of GA to solve the Job shop problem, mainly refer to [Gen-Tsujimura-Kubota ' s Method ()] (https://ieeexplore.ieee.org/document/400072/) proposed by the Job shop scheduling problem of the chromosome encoding method.<br>


The concept of this method is to represent the chromosome as a set of workpieces of the job processing program, a gene represents the processing of a workpiece, according to the number of chromosomes in the appearance of the workpiece, to know the current processing work of each workpiece, and then to correspond to the workpiece processing machine and processing time, in order to carry out the scheduling.<br>

Assuming that there is now a Job shop scheduling problem with N workpiece M machine, that chromosome will consist of N x M genes, because each workpiece will only be processed once per machine, a total of M machine processing, so each workpiece in the chromosome will appear M times, here to lift the above 3 x 3 A case study of Job Shop<br>

O<sub>ijk</sup></sub>  Indicates that the workpiece I uses the K machine in the operating program J

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-jobshop/picture/5.png" width="780" height="420">
</div>
<br>

## :black_nib: Description of the program <br>

Here mainly for a few important blocks in the program to explain, some details are not put in, if necessary please refer to [Complete program code](https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/NSGA-II/NSGA-II%20code.py)Or[Sample Archive](https://wurmen.github.io/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation%20with%20python/NSGA-II/Example_NSGAII.html)<br>

:bulb:As the following procedures have three main functions, it is recommended that you can self-print function input and output values to facilitate the execution of the function of the solution  

### :arrow_down_small: Import the required Kits <br>

```python
'''==========Solving job shop scheduling problem by gentic algorithm in python======='''
# importing required modules
import pandas as pd
import numpy as np
import time
import copy
```

### :arrow_down_small: Initial settings <br>
This area mainly contains read files or data given, as well as some parameters on the settings
```python
''' ================= initialization setting ======================'''
num_job=10 # number of jobs
num_mc=10 # number of machines

pt_tmp=pd.read_excel("JSP_dataset.xlsx",sheet_name="Processing Time",index_col =[0])
ms_tmp=pd.read_excel("JSP_dataset.xlsx",sheet_name="Machines Sequence",index_col =[0])
job_priority_duedate_tmp=pd.read_excel("JSP_dataset.xlsx",sheet_name="Priority",index_col =[0])

# raw_input is used in python 2
population_size=int(input('Please input the size of population: ') or 20) # default value is 20
crossover_rate=float(input('Please input the size of Crossover Rate: ') or 0.8) # default value is 0.8
mutation_rate=float(input('Please input the size of Mutation Rate: ') or 0.3) # default value is 0.3
mutation_selection_rate=float(input('Please input the mutation selection rate: ') or 0.4)
num_mutation_jobs=round(num_job*num_mc*mutation_selection_rate)
num_iteration=int(input('Please input number of iteration: ') or 1000) # default value is 1000

# speed up the data search
# Below code can also be  written "pt = pt_tmp.as_matrix().tolist()"
pt=[list(map(int, pt_tmp.iloc[i])) for i in range(num_job)]
ms=[list(map(int,ms_tmp.iloc[i])) for i in range(num_job)]
job_priority_duedate=[list(job_priority_duedate_tmp.iloc[i]) for i in range(num_job)]
start_time = time.time()

```
### :arrow_down_small: Non-atom sort function <br>
- This function has two input-population size and two adaptive values for each chromosome in the population (Makespan and TWET), both of which are recorded in the Chroms_obj_record dictionary
-  Output the chromosomes contained in each leading edge index
```python
'''-------non-dominated sorting function-------'''      
def non_dominated_sorting(population_size,chroms_obj_record):
    s,n={},{}
    front,rank={},{}
    front[0]=[]     
    for p in range(population_size*2):
        s[p]=[]
        n[p]=0
        for q in range(population_size*2):

            if ((chroms_obj_record[p][0]<chroms_obj_record[q][0] and chroms_obj_record[p][1]<chroms_obj_record[q][1]) or (chroms_obj_record[p][0]<=chroms_obj_record[q][0] and chroms_obj_record[p][1]<chroms_obj_record[q][1])
            or (chroms_obj_record[p][0]<chroms_obj_record[q][0] and chroms_obj_record[p][1]<=chroms_obj_record[q][1])):
                if q not in s[p]:
                    s[p].append(q)
            elif ((chroms_obj_record[p][0]>chroms_obj_record[q][0] and chroms_obj_record[p][1]>chroms_obj_record[q][1]) or (chroms_obj_record[p][0]>=chroms_obj_record[q][0] and chroms_obj_record[p][1]>chroms_obj_record[q][1])
            or (chroms_obj_record[p][0]>chroms_obj_record[q][0] and chroms_obj_record[p][1]>=chroms_obj_record[q][1])):
                n[p]=n[p]+1
        if n[p]==0:
            rank[p]=0
            if p not in front[0]:
                front[0].append(p)

    i=0
    while (front[i]!=[]):
        Q=[]
        for p in front[i]:
            for q in s[p]:
                n[q]=n[q]-1
                if n[q]==0:
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i=i+1
        front[i]=Q

    del front[len(front)-1]
    return front
```
### :arrow_down_small: A function that calculates a crowded distance <br>
- Input: The chromosome index contained in the leading edge to be calculated, the adaptive value of all chromosomes at present (the adaptive value of the chromosome to be calculated can be grasped through the index entered by the former)
- Output: The crowded distance of the chromosome being calculated
```python
'''--------calculate crowding distance function---------'''
def calculate_crowding_distance(front,chroms_obj_record):

    distance={m:0 for m in front}
    for o in range(2):
        obj={m:chroms_obj_record[m][o] for m in front}
        sorted_keys=sorted(obj, key=obj.get)
        distance[sorted_keys[0]]=distance[sorted_keys[len(front)-1]]=999999999999
        for i in range(1,len(front)-1):
            if len(set(obj.values()))==1:
                distance[sorted_keys[i]]=distance[sorted_keys[i]]
            else:
                distance[sorted_keys[i]]=distance[sorted_keys[i]]+(obj[sorted_keys[i+1]]-obj[sorted_keys[i-1]])/(obj[sorted_keys[len(front)-1]]-obj[sorted_keys[0]])

    return distance
```
### :arrow_down_small: Select a function <br>
A function (calculate_crowding_distance) is called inside this function to calculate the crowding distance, because in the process of selecting chromosomes to form a new population, when the number of chromosomes to be selected is less than the number of chromosomes in the current edge of the atom, You have to tell which chromosome I'm going to choose through a crowded distance.<br>
- Input: The size of the population, the chromosome index contained in the front edges obtained by the non-in function, the adaptive value of all chromosomes to be selected, and the scheduling results of each chromosome list
- Output: The new ethnic list and the index in the list of the original ethnic groups within the ethnic group
```python
'''----------selection----------'''
def selection(population_size,front,chroms_obj_record,total_chromosome):   
    N=0
    new_pop=[]
    while N < population_size:
        for i in range(len(front)):
            N=N+len(front[i])
            if N > population_size:
                distance=calculate_crowding_distance(front[i],chroms_obj_record)
                sorted_cdf=sorted(distance, key=distance.get)
                sorted_cdf.reverse()
                for j in sorted_cdf:
                    if len(new_pop)==population_size:
                        break                
                    new_pop.append(j)              
                break
            else:
                new_pop.extend(front[i])

    population_list=[]
    for n in new_pop:
        population_list.append(total_chromosome[n])

    return population_list,new_pop
```
### :arrow_down_small: Generate an initial solution <br>

Depending on the size of the population set above, the initial population is produced in a random manner, with a total of 10 = 100 genes per chromosome, each of which is stored by a list

```python
'''----- generate initial population -----'''
best_list,best_obj=[],[]
population_list=[]
for i in range(population_size):
    nxm_random_num=list(np.random.permutation(num_job*num_mc)) # generate a random permutation of 0 to num_job*num_mc-1
    population_list.append(nxm_random_num) # add to the population_list
    for j in range(num_job*num_mc):
        population_list[i][j]=population_list[i][j]%num_job # convert to job number format, every job appears m times

```

### :arrow_down_small: Mating <br>
A two-point mating method is used to initially produce a set of random sequences used to select the parental chromosome, followed by two two in the sequence, to decide whether to mate according to the mating rate, and, if so, to mate to produce two offspring and replace the original parental chromosome
```python
    '''-------- two point crossover --------'''
    parent_list=copy.deepcopy(population_list)
    offspring_list=[]
    S=list(np.random.permutation(population_size)) # generate a random sequence to select the parent chromosome to crossover

    for m in range(int(population_size/2)):

        parent_1= population_list[S[2*m]][:]
        parent_2= population_list[S[2*m+1]][:]
        child_1=parent_1[:]
        child_2=parent_2[:]

        cutpoint=list(np.random.choice(num_job*num_mc, 2, replace=False))
        cutpoint.sort()

        child_1[cutpoint[0]:cutpoint[1]]=parent_2[cutpoint[0]:cutpoint[1]]
        child_2[cutpoint[0]:cutpoint[1]]=parent_1[cutpoint[0]:cutpoint[1]]

        offspring_list.extend((child_1,child_2)) # append child chromosome to offspring list
```
### :arrow_down_small: Repair <br>
This example is a Job shop problem with 10 x 10，As a result, each workpiece appears 10 times in chromosomes, but because of the mating action above, it will cause the number of workpieces in some chromosomes to appear less than 10 or greater than 10, resulting in an unworkable scheduling solution, so this must be done for the unworkable chromosome repair action, so that it becomes a feasible schedule

```python
    '''----------repairment-------------'''
    for m in range(population_size):
        job_count={}
        larger,less=[],[] # 'larger' record jobs appear in the chromosome more than m times, and 'less' records less than m times.
        for i in range(num_job):
            if i in offspring_list[m]:
                count=offspring_list[m].count(i)
                pos=offspring_list[m].index(i)
                job_count[i]=[count,pos] # store the above two values to the job_count dictionary
            else:
                count=0
                job_count[i]=[count,0]
            if count>num_mc:
                larger.append(i)
            elif count<num_mc:
                less.append(i)

        for k in range(len(larger)):
            chg_job=larger[k]
            while job_count[chg_job][0]>num_mc:
                for d in range(len(less)):
                    if job_count[less[d]][0]<num_mc:                    
                        offspring_list[m][job_count[chg_job][1]]=less[d]
                        job_count[chg_job][1]=offspring_list[m].index(chg_job)
                        job_count[chg_job][0]=job_count[chg_job][0]-1
                        job_count[less[d]][0]=job_count[less[d]][0]+1                    
                    if job_count[chg_job][0]==num_mc:
                        break
```
### :arrow_down_small: Mutation <br>

The Mutant method used here [Flow shop](https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-flowshop/GA%20for%20flow%20shop%20problem.md) The same example is the mutation through the way of gene displacement, which is mutated in the following ways:<br>1. According to mutation selection rate determines how many percentages of genes in chromosomes are mutated, assuming that each chromosome has six genes and mutation selection rate 0.5, 3 genes are mutated.

2. Randomly select the gene to be displaced, assuming that 5, 2, 6 are selected (in this case, the gene at that position is mutated)
3. Gene transfer, the way of transfer as shown in the figure.
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/implementation-with-python/GA-flowshop/picture/6.png" width="450" height="250">
</div>
<br>

```python
    '''--------mutatuon--------'''   
    for m in range(len(offspring_list)):
        mutation_prob=np.random.rand()
        if mutation_rate <= mutation_prob:
            m_chg=list(np.random.choice(num_job*num_mc, num_mutation_jobs, replace=False)) # chooses the position to mutation
            t_value_last=offspring_list[m][m_chg[0]] # save the value which is on the first mutation position
            for i in range(num_mutation_jobs-1):
                offspring_list[m][m_chg[i]]=offspring_list[m][m_chg[i+1]] # displacement

            offspring_list[m][m_chg[num_mutation_jobs-1]]=t_value_last # move the value of the first mutation position to the last mutation position   

```
### :arrow_down_small: Adaptive value Calculation <br>
-  Calculate two target values per chromosome - makespan and TWET
- The parental (parent_list) and The Offspring (Offspring_list) are merged into a large list (total_chromosome), followed by a selection from this large list to create a new ethnic group
```python
     '''--------fitness value(calculate  makespan and TWET)-------------'''
    total_chromosome=copy.deepcopy(parent_list)+copy.deepcopy(offspring_list) # combine parent and offspring chromosomes
    chroms_obj_record={} # record each chromosome objective values as chromosome_obj_record={chromosome:[TWET,makespan]}
    for m in range(population_size*2):
        j_keys=[j for j in range(num_job)]
        key_count={key:0 for key in j_keys}
        j_count={key:0 for key in j_keys}
        m_keys=[j+1 for j in range(num_mc)]
        m_count={key:0 for key in m_keys}
        d_record={} # record jobs earliness and tardiness time as d_record={job:[earliness time,tardiness time]}

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

        for j in j_keys:
            if j_count[j]>job_priority_duedate[j][1]:
                job_tardiness=j_count[j]-job_priority_duedate[j][1]
                job_earliness=0
                d_record[j]=[job_earliness,job_tardiness]
            elif j_count[j]<job_priority_duedate[j][1]:
                job_tardiness=0
                job_earliness=job_priority_duedate[j][1]-j_count[j]
                d_record[j]=[job_earliness,job_tardiness]
            else:
                job_tardiness=0
                job_earliness=0
                d_record[j]=[job_earliness,job_tardiness]

        twet=sum((1/job_priority_duedate[j][0])*d_record[j][0]+job_priority_duedate[j][0]*d_record[j][1] for j in j_keys)
        makespan=max(j_count.values())
        chroms_obj_record[m]=[twet,makespan]
```
### :arrow_down_small: Non-atom sort calculation  <br>
```python
    '''-------non-dominated sorting-------'''      
    front=non_dominated_sorting(population_size,chroms_obj_record
```
### :arrow_down_small: Choose  <br>

```python
    '''----------selection----------'''
    population_list,new_pop=selection(population_size,front,chroms_obj_record,total_chromosome)
    new_pop_obj=[chroms_obj_record[k] for k in new_pop]
```

### :arrow_down_small: Comparison <br>
Find the best solutions for this round and compare them with the best solutions found in the iteration so far
```
    '''----------comparison----------'''
	if n==0:
        best_list=copy.deepcopy(population_list)
        best_obj=copy.deepcopy(new_pop_obj)
    else:            
        total_list=copy.deepcopy(population_list)+copy.deepcopy(best_list)
        total_obj=copy.deepcopy(new_pop_obj)+copy.deepcopy(best_obj)

        now_best_front=non_dominated_sorting(population_size,total_obj)
        best_list,best_pop=selection(population_size,now_best_front,total_obj,total_list)
        best_obj=[total_obj[k] for k in best_pop]
```

### :arrow_down_small: Results <br>
Eventually the output will be found in all iterations to find the best solution, because this is a multi-objective problem, so there may be multiple sets of solutions, this side of the setting is that the output and the size of the population of the same number of solutions
```python
'''----------result----------'''
print(best_list)
print(best_obj)
print('the elapsed time:%s'% (time.time() - start_time)
```

## :black_nib: Reference <br>
- [Wu, Min-You, Multi-Objective Stochastic Scheduling Optimization: A Study of Auto Parts Manufacturer in Taiwan](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi?o=dnclcdr&s=id=%22104NCKU5621001%22.&searchmode=basic)

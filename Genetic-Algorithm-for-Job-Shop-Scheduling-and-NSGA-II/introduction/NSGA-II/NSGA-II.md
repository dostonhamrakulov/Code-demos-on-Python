# Nondominated Sorting Genetic Algorithm II (NSGA-II)

*2018/06/12*
<br>
## :black_nib: Foreword
The previous article introduced what is genetic algorithm (GA), and the non-metaphase sorting gene algorithm (NSGA-II) introduced in this paper was improved by NSGA, which is K.Deb, A.Pratap, S.Agarwal, T. Meyarivan proposed in 2002 that the architecture of the algorithm is similar to that of GA, but it is specifically used to solve problems with multiple goals, so this article will introduce what NSGA-II is, and finally implement it through PYTHON. Solve the scheduling Jop Shop problem with dual targets.
<br>

## :black_nib: What is the concept of "dominated"?
In general, in the single-objective problem, we can easily judge what is the best solution, which solutions are good, and which are bad, but when we encounter multiple goals, the quality of the solution is not so easy to judge. Especially when there is a conflict between the targets, therefore, in the multi-objective problem, the concept of "Ling Yue" will be used to judge the quality of a solution. <br>

Let's take a simple example to illustrate this concept. Suppose there are four people who want to be friends with me. Their salary and height are as shown in the table below, and my friendship has two goals - height and salary, that is, I hope that the higher the salary and salary of the friends I have, the better, so both goals are maximizing the problem. From the table, we can find that A is better than others in terms of height and salary, so we call A Lingyue all other solutions, which are represented by mathematical symbols as A≻B, C, D, and A can be in this problem. Known as non-dominated solution, B and C have their own advantages in height and salary, so these two solutions are not in conflict, D is no worse than other heights or salaries. People, so D is overtaken by everyone, that is, A≻D, B≻D, C≻D. <br>

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/1.png" width="550" height="250">
</div>
<br>

Since the above problem is a two-objective problem, it is drawn into a graph, which can represent the two-dimensional space as shown in the upper right image. When we get more and more solutions (one solution in this question represents a person), ** once found A set of solutions, which are mutually incompatible with each other and are not given to Lingyue. We call this set of solutions Pareto-optimal solution**, which is formed by this set of solutions. The leading edge is called the Pareto-optimal front, which is the blue line in the figure. Therefore, in the multi-objective problem, the most critical part of ** is to find the best frontier of Plato**, and the solution on the leading edge is the solution we want, so in the multi-objective problem, it is not like the single-objective problem. There is a single best solution, and in general there will be multiple sets of solutions.

## :black_nib: NSGA-II Architecture
The architecture of NSGE-II is shown in the figure below. As mentioned in the introduction, its architecture is similar to that of GA. The only big difference is the part of the red box, so the next step will be to put more emphasis on the four in the red box. The parts are explained at the end.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/2.png" width="550" height="350">
</div>
<br>

### :arrow_down_small: Elitisr Strategy <br>

In order to ensure that the remaining chromosomes are excellent and feasible, the elite strategy is adopted in the fitness evaluation. This strategy is simply a mating, parental and mating mutation before mutation. The descendants are kept together and selected to prevent the chromosomes from getting worse and worse, and to avoid losing the good solution found.

### :arrow_down_small: Nondominated sorting approach <br>

Compared to the original NSGA, NSGA-II proposes a faster non-over-ordering method with less time complexity and no need to specify the sharing function. The following will introduce the entire non-overlapping order. The main concept, and use the above example to illustrate, here I divide it into five implementation steps. (For details of NSGA, please refer to [Original] (https://pdfs.semanticscholar.org/b39d/633524b0b2b46474d35b27c2016f3c3f764d.pdf)) <br>

:balloon: **Step 1. Calculate two entities for each solution: n<sub>p</sup></sub>, S<sub>p</sup></ Sub>** <br>

 p is the pronoun of the solution to be solved, n<sub>p</sup></sub> represents the number of solutions of the Ling Yue solution (Imagine how many solutions are solved by the solution), S<sub>p</sup ></sub> is the solution set of the solution to the solution (that is, who is being solved by P.). Taking the above example as an example, you can get the following table:

It can be clearly seen from the image on the right that the solution A has over all the solutions, so S<sub>A</sup></sub>={B, C, D} and n<sub>A</ Sup></sub>=0; B is only given to Ling by A, and Ling knows D, so n<sub>B</sup></sub>=1, S<sub>B</sup>< /sub>={D}, others and so on...
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/3.png" width="600" height="300">
</div>

:balloon: **Step 2. Find the members of the first nondominated front: (n<sub>p</sup></sub>= 0** <br>

Through the previous step, we can get a list of the relationship between each solution and other solutions. Then we will classify these solutions to facilitate the final selection of chromosomes (solutions). The concept is as shown in the following figure. The Lingyue relationship table divides the solutions into different levels. The non-linger solution of the first layer has the highest level (that is, the Platonic front solution), while the second layer has the second highest level, and so on. The higher the priority is selected as the new population (population)

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/4.png" width="325" height="250">
</div>

Therefore, in the beginning, we must first find the first layer of the first solution, that is, the solution of n<sub>p</sup></sub>= 0 in the table formed in the previous step, in this case, the solution A. And the solution on the blue line, and give these solutions a rank of 1.

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/5.png" width="300" height="175">
</div>
<br>

:balloon: **Step 3. For each solution of n<sub>p</sup></sub>= 0, visit each of these solutions in the S<sub>p</sup></sub> collection Solution (q) and subtract the number of n<sub>p</sup></sub> from the solution (< each> with each solution with n<sub>p</sup></sub >= 0, we visit each member (q) of its set S<sub>p</sup></sub> and reduce its domination count by one.)**<br>

:balloon: **Step 4. In the previous step of accessing each solution, if any solution n<sub>p</sup></sub> becomes 0, then the solution belongs to the second non-transition front , so give it a sorting level of 2**<br>
**(If for any member the domination count becomes zero, it belongs to the second nondominated front.)**<br>

From Step 2, we know that the solution of n<sub>p</sup></sub>= 0 is only A, and the solution of A is more than B, C, D (from S<sub>p</sup> </sub> learned), so we went to visit these solutions one by one, and reduced their n<sub>p</sup></sub> by one, to get the updated table as follows, and in the process of visiting It is found that the n<sub>p</sup></sub> of the solution B and the solution C become 0, so they are the solutions of the second non-transition leading edge, so they are given a rank of 2, that is, the second Priority is selected as a solution to population

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/6.png" width="300" height="175">
</div>
<br>
:balloon: **Step 5. Repeat the above steps until all leading edges are recognized**<br>
**(The above procedures are continued until all fronts are identified.)**<br>

:bulb: Pseudo code

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/7.png" width="450" ​​height="500">
</div>

### :arrow_down_small: Crowding distance (Crowding-distance)

In order to maintain the diversity of solutions and to make choices when different solutions are located at the same non-linger level, a method of crowding distance is proposed to evaluate the density relationship between each solution in the group and its surrounding solutions. The concept is as follows: As shown, when we calculate the crowded distance of a particular solution, we follow the non-over the leading edge of the solution, and find the two adjacent solutions that are closest to the specific solution along each target in the leading edge. To calculate the average distance between the two solutions, and finally sum the distances calculated by each target to obtain the crowded distance of the specific solution. In the dual-target example of the following figure, the crowded distance of the i-th solution at its leading edge is the average side length of the rectangle enclosed by the two solutions closest to the solution i.

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/8.png" width="500" height="350">
</div>

As mentioned in the previous paragraph, calculating the crowded distance helps to maintain the diversity of the solution, which means that when a solution is to be selected from a group of solutions located at the same non-over the leading edge, ** tends to choose a crowded distance. The big solution **, because the congestion distance is larger, indicating that the solution is more different from other solutions, which helps to avoid the situation of falling into the local solution during the iterative process of the algorithm, and to achieve exploration (exploration) The effect is expected to find more and better solutions, and the congestion distance is calculated in detail as follows:<br>

:balloon: **Step 1. Sort each target's solution from small to large, and calculate each solution by the following formula. The estimated distance of each target is distance<sub>o</sup></sub> (i)**<br>

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/9.png" width="360" height="130">
</div>

o indicates the target, F<sub>o</sup></sub>(i) is the ith solution after sorting the target O, F<sub>o,max</sup></sub> is the maximum boundary solution , F<sub>o,min</sup></sub> is the minimum boundary solution<br>

##### :zap: The above formula has a normalization action to avoid the difference in numerical scale between different target solutions, so the targets are converted to the same scale for subsequent comparison. <br>
<br>

:balloon: **Step 2. Add the estimated distance (distance<sub>o</sup></sub>(i)) calculated by each solution to each target to get each solution. Total crowding distance CD(i)** <br>

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/10.png" width="200" height="130">
</div>

:bulb: Pseudo code

<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/NSGA-II/Picture/11.png" width="560" height="380">
</div>

### :arrow_down_small: Selection mechanism

Through the above process, each chromosome (solution) in the final population has two attributes:
- non-linggrade level (nondomination rank)
- Crowding distance

When you finally pick a new population member, you will pick it according to the following rules:
1. Compare the non-improvement level of each solution first, ** the higher level solution (the smaller number), the higher the priority is selected**
2. If the non-upgrade levels of the two solutions are the same, compare the crowded distance, ** the larger the crowded distance, the higher the priority is selected**

## :black_nib: Summary
Finally, through the following gif diagram, the entire process of NSGA-II is integrated. For each iteration, the following actions will be performed until the set conditions are reached:

1. First, there is an initial population (parental) P<sub>t</sup></sub> containing N chromosomes, which are produced by mutation and mating to produce progeny Q<sub>t</sup></sub > .
2. Due to the adoption of the elite strategy, the parent and the offspring are retained together for selection.
3. Then perform non-overlapping sorting to get the non-overlapping level of each solution (F<sub>1</sup></sub><level 1>, F<sub>2</sup></sub ><level 2>.....).
4. Finally, select the new N chromosomes as the population of the next iteration, first select according to the level of non-imperial hierarchy. If the following picture shows, the number of chromosomes remaining to be selected into the new population is smaller than the next one to be selected. The number of chromosomes in the non-over-the-level hierarchy is selected by the crowded distance, and the larger the crowded distance is selected to enter the new population.
5. Finally, generate a new population P<sub>t+1</sup></sub> and proceed to the next iteration to repeat the above process.

![](https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/blob/master/introduction/ NSGA-II/Picture/123.gif)

### :black_nib: Reference
- [K. Deb, A. Pratap, S. Agarwal, T. Meyarivan, A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II, IEEE Trans. Evol. Comput. 6(2) (2002) 182] (https:/ /ieeexplore.ieee.org/document/996017/) <br>
- [Wu, Min-You, Multi-Objective Stochastic Scheduling Optimization: A Study of Auto Parts Manufacturer in Taiwan] (https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi?o=dnclcdr&s =id=%22104NCKU5621001%22.&searchmode=basic)

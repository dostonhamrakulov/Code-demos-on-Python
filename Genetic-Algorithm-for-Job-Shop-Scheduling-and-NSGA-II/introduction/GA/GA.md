# Genetic Algorithm (GA)
*[POLab](http://polab.imis.ncku.edu.tw/)* <br>
*[cheng-man wu](https://www.linkedin.com/in/chengmanwu)*<br>
*2018/12/01*
<br>

##: black_nib: GA Background (Background)
The architecture of the Gene Algorithm (GA) was originally proposed by Professor John Holland in 1975**. The main inspiration for this algorithm was the evolutionary mechanism in the biosphere**, in nature, ** The reproduction and inheritance of organisms is through the mating and mutating of chromosomes to change the composition of different genes to produce the next generation. The chromosomes are mainly composed of DNA and proteins. A DNA fragment represents a gene that controls a certain trait. The chromosome is also represented by many genes. <br>

In simple terms, genetic algorithms are developed through the concept of expressing a potential solution or parameter of a problem in a chromosome, by encoding the chromosome into a string or numerical form, and each value or The string represents the gene in the chromosome, indicating a part of the solution, and then through the mutation and mating, to produce the next generation, that is, different potential solutions, and finally the concept of survival of the fittest, elimination of discomfort, good solution A reservation is made to make the next round of mating mutations to produce a better solution until the set stop condition is reached, expecting to be able to jump off the local solution in the future to find the global optimal solution. <br>

Gene algorithm can be used to solve most optimization problems, and this topic focuses on the combination and application of GA and scheduling problems. Therefore, the following will introduce the concept of GA and implement the unit. It shows how GA is applied to scheduling problems.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/12.png" width=" 425" height="300">
</div>
<br>

<p align="center">Image taken from: South textbook</p>

## :black_nib: GA Process (Procedure)
The figure below shows the flow chart of GA. Next, each step will be explained.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/14.png" width=" 600" height="500">
</div>
<br>

### :arrow_down_small: Encoding (Encoding) <br>

GA during the entire execution, will run on alternating ** ** ** called code space (Coding space) ** the solution space (Solution space), but mainly in the genetic manipulation performed in the encoding space, like mutant And the mating action, in the solution space, perform the evaluation and selection, as shown below:

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/11.png" width=" 700" height="300">
</div>
<br>

In the coding space, ** is represented in a coded form, as mentioned in the background. **In C, usually a chromosome (Chromosome) represents a potential solution to solve the problem**, The chromosome is made up of genes, so the gene is part of the solution. Therefore, before the algorithm starts, the chromosome design must be performed according to the attributes of the problem. <br>
<br>
There are many ways to encode chromosomes. The most common encoding method is Binary encoding, which is to convert the solution into a string of 1 and 0. This way is also used most often when your solution. When it is a numeric form, as shown below:<br>

:bulb: In the schedule, usually the workpiece processing sequence is treated as a chromosome<br>

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/13.png" width=" 450" height="150">
</div>
<br>

We use [Wikipedia] (https://en.wikipedia.org/wiki/%E6%9F%93%E8%89%B2%E9%AB%94_(%E9%81%BA%E5%82%B3 %E6%BC%94%E7%AE%97%E6%B3%95)) The example given is a simple coding description:<br>

**Example**<br>
Suppose now that there is a problem to find an integer x between 0 and 255. This integer x should have the largest value of the function f(x)=x<sup>2</sup></sub> (of course this It's a very simple question, but here is a simple explanation, so don't worry too much about XD). <br>

Since the integers from 0 to 255 are all possible to solve, in order to represent all the integers in this interval, a 2-bit binary string can be used to represent a solution. As shown in the figure below, each chromosome in GA is It consists of 8 genes. <br>

:bulb: Why is it using 8 bits?
 0 ~ 255 has a total of 256 numbers, so in terms of binary encoding, 8 genes can just represent 2<sup>8</sup></sub>=256 counts<br>

:bulb: In addition, by this example, the meaning of decoding (Decoding) is explained by the way, because in GA we represent a solution through the encoded chromosome, so when it is to be evaluated and selected, the chromosome must be pushed back to the original To solve, you must go through the decoding step, as shown in the figure, to convert the chromosome back to the actual value it represents. The way the conversion depends on how the chromosome was designed. <br>


<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/2.png" width=" 550" height="475">
</div>
<br>

Of course, there are many ways to encode, except for the binary encoding method, which can be directly expressed in real numbers or in the form of letters, etc., or in the scheduling of applications in this topic example, processing of a workpiece. Sequences are used as representations of chromosomes. Therefore, in GA, the coding of chromosomes is also an important part. The quality of chromosome design may affect the difficulty of encoding and decoding or the efficiency of the entire GA. <br>

:bulb: Here are a few of the questions you need to decide when coding:
1. What symbols are used to encode? Binary, real numbers...
2. What is the coding structure? One-dimensional, two-dimensional...
3. The length of the chromosome? Fixed length, variable length...
4. What kind of content should be included in the code? Only the solution, or the parameter to be added, must be encoded together.

#### :unlock: The parameters you need to pay attention to or set in this step.
- Encoding method
- the length of the chromosome (Chromosome length)

-------------------------------------------

### :arrow_down_small: Initial population <br>

When the chromosome design is completed, it will formally enter the main body of the GA algorithm. At the beginning we must first generate a group of chromosomes as the initial group, which is called the initial solution. As shown in the figure below, they can also be called GA. The initial parents (Parents) are a bit like the first generation of ancestors of an organism, and then through the mating and mutation of the following steps to produce offspring (Offspring) to breed more and better descendants, so here The steps must first determine the size of the group.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/3.png" width=" 400" height="285">
</div>
<br>

#### :unlock: The parameters you need to pay attention to or set in this step.
- Population size (Population size)

--------------------------------------------
In the GA, the so-called "Genetic operations" - mating and mutations - are used to generate offspring, that is, to generate new potential solutions (of course, it is also possible to generate repetitive solutions), and hope can be explored. The effect of (exploration) increases the diversity of solutions, hoping to break away from local solutions and find more excellent solutions.

### :arrow_down_small: Mating (Crossover) <br>

Usually, when mating, the crossover rate of any two chromosomes is determined according to the set crossover rate, and some genes of the two chromosomes are exchanged and recombined to generate new chromosomes. <br>
There are many ways to mate, and the three common mating methods are described below (in the scheduling example description, other different mating methods will be demonstrated.)<br>

(The following are all demonstrations of binary-encoded chromosomes)<br>

**1. Single point crossover** <br>

Randomly select a gene position as a transaction point, and cut the parent chromosome into two segments with this gene position, then fix one segment and exchange another segment to generate two new children.
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/4.png" width=" 450" height="355">
</div>
<br>

**2. Multi-point crossover** <br>

The concept of multi-point mating is similar to that of single-point mating. It only becomes to select multiple gene positions at a time as the transaction point, and then according to the personal setting, some segments are fixed, and the rest are exchanged to generate new children.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/5.png" width=" 450" height="355">
</div>
<br>

**3. Uniform crossover**<br>

Uniform mating is to randomly generate a binary code equal to the length of the parental chromosome, called Crossover Mask. When the value in Mask shows 1, the genes corresponding to the parental chromosome must be exchanged with each other. Then there is no need to exchange, in this way to generate new children.

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/6.png" width=" 460" height="325">
</div>
<br>

#### :unlock: The parameters you need to pay attention to or set in this step.
- Mating method (Crossover method)
- Crossover rate


### :arrow_down_small: Mutation (<br><br>

In order to increase the diversity of the solution and avoid falling into the local solution, for each chromosome, it is determined whether a certain chromosome is to be mutated according to the set mutation rate, and the gene in a single chromosome is changed in a random manner, a common The method is to exchange several genes in a randomly selected chromosome for a single chromosome, as shown in the following figure:
<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/7.png" width=" 445" height="225">
</div>
<br>

#### :unlock: The parameters you need to pay attention to or set in this step.
- Mutation method
- Mutation rate

---------------------------------

### :arrow_down_small: Fitness computation <br>

:balloon: **adaptive function to evaluate chromosome quality**<br>

When solving problems with GA, you must formulate a fitness function that belongs to this problem. **Accommodation function is a mechanism for evaluating the quality of a chromosome. ** Determine the chromosome by converting the fitness value. Fitness, when the fitness value is better, when the chromosome is selected in the next step, the chromosome has a greater chance of being retained and continues to multiply. On the contrary, the worse the adaptation value, the more likely it is to be eliminated.

:balloon: **Development function (Fitness function)** <br>

In general, the **adaptive function is usually the objective function for solving the problem**, or a function sufficient to represent the problem object to be able to fully evaluate the quality of the chromosome.

:bulb: Basically, before performing this step, the chromosome must be decoded to further calculate the fitness value.

#### :unlock: The parameters you need to pay attention to or set in this step.
- Fitness function

-----------------------------------

### :arrow_down_small: Select (Selection) <br>

In order to preserve better chromosomes for evolution, this step is mainly based on the chromosomes produced in the above steps, through a selection mechanism, to select the best quality chromosomes to form a new ethnic group. For the evolution of the next round, the following two selection mechanisms will be introduced:<br>

**1. Roulette wheel** <br>

The concept of the roulette method can be imagined as a darts game. First, we will divide a rotatable roulette into a number of fan-shaped areas of different sizes. Each chromosome has a corresponding fan-shaped area. Then we take out a Darts, randomly shot to this roulette, when I shoot in the sector, the chromosomes belonging to this sector will be selected, so it is conceivable that having a larger chromosome will have a greater chance of being selected. Of course, the fan-shaped area to which the chromosome belongs is not arbitrarily divided, but is derived from their fitness values. The detailed steps of the roulette method are explained below:<br>

<br>
<div align=center>
<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/14.gif" width=" 445" height="250">
</div>
<br>

(eval(): adaptation function, v<sub>k</sup></sub>: kth chromosome, eval(v<sub>k</sup></sub>): adaptation of the kth chromosome Value) <br>

:balloon: Step 1. Calculate the sum of the fitness values ​​of all chromosomes to be selected F

<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/8.png" width=" 250" height="115">

:balloon: Step 2. For each chromosome v<sub>k</sup></sub>, calculate the probability of selection p<sub>k</sup></sub>

<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/9.png" width=" 360" height="50">

:balloon: Step 3. For each chromosome v<sub>k</sup></sub>, calculate its cumulative probability q<sub>k</sup></sub>

<img src="https://github.com/dostonhamrakulov/Code-demos-on-Python/blob/master/Genetic-Algorithm-for-Job-Shop-Scheduling-and-NSGA-II/introduction/GA/picture/10.png" width=" 450" height="70">

:balloon: Step 4. From the interval [ 0 , 1 ], randomly generate a number r


:balloon: Step 5. If r <= q<sub>1</sup></sub>, select the first chromosome, otherwise, when q<sub>k-1</sup></sub> < r < q<sub>k</sup></sub>, select the kth chromosome v<sub>k</sup></sub>


:balloon: Step 6. Go back to Step 4 until the number of chromosomes selected reaches the set population size<br>

**Example**<br>
Suppose now that there is a problem of maximization, there are four chromosomes, and the fitness values ​​of these four chromosomes are 4, 7, 3, and 6 respectively.
- Step 1. Calculate the sum of the fitness values ​​of all chromosomes to be selected F<br>
F = 4 + 7 + 3 + 6 = 20

- Step 2. Calculate the probability of selection for each chromosome vk pk<br>
P1 = 0.2, p2 = 0.35, p3 = 0.15, p4 = 0.3

- Step 3. For each chromosome vk, calculate its cumulative probability qk<br>
Q1=0.2, q2=0.55, q3=0.7, q4=1

- Step 4. From the interval [ 0 , 1 ], randomly generate a number r <br>
r = 0.6

**2. Tournament selection** (<br>

Randomly select a number of chromosomes from the ethnic group, compare their fitness values, select the chromosome with the best fitness value, and repeat the above actions until the number of selected chromosomes reaches the set population size. (To select the number of chromosomes to be compared at a time, you can set a reasonable number of choices according to the individual)

#### :unlock: The parameters you need to pay attention to or set in this step.
- Selection mechanism

----------------------------------------
### :arrow_down_small: Termination condition <br>

Usually, a stop mechanism is set to be used as the termination condition. Once the set stop condition has not been reached, the new ethnic group generated in the last step is returned to the step of mutation and mating, and then other steps are performed in sequence. The loop is continually looped until the set stop condition is reached, and finally the best solution obtained in all iterations is obtained. The usual stopping mechanism is as follows:
- Number of iterations
- The number of times the solution has been changed several times in succession
- Stop when the difference of several consecutive solutions is less than the set number

#### :unlock: The parameters you need to pay attention to or set in this step.
- Number of iterations

## :black_nib: Summary (Summary)
After the above introduction, here is a summary of the several parameters that must be set when using a gene algorithm: <br>

- Encoding method
- the length of the chromosome (Chromosome length)
- Population size (Population size)
- Mating method (Crossover method)
- Crossover rate
- Mutation method
- Mutation rate
- Fitness function
- Selection mechanism
- Termination condition

## :black_nib: Reference
- Holland, J. H. (1975). Adaptation in natural and artificial systems. Ann Arbor, MI: University of Michigan Press.
- Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization and Machine Learning. Addison-Wesley Longman Publishing Co., Inc. Boston, MA.
- Chia-Yen Lee (2017), Meta-Heuristic Algorithms-Genetic Algorithms & Particle Swarm Optimization, Intelligent Manufacturing Systems course

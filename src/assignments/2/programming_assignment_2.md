# Programming Assignment 2: Probabilistic State

You will have the option of three possible programming assignments, depending on the skills you'd like to exercise. You are welcomed to work in pairs. 

## Objectives

Each possible assignment will have specific learning objectives related to the topics in the course, designed to build depth. 

### Web Demo
You will additionally be asked to produce an externally-facing demonstration of your code. The benefit to undergraduates and those seeking industrial employment is that your demo can be listed as part of your portfolio work. For graduate students, an increasing number of academic conferences are requiring artifacts, which typically take the form of Notebooks, web demonstrations, or containerized environments (for more core systems work). Spinning up web servers and producing quick demonstrations is an essential skill for anyone in a computational field. 

If you manage your own server, you may host there. However, all students at UVM have access to the web server [silk](https://silk.uvm.edu/manual/). If you have not set up silk already, you will need to email `saa@uvm.edu` requesting an account. 

Since all of your code should be in Python, you should use [Brython](https://brython.info) to make it web-accessible. The demo can be a simple setup, with two panes: one for input (which itself may contain multiple panes) and one for output. 

### How to submit

Similarly to the [first programming assignment](../1/programming_assignment_1.html#how-to-submit), `gzip` and archive all of your files, including a README with a link to your web demo into a file with the name `p2_<your_last_name>.tgz`. If you collaborate with another student, list both of your last names; only one of you needs to upload the file. 

## Option 1: Implement heuristic search for minimal queries

Write a program that takes two inputs:

1. A Bayesian Network
2. A query on the Bayesian Network

and outputs a minimized representation of the query _and a cost associated with its computation_.  The network should be specified in the [Graph Modeling Language](https://en.wikipedia.org/wiki/Graph_Modelling_Language). This should be read in from a file. Your query should have the grammar that follows this rough BNF-esque specification:

```
query ::= "P(" <joint> [<conditional>] ")"
joint ::= $A_1$["=" $a_1$] ["," <joint>]
do ::= "do(" <joint> ")"
conditional ::= "|" <joint> [<do>]
```

The query can be a command line argument. Thus, I expect to be able to run your program like so:

> python -m minimize_probs --dag file_with_dag.gml --query "P(C|D, do(E=e))"

The main entry point of your code[^1] will roughly follow these steps:

1. Load in the DAG. You can use the Python library [networkX](https://networkx.org) to read the graphs. 
2. Parse the query and determine which variables are being jointly queried and which are being conditioned on.
3. Verify that the graph is a DAG. If it is not, print an error and exit the program.
4. Generate the factorized joint probability distribution for the graph. 
5. Apply only valid operations to the joint probability distribution to produce an expression equivalent to the input query. 

This final step can be framed as a search problem. Your initial state is the factorized distribution and your final state is an expression equivalent to the input query. Each action you take is the application of a rule to a point in a data structure representing the term you are rewriting:

1. Bayes Rule ($P(X\mid Y) = P(Y\mid Y)P(Y)/P(X)$).
2. Multiplication/Chain Rule/Conditional probability ($P(X, Y) = P(X\mid Y)P(Y)$).
3. Law of total probability/marginalization ($\sum_{y\in\mathcal{Y}} P(X, Y=y) = P(X)$).
4. Unit measure ($\sum_{x\in\mathcal{X}} P(X=x) = 1$).

While these four rules form the core set of rewrites, you may want to break them into smaller rewrite rules. 

The search part of this assignment involves two choices: which rule to apply and which point in the expression to alter. Your objectives are:

1. **Produce a _correct_ expression for the input query.** An expression is correct if (a) for all inputs, it produces the same outputs as the query expression and (b) it only contains quantities encoded by the DAG.
2. **Produce a _minimal_ expression for the input query.** An exprssion is minimal according to a cost function you will define. This is a design you choice you will make. The only requirement is that it contain the fewest number of variables. You may additionally assign cost to e.g. the position of summation symbols.
3. **Produce this expression with the fewest rewrite steps.** Your output should include both the resulting expression and the number of steps your program took to find it. 

For this assignment, you may assume that all variables are binary, although if you'd like to extend them to be arbitrary and finite $k$-ary variables, you are welcome to do that. Note that I do not recommend representing variables with infinite support at this time. 

### Objectives

This assignment develops three skills: (1) defining a heuristic function, (2) manipulating probabilistic expressions, and (3) implementing a search strategy. I strongly recommend this option if you struggled with Question 2 on Exam 2. 

## Option 2: Implement a game theory game generator

For this assignment, your task will be to generate 2-player $n\times m$ games, along with their solution and a [simulation module](#simulation). Your main program should be at least 1-step interactive: 

1. Generate a game according to a [specification](#game-speciication) 
2. Print a representation of the game
3. Query the user for their strategy
4. Verify whether the user's strategy is optimal

### Specification

You may support the specification as command line arguments or by reading in a, e.g., [YAML](https://yaml.org) or [TOML](https://toml.io/en/) configuration file. It should include parameters that capture the following information:

* number of player actions
* number of opponent actions
* whether the game is zero-sum and if so, whether there is a saddle point
* whether there should be a dominant strategy
* whether the best stategy is the same under coordination

You will then generate games according to these specifications, along with their solutions. **All rewards should be integer-valued.**

### Simulation

In addition to the core program, you should write a simulator that plays two agents against each other for multiple games. Create a suite of at least three agents, each of which may have some or all of the following characteristics:

**Starting strategies**

1. Selects action uniformly at random. 
2. Starts with the globally highest payout. 
3. Starts with the globally lowest payout.
4. Starts with the optimal game-theoretic solution.

**Subsequent strategies**

1. Maximizes in the next round, conditioned on the other player's action in this round.
2. Models action selection as belief, updates beliefs about stratgies (i.e., model the choice as a bandits problem.)
3. Maintain a probability $p$ of switching to a random strategy, initially set to 1. If the agent loses, randomly select a number from $[0,1]$ and if the number is greater than $p$ (or if $p$ is 1), the randomly select a new action and reset $p$ to 1. Otherwise, update $p$ to be $0.5p$.

Hand in a Jupyter Notebook showing the results of 3 agents playing each other (9 settings) for 100 randomly generated $2\times 2$ games under the following configurations:

1. Game is zero-sum with saddle point
2. Game is zero-sum without saddle point
3. Optimal strategy is dominant 
4. Optimal strategy is mixed

Track whether each agent converged to the optimal solution according to your program.

Finally, generate 1000 $2\times 2$ games where the payoff for each player is between -10 and 10 and report how many appear in each of the four configurations listed above. 

### Objectives

This assignment develops three skills: (1) mechanism design, (2) solving for optimal solutions to 2-player games, and (3) Monte Carlo simulation. I strongly recommend this option if you struggled with Question 5 on Exam 2. 

## Option 3: Implement the probabilistic modeling worksheet as a simulation

_Note: I am including this option here for students because it was requested, but I do not recommend it._

Implement the scenario outlined in the [probabilistic modeling worksheet](https://www.overleaf.com/project/6256bff349034c7f1b9ea170) and support queries on strategies as expressed in LTL. 

In addition to implementing the basic mechanics described in the the worksheet, you will need to (1) compute the expected utility in terms of hull damage and system liveness for an arbitrary time window and (2) translate a high-level strategy expressed in LTL into an executable strategy within the system. 

Thus, the minimum specification requires you to implement all of the reasoning such that I can use your program to answer all of the queries listed in the worksheet, modulo minor variation.


[^1]: If you are not familiar with it, I strongly recommend you use [argparse](https://docs.python.org/3/library/argparse.html) to handle command line arguments. 
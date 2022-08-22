# Basic Decision Theory 

In class, we saw an example of decision theory: we had the choice between buying two cars, $C_1$ and $C_2$ (we could not decide to not buy a car) and we had the option of running at most one test on one of the cars, where test $T_1$ could only be used on car 1 and test $T_2$ could only be used on car 2: you can think about this as if the manufacturer created the tests, so you cannot apply $T_1$ on $C_2$ and vice versa. 

We were also told the following information about the cars and tests:

* Car $C_1$ costs $500 below the market rate.
    * If $C_1$ is faulty (i.e., $C_1$ = -), then it costs $700 to repair.
* Car $C_1$ is not faulty with probability 0.7.
* Test $T_1$ tells us whether $C_1$ is faulty or not and costs $50.
    * $T_1$ is a true positive 80% of the time.
    * $T_1$ is a true negative 65% of the time. 


* Car $C_2$ costs $250 below the market rate.
    * If $C_2$ is faulty (i.e., $C_2$ = 0), then it costs $150 to repair.
* Car $C_2$ is not faulty with probability 0.8.
* Test $T_2$ tells us whether $C_2$ is faulty or not and costs $20.
    * $T_2$ is a true positive 75% of the time.
    * $T_2$ is a true negative 70% of the time. 

From this information, we can enumerate some facts from this information alone:

1. $P(C_1 = +) = 0.7$
1. $P(C_1 = -) = 0.3$[^1]
1. $P(C_2 = +) = 0.8$
1. $P(C_2 = -) = 0.2$[^1]
1. $P(T_1 = + \mid C_1 = +) = 0.8$
1. $P(T_1 = - \mid C_1 = +) = 0.2$[^1]
1. $P(T_1 = + \mid C_1 = -) = 0.35$[^1]
1. $P(T_1 = - \mid C_1 = -) = 0.65$
1. $P(T_2 = + \mid C_2 = +) = 0.75$
1. $P(T_2 = - \mid C_2 = +) = 0.25$[^1]
1. $P(T_2 = + \mid C_2 = -) = 0.3$[^1]
1. $P(T_2 = - \mid C_2 = -) = 0.7$

[^1]: These quantities were all calculated using the law of total probability from the information given.

Now, the first thing we did was consider the case where we run no test. Since there is no direct cost associated with not running the test, we only need to compute the expected utility (cost) of each car:

$EU[C_1] = P(C_1 = +)(cost) + P(C_1 = -)(cost + repair) = 0.7*(-500) + 0.3*(-500+700) = -290$
$EU[C_2] = P(C_2 = +)(cost) + P(C_2 = -)(cost + repair) = 0.8*(-250) + 0.2*(-250+150) = -220$

Since we want to minimize cost, we choose the car with the minimum expected utility (car 1).

The next thing we did was ask: suppose we decided to run test 1. Given the result of that test, which car should we choose?

We need to break this problem into cases: the first case will condition on the the test returning + and the second case will condition on the test returning -. As part of your homework, you will work your way up to making a decision about which test to run, but first we are going to reason about adding in a small amount of additional uncertainty.

$EU[C_1 \mid T_1 = +] = P(C_1 = + \mid T_1 = +)(cost + test) + P(C_1 = - \mid T_1 = +)(cost + repair + test)$

Note that we do not currently have $P(C_1 = + \mid T_1 = +)$. Therefore, we must calculate it. Let's use Bayes Rule:

$P(C_1 = + \mid T_1 = +) = P(T_1 = + \mid C_1 = +)P(C_1 = +)/P(T_1 = +)$

While we have the first two terms necessary (from our given information), we do not currently have $P(T_1 = +)$. We will need to calculate this as well. Recall that we can use the law of total probability to marginalize out a variable:

$P(T_1 = +) = P(T_1 = +, C_1 = +) + P(T_1 = +, C_1 = -)$

Although we do not have the joint probability of $T_1$ and $C_1$ directly, we can use the definition of conditional probability and substitute in values we do have:

$P(T_1 = +) = P(T_1 = + \mid C_1 = +)P(C_1 = +) + P(T_1 = + \mid C_1 = -)P(C_1 = -)$ 
$= 0.8*0.7 + 0.35*0.3 \approx 0.665$

Thus, we have two additional quantities to add to our list of known probabilities:

1. $P(T_1 = +) = 0.665$
2. $P(T_1 = -) = 0.335$

Now we can compute $P(C_1 = + \mid T_1 = +)$ (and consequently $P(C_1 = - \mid T_1 = +)$):

1. $P(C_1 = + \mid T_1 = +) = 0.8*0.7/0.665 \approx 0.842$
2. $P(C_1 = - \mid T_1 = +) = 0.158$


And thus:

$EU[C_1 \mid T_1 = +] = 0.842(-500+50) + 0.158(-500+700+50) \approx -339$

Now, since we are conditioning on having already performed the test, we need to compare with the exepected utility of car 2, given the outcome of the test:

$EU[C_2 \mid T_1 = +] = P(C_1 = + \mid T_1 = +)(cost + test) + P(C_1=-\mid T_1 = +)(cost + test + repair)$

However, since test 1 doesn't tell us anything about car 2, we know that $C_1$ is independent of $T_1$.[^2]
[^2]: This is an example of how belief or epistemic uncertainty impacts probabilities. We might think of both test accuracy and car quality as aleatory uncertainty due to, e.g., the randomness of flaws in the manufacturing process for the test or the randomness of part degredation for the car. However, when we are making decisions, we treat these random processes as our baseline beliefs about car quality. Although the probability that a random car is faulty might be due to a truly random process, our belief about its current state can be updated in light of new information &mdash; even though the test does not change anything about the mechanism that causes the car to be faulty. 

$EU[C_2 \mid T_1 = +] = P(C_2 = +)(cost + test) + P(C_2=-)(cost + test + repair)$ 
$= 0.8*(-250 + 20) + 0.2*(-250 + 150 + 20) = -200$

Now we want to choose the car that minimizes the expected cost ($min\{-339, -200\}$) and so we choose car 1. 

Remember that so far we have only computed the optimum choice for what car to buy under two conditions: no test and when test $T_1$ is +. In class we discussed how computing the case for $T_1 = -$ causes us to choose a different outcome: we decide to purchase car 2 when $T_1$ returns -. 

The homework assignment asks you to perform a similar process for car 2 and it asks you to compute the expected utility of each test. (i.e., $E[T_1]$ and $E[T_2]$). If you get stuck on this part, remember to enumerate the outcomes and their costs (which may be expected values) (e.g., there are only two possible outcomes for $T_1$: the case where it is positive and you choose car 1 and the case where it is negative and you choose car 2).
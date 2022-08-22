# Another way to think about aperiodicity

One of the concepts that students sometimes find confusing is what aperiodicity means in the context of Markov Chains: while it has to do with cycles in the transition graph, the presence of a cycle does not make a Markov chain periodic. However, the lack of cycles does make a Markoc chain aperiodic trivially &mdash; no cycles entails that the transition matrix cannot be irreducible. 

## Aperiodicity, formally

A Markov Chain is _periodic_ iff there is at least one state such that, for some t > 1, we can only visit that state every t steps. We can express this using first order logic like so:

$\exists s \exists t \forall c (t > 1 \wedge P(X_{tc} = s) > 0 \wedge \forall n (n \mod t \not= 0 \rightarrow P(X_n = s) = 0)$

When this statement is satisfied, we say that the chain is periodic; its negation defines _aperiodicity_. Note that technically we also typically define periodicity in terms of an intial $k$ steps, saying that after $k$ steps the chain is periodic or aperiodic. We also typically define aperiodicity in terms of a starting state. 

## What aperiodicity really gives you

Aperiodicity is a property over the set of possible paths; it's really about your ability to sample. If a Markov chain is aperiodic, then after some initial period $k$, the probability of observing any of the possible states at time n $k+n, n > 0$ should be greater than one. So, even if a particular path has repeated structure and only visits a state every $t$ steps, another path could. 

One way you can informally verify this is to draw a branching structure for each possible state we can visit. 

```      
s1 ----> s2
  <______/
```

This is where the start state is important: if we condition on starting in state s1, the chain is periodic, where $t=2$. We can see this trivially because there is only one path out of each state. If we can drop into any state, then we can observe either s1 or s2 at any time step. However, we care about our ability of an arbitrary random walk to be able to access any state at some time $k+n$. Most applications of Markov chains (and indeed, MDPs) do not allow us to start at arbitrary states (in fact, if we could do that, things would be a lot easier!). 

Now, we saw that when we add a self-loop to an irreducible Markov chain, we get aperiodicity, since we can stay in a state for any number of steps, which allows us to visit all reachable states at any time (and they are all reachable, since the chain is irreducible!):


```      
            ____
           /    \
s1 ----> s2<----/
  <______/
```

We then saw an example of a chain where we had two connected loops:

```      
s1 ----> s2 ---> s3 ----> s4
  <______/        <______/
```

This Markov chain is not irreducible, so we generally don't care about it, since there are states we will never visit, but it's also periodic, since once we get stuck in nodes (s3, s4), we visit each state with a period of 2. Note that we can visit s3 at any time step after $k=2$.

Let's update the chain again:

```      
s1 ----> s2 ---> s3 ----> s4
  <______/ <_____/ <_____/
```

We can expand the nodes reachable at any step from s1 to see whether a pattern emerges at each time step.
In our diagram below, we merge nodes when it is convenient to do so (it has no special semantics and merely reduces redundancy at each time step:

```
0    1  2  3  4  5  6
                            
        s1    s1    s1 ...
       /  \  /  \  /
s1 - s2    s2    s2
       \  /  \  /  \
        s3    s3     s3 ...
          \  / \   /
           s4    s4
```

It should be clear that after $k$ = 1, all states have a period of 2. You can see in simulation for the Example 1 tab in this [Google sheet](https://docs.google.com/spreadsheets/d/1vPEhaQ97wZBRIS2AO-8_bGAmfNj-_VNqbHd6JLWpi6M/edit?usp=sharing) that every 
state has a non-zero probability of being visited every 2 steps.

Now let's try another example:
```
  _______________________
 V                       \
s1 ----> s2 ---> s3 ----> s4
  <______/        <_____/
```

Here is this example's expansion of states:

```
0    1    2    3    4    5 
                       
                    s1 - s2 ...
                  /
          s3 - s4
        /         \
s1 - s2             s3 - s4 ...
        \         /
          s1 - s2
                  \
                    s1 - s2 ...
```

Once again, our chain is periodic with a period of $t=2$, which can be verified in the linked spreadsheet above. 

Now let's see what happens when we change the target of one of the arrows:

```
           ______________
          V               \
s1 ----> s2 ---> s3 ----> s4
  <______/        <_____/


0    1    2    3    4    5    ...

                    s1 - s2   ...
                  /
          s1 - s2
        /         \
s1 - s2             s3 - s4   ...
        \         /
          s3 - s4        s1   ...
                  \    / 
                    s2 
                       \ 
                         s3   ...
```

We can see this reflected in the spreadsheet for Example 3: after the fifth step, we have a nonzero probability of being in each state.

Finally, note that if you play around with the starting state probabilities (row 7), you can obtain nonzero probabilities of being in each state very quickly. Aperiodicity is _not_ defined in terms of the start state distribution, since by definition if you can start sampling from anywhere, you wouldn't need MCMC in the first place! Instead, aperiodicity is defined in terms of the _transition probabilities_ with respect to specific states. For larger state systems, you can see this via the transition matrix taken to the $t^{th}$ power -- there will be a cluster of states with non-zero probabilities at these time steps that will have transition probabilities of 0 at the $(t+m)^{th}$ state, where $m \mod t \not= 0$.

# Inference rules
_Resources and clarifications_

Today in class, we discussed inference rules in natural deduction. There are some excellent resources out there but this [chart can be helpful](inference_rules.jpg). The sections from the Lean theorem prover book on natural deduction for [propositional](https://leanprover.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html) and [first-order predicate](https://leanprover.github.io/logic_and_proof/natural_deduction_for_first_order_logic.html) appear clear and useful, but I have not investigated them closely.

In any case, most of the inference rules are fairly self-explanatory, but the rules for or-elimination can be tricky.

Suppose we _have_ $F \vee G$. To be very clear, let's suppose we have some sequent $F\vee G, H \vdash F$. How do we get $F$ out? Well, to do this we need two proofs: a proof of $F$ _and_ a proof of $G$. Our scoping would look like so:

```
     |================================================================|
2.   | F \/ G                                                         | 
3.   | H                                                              | 
     |----------------------------------------------------------------|
     | |==============================================================|
4.   | | assume F                                                     | 
     | |--------------------------------------------------------------|
5.   | | F (trivially)                                                | 
     | |==============================================================|
     | |==============================================================|
6.   | | assume G                                                     | 
     | |--------------------------------------------------------------|
7.   | | ...proof steps, possibly using information from (2, 3)       |
n.   | | derive F                                                     |
     | |==============================================================|
n+1. | F by or-elmination (2, 5, n)                                   |
     |================================================================|
```

Now, this particular example is trivial, but it illustrates the main issue of why you need two proofs &mdash; when we assume $F$, we open a new scope. We can't let our assumption that $F$ is true escape the scope and therefore we can't use it outside the scope. The way or-elimination works is that you must provide a proof of the goal (here, $F$) under each of the assumptions that $F\vee G$ is true, in order to use either one at will. This might be easier to understand if our goal were some new formula instead: $F\vee G, H \vdash J$. Then we would have:

```
     |================================================================|
2.   | F \/ G                                                         | 
3.   | H                                                              | 
     |----------------------------------------------------------------|
     | |==============================================================|
4.   | | assume F                                                     | 
     | |--------------------------------------------------------------|
5.   | | ...proof steps, possibly using information from (2, 3)       |
n.   | | J                                                            |
     | |==============================================================|
     | |==============================================================|
n+1  | | assume G                                                     | 
     | |--------------------------------------------------------------|
n+2. | | ...proof steps, possibly using information from (2, 3)       |
m.   | | J                                                            |
     | |==============================================================|
m+1. | J by or-elmination (2, 5, n)                                   |
     |================================================================|
```
Perhaps this is more intuitive because the addition of $J$ decouples the proof from each new assumption (4, n+1). In any case, the smallest possible value of $J$ is going to be one of $F$ or $G$. 

There are two other observations worth meditating on: 

1. We cannot discharge either of $F$ or $G$ without more information &mdash; that is, unlike and-elimination, we don't get to just pick one of the two. This is why I had included $H$ above.

2. The scopes of the two assumptions (lines 4 through n and lines n+1 through m+1) are non-overlapping, so none of the information inside one can be used inside the other. This is why at step n+2, we can use information from lines 2 or 3, but not 4 through n. 
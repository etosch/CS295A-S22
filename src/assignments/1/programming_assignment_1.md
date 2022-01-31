# Programming Assignment 1: Logic

Undergraduates will [implement some of the algorithms](#implementing-algorithms) used to support logic programming. Graduate students have the additional option of [using existing logic programming tools](#using-exisiting-tools) for a task. 

## Implementing algorithms

For this assignment, you will implement the resolution algorithm for first order logic over a mini Prolog-like langauge. Prolog is a logic programming language that has a long history of use in AI. Prolog is  _declarative_, i.e., you tell it _what_ you want it to do, not _how_ to do it. The mini language is written as a Python library, so you don't need to do any additional parsing or learn Prolog syntax. 

At present, the core language supports user-defined predicates, but not functions or constants. It supports free variables. 

Suppose you create a predicate for course pre-requisites in the major:

```
PreReq = Predicate(2, "PreReq")
```

You can add pre-requisites like so:

```
PreReq.fact("Math21", "Math22")
```
This states that Math21 is a pre-requisite for Math22. The statement of fact adds "Math21" and "Math22" to the universe. We can now do things like assert this fact by evaluating the expression against the universe and using Python's built-in `assert` command on the result:

```
sat, _ = PreReq("Math21", "Math22").interpret()
assert sat
sat, _ = ~PreReq("Math21, "Math21").interpret()
assert sat
```

Note that the second assertion is only true because we haven't added `PreReq.fact("Math21", "Math21")` to our knowledge base &mdash; that is, it is false because it doesn't check against what we know, not because a course inherently cannot be a pre-requisite of itself. Remember: `PreReq` is just an arbitrary predicate to the code; it knows nothing special about its inherent qualities. Let's tell tell the system this fact, which is generally known as the _anti-reflexive_ property. This property can be expressed for our predicate `PreReq` as $\forall x (\neg P(x, x))$. We can express this in code like so: 

```
Forall.fact("x", ~PreReq("x", "x"), name="anti-reflexivity")
```

This command registers the anti-reflexivity of pre-requisites in the `knowledge_base` global variable. `Forall.fact` takes an optional argument for the name of the fact, but this isn't strictly necessary. 

When a fact is registered in the knowledge base, it is immediately evaluated to ensure that it is consistent with things we already know to be true. We haven't registered any facts that violate the anti-reflexivity property, so things are okay. 

If, however, we wanted to encode that pre-requisites are _transitive_ ($\forall x\forall y\forall z (P(x,y) \wedge P(y, z)\rightarrow P(x,z)$), we would express it like so:

```
Forall.fact("x", Forall("y", Forall("z", (PreReq("x", "y") & PreReq("y", "z")) > PreReq("x", "z") ))
```

Unfortunately, when we go to register this fact, it raises an error saying that the fact is inconsistent. This is because while we have values that make the premises true &mdash; Math 21 is a pre-req for Math 22 and Math 22 is a pre-req for Math 121 &mdash; we do not have `PreReq("Math21", "Math121")` registered as a fact. We can remedy this by augmenting our interpretation to ensure that these predicates hold:

```
for (x, y1) in PreReq.get_satisfying():
    for (y2, z) in PreReq.get_satisfying():
        if y1 == y2:
            PreReq.fact(x, z)
```

Now, maybe this isn't information you actually want in your knowledge base. For example, perhaps you came in with transfer credits or got a waiver to take Math 22 without having to taked Math 21. Such decisions are part of the "knowledge engineering" task. 


Now, every time we want to see if a formula holds with respect to our universe, we call `interpret` on it. Interpret loops through all of the elements of the universe for each term (here only arguments to predicates). If the universe were very large, we could see how this would become very inefficient very quickly. Furthermore, we know that there are some formulas that are unsatisfiable. Imagine if we tried to include in our knowledge base a fact that is a contradiction, but we couldn't recognize it as a contraction from its surface sting alone. Then we would be wasting time updating the wrong part of our knowledge base!

You task is to implement an alternative approach: resolution. Resolution is an algorithm that tests for the satisfiability of predicate formulas, without knowing anything about the universe.



<!-- ### Write a function that tests whether formulas have the correct form

This will get you warmed up working with the library. Implement the function `check_form` in file `programming_assignment_1.py`. This function should check for the following features:

1. No existential quantifiers.
2. No free variables. 
3. All quantifiers should appear at the beginning of the formula. This means that $\forall x \forall y (P(x, y) \wedge Q(x,y))$ should pass, but $(\forall x \forall y P(x,y)) \wedge \forall x \forall y Q(x, y)$ should not.
4. In the body of the formula (i.e., after the quantifiers, provided the above conditions are met)[^1], check that it is in conjunctive normal form:

    a. Negation can be applied to atomic formulas (here, just predicates).
    b. The formulas has a maximum depth of 2 such that it can be represented by an expression of the form $C_1 \wedge \ldots \wedge C_n$ where each $C_i$ has the form $p_1 \vee \ldots \vee p_m $ and each $P_j$ is a predicate of arity 0, 1, or 2, applied to the appropriate arguments. 

The logical connectives ($\wedge$ and $\or$) are at most binary, but clauses may have up to $k$ arguments. This means that there are _multiple parse trees_ for how to represent a single clause. For example, $\neg P_1(x) \vee \neg P_2(x) \vee P_3(x)$ could be encoded as `_Or(P1, _Or(P2, P3))` or `_Or(_Or(P1, P2), P3))` and still have the same surface string. You are allowed to assume a _normalized_ representation without having to write a normalization function, but you must write down what that representation is in the Python notebook so that we know your assumptions when grading. I recommend making the right branch _heavy_, i.e., the first encoding (`_Or(P1, _Or(P2, P3))`), where the greater depth is to the right.

_You do not need to convert the input to the correct form._ -->

### Implement resolution

Implement the function `resolution` in `programming_assignment_1.py`. This function operates on formulas that have following features:

1. No existential quantifiers.
2. No free variables. 
3. All quantifiers should appear at the beginning of the formula. This means that $\forall x \forall y (P(x, y) \wedge Q(x,y))$ is in the correct form, but $(\forall x \forall y P(x,y)) \wedge \forall x \forall y Q(x, y)$ is not.
4. In the body of the formula (i.e., after the quantifiers, provided the above conditions are met), check that it is in conjunctive normal form:

    a. Negation can be applied to atomic formulas (here, just predicates).

    b. The formulas has a maximum depth of 2 such that it can be represented by an expression of the form $C_1 \wedge \ldots \wedge C_n$ where each $C_i$ has the form $p_1 \vee \ldots \vee p_m$ and each $p_j$ is a predicate applied to the appropriate arguments. 


Any formula can be converted to have this form. However, for convenience we will be operating over sets of sets of predicates or their negation variables, where we expect to have at most one positive predicate in each clause. So, we will use the representation:

```
cnf = {{PreReq("x", "y"), ~PreReq("y", "x"), ~PreReq("z", "y")}, \
       {~PreReq("x", "y"), ~PreReq("y", "x")}, \
       {PreReq("y", "x"), ~PreReq("x", "w"))}, \
       {PreReq("z", "y")}, \
       {PreReq("y", "x")}
       }
```

to mean 
```
Forall("x", Forall("y", Forall("z"), Forall("w", \
    (PreReq("x", "y") | ~PreReq("y", "x") | ~PreReq("z", "y")) & 
    (~PreReq("x", "y") | ~PreReq("y", "x")) &
    (PreReq("y", "x") | ~PreReq("x", "w")) &
    PreReq("z", "y") &
    PreReq("y", "x")
    )))
```

Note that we could have any number of predicates in our CNF formula. We only show `PreReq` here because it is the only one we have defined so far.

The goal of resolution is to show that a formula is unsatisfiable, without having to evaluate against a reference universe. We can do this by combining two clauses such that one has the positive form of an atomic formula and the other has the negative form, removing the literals. For example, the first two clauses above can be combined because the first contains `PreReq("x", "y")` and the second contains `~PreReq("x", "y")`, so the combined clause is `{~PreReq("y", "x"), ~PreReq("z", "y")}`. This clause is then added to the total set of clauses:

```
cnf.add({~PreReq("y", "x"), ~PreReq("z", "y")})
```
The goal is to iterate over the set, combining clauses in this manner until we derive the empty set. The empty clause/set is evidence that the formula is unsatisfiable. 

For this example, we can derive the empty set following the above algorithm because the variables in the arguments all agree. However, because the CNF formula is universally quantified, these must hold for all bindings to the variables, and some variables could be equal to each other. We can simulate this _without knowing anything about the universe_ by _grounding_ the predicate with  elements. For example, we could ground the second clause, which we will refer to as $C_2$ `{~PreReq("x", "y"), ~PreReq("y", "x")}` by setting all variables equal to some term $a$: `{~PreReq(a, a), ~PreReq(a, a))}` and then grounding the fourth clause, which we will refer to as $C_4$ with the same variable, so `{PreReq("z", "y")}` becomes `{PreReq(a, a)}`. We then just combine $C_2$ with $C_4$ twice to derive the empty set. 

While this may not seem like much, grounding can be used to substitute arbitrary function outputs as well &mdash; critically this means that you do not need to know anything about the function in order to reason about the satisfiability of the formula! Since the core language currently does not implement functions, you will not have to reason over them.

_**WARNING**: you cannot remove more than one atomic formula for each step of resolution._

### Load in data

The examples here are for course pre-requisites, but you could set your universe to be anything you like. 

For this part of the assignment, you will need to add facts and items to your universe. Your universe should have at least 50 items in it and you should be using at least 3 predicates. Be sure to comment your code. 

Show your work in the Jupyter notebook.

### Create test data and compare

Create 10 test unsatisfiable formulas and compare how long it takes to show that they are unsatisfiable against the built-in `interpret` function. You may compare according to a metric of your choosing, but you must justify it. For example, you may wish to report on average wall-clock time over some $n$ trials, or you may wish to compare the size of the resolution set vs. number inputs tested. 

Show your analyses in the Jupyter notebook. If you create auxiliary functions for e.g., generating test data, put that in `programming_assignment_1.py`.


### Warning
I strongly recommend doing any development in the Jupyter notebook. Because notebooks are stateful and because you can execute them out of order, they can lead to a lot of headaches. Instead, view them as demonstrations of your work and note that we will be grading the homework assignments by interacting with the notebook. 

## Using existing tools

This is a more open-ended assignment and is only open to graduate students. If you are working on a research project that involves the content of this course, you may choose to link each of the programming assignments together as milestones in a single project. 

For this first milestone, your task should be to encode some part of a problem such that it can be manipulated using an SMT solver, such as z3. For your assignment, hand in a report that defines your problem, states why an SMT solver is necessary, and demonstrates that you have successfuly applied the SMT solver to at leaset a small subset of the problem space. 

## FAQ

* **Can I change the code?** Sure, go nuts. The purpose of these assignments is to get you to engage with the concepts. The starter code is just that. The only requirement is that you code against the API for the purposes of grading via the Python notebook. If Michael can't grade your work, then you get a grade of 0. 

* **Can I code in a different language?** No. Poor Michael has to grade all of these and I only have 10 hours of his time per week, so we need to use that time effectively! 

* **I noticed problem X/Y/Z. Can you add tests to your code?** 
Writing tests is a _great_ way to familiarize yourself with new code. I welcome any contributions in terms of tests or corrections via pull requests. 
Unfortunately, I am simply not paid enough to _not_ debug my code in production, so we have what we have. 

<!-- [:^1] This is often referred to as the _matrix_ of the formula, i.e., if $F$ is quantifier-free and $ G = \forall x_1 \cdots \forall x_n F$ such that there are no variables in $G$, then $F$ is the matrix of $G$. -->
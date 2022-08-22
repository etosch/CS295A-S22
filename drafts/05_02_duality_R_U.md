# Duality of R and U

In our lectures on LTL, we discussed how R and U are _duals_ of each other, i.e. $\phi_1 R \phi_2 = \neg (\neg \phi_1 U \neg \phi_2)$. Recall the definitions of R and U:

$\phi_1 U \phi_2 \triangleq \exists i (\pi^i \models \phi_2 \wedge \forall j (j < i \rightarrow \pi^j\models \phi_1))$
$\phi_1 R \phi_2 \triangleq \forall k (\pi^k\models\phi_2) \vee \exists j ( \pi^j\models \phi_1 \wedge \forall i ( i\leq j \rightarrow \pi^i\models\phi_2))$

Since $R$ is defined such that $\phi_1 R \phi_2 = \neg (\neg \phi_1 U \neg \phi_2)$ holds, we should be able to derive $R$ from $U$. That is, we should be able to show:


$\neg (\neg \phi_1 U \neg \phi_2) = \neg \exists i (\pi^i \models \neg \phi_2 \wedge \forall j (j < i \rightarrow \pi^j\models \neg \phi_1))$

$\quad\quad\quad\quad\quad~~= \ldots$

$\quad\quad\quad\quad\quad~~= \forall k (\pi^k\models\phi_2) \vee \exists j ( \pi^j\models \phi_1 \wedge \forall i ( i\leq j \rightarrow \pi^i\models\phi_2))$

First we rewrite the implication in $\neg \exists i (\pi^i \models \neg \phi_2 \wedge \forall j (j < i \rightarrow \pi^j\models \neg \phi_1))$ as a disjunction:

$\neg \exists i (\pi^i \models \neg \phi_2 \wedge \forall j (\neg (j < i) \vee \pi^j\models \neg \phi_1))$

We can also rewrite each instance of $\pi\models\neg\phi$ as $\neg (\pi\models\phi)$:

$\neg \exists i (\neg(\pi^i \models  \phi_2) \wedge \forall j (\neg (j < i) \vee \neg(\pi^j\models \phi_1)))$

We can then use deMorgan's to rewrite the disjunction of negations as a negation of a conjunction (i.e., $\neg A \vee \neg B \equiv \neg (A \wedge B)$):

$\neg \exists i (\neg(\pi^i \models  \phi_2) \wedge \forall j \neg ((j < i) \wedge (\pi^j\models \phi_1)))$

We can then use deMorgan's for quantifiers to further extract the negation: 

$\neg \exists i (\neg(\pi^i \models  \phi_2) \wedge \neg \exists j ((j < i) \wedge (\pi^j\models \phi_1)))$

Now we again apply deMorgan's, this time to a conjunction of negations to produce a negation of a disjunction:

$\neg \exists i \neg ((\pi^i \models  \phi_2) \vee \exists j ((j < i) \wedge (\pi^j\models \phi_1)))$

We then apply deMorgan's for quantifiers again:

$\neg\neg  \forall i ((\pi^i \models  \phi_2) \vee \exists j ((j < i) \wedge (\pi^j\models \phi_1)))$

Double negation: 

$\forall i ((\pi^i \models  \phi_2) \vee \exists j ((j < i) \wedge (\pi^j\models \phi_1)))$ 

Now we note that the existential quantifier distributes over disjunction (not that the term we are extending its scope over has any existentially quantified terms anyway!):

$\forall i\exists j ((\pi^i \models  \phi_2) \vee ((j < i) \wedge (\pi^j\models \phi_1)))$ 

We can then apply the distributive property to obtain:

$\forall i\exists j ((\pi^i \models  \phi_2) \vee (j < i)) \wedge ((\pi^i \models  \phi_2) \vee (\pi^j\models \phi_1)))$ 

For funsies, let's rewrite that first disjunction as an implication:

$\forall i\exists j ((j \geq i \rightarrow \pi^i \models  \phi_2) \wedge ((\pi^i \models  \phi_2) \vee (\pi^j\models \phi_1)))$ 

Now let's distribute that implication:

$\forall i\exists j (((j \geq i \rightarrow \pi^i \models  \phi_2) \wedge (\pi^i \models  \phi_2)) \vee ((j \geq i \rightarrow \pi^i \models  \phi_2) \wedge \pi^j\models \phi_1)))$ 

Let's distribute the existentially quantified variable, rewrite the inequality, and apply some symmetry:

$\forall i \Big(\exists j \big((j \geq i \rightarrow \pi^i \models  \phi_2) \wedge (\pi^i \models  \phi_2)\big) \vee \exists j \big(\pi^j\models \phi_1 \wedge (i \leq j \rightarrow \pi^i \models  \phi_2) \big)\Big)$ 

We've taken the expression as far as syntactic rewriting will allow us. Now we need to reason over what these terms actually mean. Let's start with the first term: $(j \geq i \rightarrow \pi^i \models  \phi_2) \wedge (\pi^i \models  \phi_2)$. We don't have any restrictions on the existentially quantified $j$; we just need a $j$ to exist. We did not include the universe that our $i$s and $j$s are quantified over, but we know that they must be from the set $\{1, \ldots, |\pi|\}$, since $\pi^j$ and $\pi^i$ must evaluate to something. Since $i$ and $j$ are drawn from the same set, we can existentially quantify $j$ with whatever we want and the outcome will be the same: $\pi^\models \phi_2$ holds. Thus we can rewrite this expression as:

$\forall i \Big(\pi^i \models  \phi_2 \vee \exists j \big(\pi^j\models \phi_1 \wedge (i \leq j \rightarrow \pi^i \models  \phi_2) \big))$

Now we are going to reason by cases. We are going to need to think about scope, so let's write this out using natural deduction:

$\forall i \Big(\pi^i \models  \phi_2 \vee \exists j \big(\pi^j\models \phi_1 \wedge (i \leq j \rightarrow \pi^i \models  \phi_2) \big)\Big)\vdash \forall k (\pi^k\models\phi_2) \vee \exists j ( \pi^j\models \phi_1 \wedge \forall i ( i\leq j \rightarrow \pi^i\models\phi_2))$

1. $\forall i \Big(\pi^i \models  \phi_2 \vee \exists j \big(\pi^j\models \phi_1 \wedge (i \leq j \rightarrow \pi^i \models  \phi_2) \big)\Big)$ (Given)
2. instantiate $i$ as $i_0$
    2. $\pi^{i_0} \models  \phi_2 \vee \exists j \big(\pi^j\models \phi_1 \wedge (i_0 \leq j \rightarrow \pi^{i_0} \models  \phi_2) \big)$ ($\forall_e$, 2)
    3. Assume left disjunction of (a)
        1. $\pi^{i_0} \models  \phi_2$ ($\vee_e$, 2.a)
        2. $\pi^{i_0} \models  \phi_2 \vee \exists j ( \pi^j\models \phi_1 \wedge \forall i ( i\leq j \rightarrow \pi^i\models\phi_2))$ ($\vee_i$, 2.b.i)
    4. Assume right disjunction of (a)
        1. $\exists j \big(\pi^j\models \phi_1 \wedge (i_0 \leq j \rightarrow \pi^{i_0} \models  \phi_2) \big)$ ($\vee_e$, 2.a)
        2. instantiate $j$ as $j_0$
            1. $\pi^{j_0}\models \phi_1 \wedge (i_0 \leq j_0 \rightarrow \pi^{i_0} \models  \phi_2)$ ($\exists_e$. 2.c.i)
            2. $\pi^{j_0}\models \phi_1$ ($\wedge_e$, 2.c.ii.i)
            2. $i_0 \leq j_0 \rightarrow \pi^{i_0} \models  \phi_2$ ($\wedge_e$, 2.c.ii.i)
            2. $i_0 > j_0 \vee \pi^{i_0} \models  \phi_2$
2. 
$\forall k (\pi^k\models\phi_2) \vee \exists j ( \pi^j\models \phi_1 \wedge \forall i ( i\leq j \rightarrow \pi^i\models\phi_2))$

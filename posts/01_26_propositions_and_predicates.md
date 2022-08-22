
# Introduction to Propositions and Predicates


## Recap of Propositions:

For the purpose of propositional logic, **propositions** are (almost) atomic black-boxes:
They have _names_ and _definitions_, but their names are just atomic symbols in the logic syntax,
and their definitions are _outside_ the logic syntax (usually these are statements in a human language).

The set of all propositions, together with the special symbols ⊤ and ⊥,
are the atomic symbols of the syntax of **formulas**.
The connectives will be familiar from their roles as boolean operators: ¬, ∧ ,∨, →, _etc_.
Thus, formulas are recursive trees with connectives as nodes and atomic symbols as leaves. 

There are two truth values: 1 and 0.
(These are not part of the syntax of formulas.)
These can go by other names, commonly _"true"_ and _"false"_.
The properties and isomorphisms of [Boolean Algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
are all good fun, but for now we can simply take **truth values** ≜ {1, 0}.

The operator **⟦·⟧** maps formula to truth values; _e.g._ ⟦⊤⟧=1.
(This example is actually part of the definition of ⟦·⟧;
⊤ and ⊥ are given meaning respectively as an atomic tautology and an atomic contradiction.)
Although it's often left implicit, it technically has a subscript argument,
either an **assignment** (a set of (_proposition_, _truth value_) pairs)
or a pair (_KB_, σ) of a **knowlege base** (a list of statements of the same form as proposition definitions)
and a **storage** of proposition definitions.
In either case, ⟦·⟧₋ can be implemented in terms of lookups and if-then-else statements. 


## Predicates as Relations:

Consider the category _B_ of truth values, and whatever category _S_ of nouns/subjects.
A single proposition (_e.g._ _p_≜`"Six is prime."`) can be represented as a pair of form 
(_s_∈_S_, _R_) where _R_ is a [relation](https://en.wikipedia.org/wiki/Binary_relation) over _S_ and truth values
(_e.g._ (6, _IsPrime_)). 
Rather than writing it as a tuple "(_s_, _R_)", we can instead write it as "_R_(_s_)", which is the normal notation. 

Not any relation _R_⊆_S_⨯_B_ will serve in the representation of a proposition!
It must be a **predicate**\*, a relation mapping _every_ element of _S_ to exactly one truth value.
We use the notation _F_(_s_)≜(_s_,1)∈_F_,
and we deliberately reuse the "¬" symbol to write ¬_F_(_s_)≜(_s_,0)∈_F_.

<sub>\* Here we consider only _unary_ predicates.
_Nullary_ predicates are the same as propositions.
Higher-artiy predicates are also possible.
Also, it's not clear if predicates really have to be _total_ functions; if you know know please share!
</sub>

In the context of a relational representation of predicates and propositions,
we can introduce **quantifiers**.

> Universal Quantification:  ∀_s_∈_S_ (_P_(_s_)) ≜ {(_s_,1) | _s_∈_S_} ⊆ _P_  
> Existential Quantification: ∃_s_∈_S_ (_P_(_s_)) ≜ ∅ ≠ {(_s_,1) | _s_∈_S_} ∩ _P_

Typically the element-hood restriction on _s_ is omitted, and _S_ is assumed to be the domain of _P_,
but quantification over subsets of the domain is fine. 
In particular, notice that ∀_s_∈∅ (_P_(_s_)) is a tautology and ∃_s_∈∅ (_P_(_s_)) is a contradiction, regardless of _P_.


## Predicate Logic Syntax:

In the prior section we introduced the notions and notations of predicates and quantifiers;
here we introduce a formal syntax for them. 
While in the prior section we gave predicates meaning as relations, and gave quantifiers meaning in terms of set-theory,
_here we will treat them as pure symbols_.
They'll get (possibly contextual) meanings again later when we define a semantics.

Predicates compose into formula just like propositions do. 
This is what that looks like in BNF:

| patterns | forms    | notes |
|----------|:---------|:--------|
| _x_      |          | Variables (from some set of identifiers) |
| _P_      |          | Predicates (from some set of identifiers) |
| _F_      | ⊤ ⏐ ⊥ ⏐ _P_(_x_) <br/> ¬_F_ ⏐ _F_∧_F_ ⏐ _F_∨_F_ ⏐ _F_→_F_ <br/> ∀_x_ (_F_) ⏐ ∃_x_ (_F_) | Atomic formula (could also include nullary predicates) <br/> Connectives borrowed from Propositional syntax <br/> Quantifiers |

Not inherent in the BNF, but fundamental to understanding predicate logic formula,
are the ideas of **free variables** and **bound variables**.
In the formula ∀_x_ (_F_), we say "_x_ is **bound** (_by that specific quantifier node_) in _F_";
usually we're only interested this if _x_ actually appears in _F_.
(Existential quantifiers bind variables the same way.)
If _x_ appears in some _F_ and is not bound by any quantification node in _F_, then we say "_x_ is **free** in _F_".
Specifically, _an appearence of x_ may be free; it is possible to have both free and bound appearances of a variable in a single syntax tree. 

## Re-write rules:

As a first step toward a _semantics_ for predicate-logic syntax trees, we declare an equivalence relation (and therefor equivalence classes).
When we discussed propositional logic, we considered the (reflexive, symmetric, transitive) relation
_a_≡_b_ ≜ ⟦_a_⟧=⟦_b_⟧ _("for all suitable assignments")_.
Equivalence here is similar, we just haven't discussed ⟦·⟧ yet. 

Usually, we're interested in these equivalence classes because they define our re-write rules for formula:
if _F_≡_G_ then we can use _G_ anywhere we were using _F_. 

### Example:

This example from class shows re-write steps from one representation of the required property of a predicate into its usual presentation:

| Justification                 | formula |
|------------------------------:|---------|
| Start  ("_P_ is a predicate")           | ∀_f_ ∀_f'_ ∀_b_       ( (_f_=_f'_ ∧ (_f_,_b_)∈_P_) → ¬∃_b'_ (_b_≠_b'_ ∧ (_f'_,_b'_)∈_P_) ) |
| Distribute negation across existence   | ∀_f_ ∀_f'_ ∀_b_       ( (_f_=_f'_ ∧ (_f_,_b_)∈_P_) → ∀_b'_ ¬(_b_≠_b'_ ∧ (_f'_,_b'_)∈_P_) ) |
| Distribute negation across conjunction | ∀_f_ ∀_f'_ ∀_b_       ( (_f_=_f'_ ∧ (_f_,_b_)∈_P_) → ∀_b'_  (_b_=_b'_ ∨ (_f'_,_b'_)∉_P_) ) |
| Move quantifier up (no name conflicts!) | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ ( (_f_=_f'_ ∧ (_f_,_b_)∈_P_) →        (_b_=_b'_ ∨ (_f'_,_b'_)∉_P_) ) |
| Definition of implication               | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ (¬(_f_=_f'_ ∧ (_f_,_b_)∈_P_) ∨        (_b_=_b'_ ∨ (_f'_,_b'_)∉_P_) ) |
| Distribute negation across conjunction | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ ( (_f_≠_f'_ ∨ (_f_,_b_)∉_P_) ∨        (_b_=_b'_ ∨ (_f'_,_b'_)∉_P_) ) |
| Associativity of disjunction            | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ ( ((_f_,_b_)∉_P_ ∨ (_f'_,_b'_)∉_P_) ∨        (_f_≠_f'_ ∨ _b_=_b'_) ) |
| Factor out negation from disjunction    | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ (¬((_f_,_b_)∈_P_ ∧ (_f'_,_b'_)∈_P_) ∨        (_f_≠_f'_ ∨ _b_=_b'_) ) |
| Definition of implication               | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ ( ((_f_,_b_)∈_P_ ∧ (_f'_,_b'_)∈_P_) →        (_f_≠_f'_ ∨ _b_=_b'_) ) |

It's not clear that this example actually fits into the syntax as introduced. 
For the purpose of example, let's fix that. 
Our goal is to show the same sequence of re-writes, but at every step our formula should be a valid tree in our BNF.

First we'll extend our syntax to allow binary predicates.
Here "=" is just an atomic symbol in our grammar/syntax, in the set of all predicates. 
We'll use it as a binary predicate; if we had semantics or a more advanced grammar we would enforce that.
While we intuitively understand it to mean "equality", that idea is _not_ encoded in the syntax. 
Similarly, I here use the un-italicized P to refer to a _binary_ predicate "is a predicate", who's right-hand argument is a truth value,
but neither the semantics of P nor the idea of a truth value is encoded in the syntax.

| patterns | forms    | notes |
|----------|:---------|:--------|
| _x_      | f ⏐ f' ⏐ b ⏐ b'         | Variables (that we'll use) |
| _P_      | P ⏐ =                   | Predicates (that we'll use) |
| _F_      | ⊤ ⏐ ⊥ ⏐ _P_(_x_) ⏐ _x_ _P_ _x_ <br/> ¬_F_ ⏐ _F_∧_F_ ⏐ _F_∨_F_ ⏐ _F_→_F_ <br/> ∀_x_ (_F_) ⏐ ∃_x_ (_F_) | Add binary predicates <br/> No change <br/> No change |

And then we can proceed:

| Justification                 | formula |
|------------------------------:|---------|
| Start                                   | ∀_f_ (∀_f'_ (∀_b_        ( (_f_=_f'_  ∧  _f_ P _b_) → ¬∃_b'_ ( (¬_b_=_b'_  ∧  _f'_ P _b'_) ) ) ) ) |
| Distribute negation across existence   | ∀_f_ (∀_f'_ (∀_b_        ( (_f_=_f'_  ∧  _f_ P _b_) →  ∀_b'_ (¬(¬_b_=_b'_  ∧  _f'_ P _b'_) ) ) ) ) |
| Distribute negation across conjunction | ∀_f_ (∀_f'_ (∀_b_        ( (_f_=_f'_  ∧  _f_ P _b_) →  ∀_b'_ ( (¬¬_b_=_b'_ ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Remove double negation                  | ∀_f_ (∀_f'_ (∀_b_        ( (_f_=_f'_  ∧  _f_ P _b_) →  ∀_b'_ ( (_b_=_b'_   ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Move quantifier up                      | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (_f_=_f'_  ∧  _f_ P _b_) →          (_b_=_b'_   ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Definition of implication               | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ (¬(_f_=_f'_  ∧  _f_ P _b_) ∨          (_b_=_b'_   ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Distribute negation across conjunction | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (¬_f_=_f'_ ∨ ¬_f_ P _b_) ∨          (_b_=_b'_   ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Associativity of disjunction            | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (¬_f_ P _b_ ∨ ¬_f'_ P _b'_) ∨          (¬_f_=_f'_   ∨ _b_=_b'_) ) ) ) ) |
| Factor out negation from disjunction    | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ (¬(_f_ P _b_  ∧ _f'_ P _b'_)  ∨          (¬_f_=_f'_   ∨ _b_=_b'_) ) ) ) ) |
| Definition of implication               | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (_f_ P _b_  ∧ _f'_ P _b'_)  →          (¬_f_=_f'_   ∨ _b_=_b'_) ) ) ) ) |
| One more step for the fun of it         | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (_f_ P _b_  ∧ _f'_ P _b'_)  →          (_f_=_f'_   →  _b_=_b'_) ) ) ) ) |

The double-implication isn't excellent, it might read more clearly if we took a different route from the sixth line:

| Justification                 | formula |
|------------------------------:|---------|
| Sixth line from above                      | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ (   (¬_f_=_f'_ ∨ ¬_f_ P _b_)    ∨ (_b_=_b'_   ∨ ¬_f'_ P _b'_) ) ) ) ) |
| Associativity of disjunction               | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( ( (¬_f_ P _b_ ∨ ¬_f'_ P _b'_) ∨ ¬_f_=_f'_ ) ∨ _b_=_b'_ ) ) ) ) |
| Factor out negation from disjunction       | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( (¬(_f_ P _b_  ∧ _f'_ P _b'_)  ∨ ¬_f_=_f'_ ) ∨ _b_=_b'_ ) ) ) ) |
| Factor out negation from disjunction       | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ (¬( (_f_ P _b_  ∧ _f'_ P _b'_)  ∧  _f_=_f'_ ) ∨ _b_=_b'_ ) ) ) ) |
| Definition of implication                  | ∀_f_ (∀_f'_ (∀_b_ (∀_b'_ ( ( (_f_ P _b_  ∧ _f'_ P _b'_)  ∧  _f_=_f'_ ) → _b_=_b'_ ) ) ) ) |
| Cull parentheses (not technically allowed) | ∀_f_ ∀_f'_ ∀_b_ ∀_b'_ ( ( _f_ P _b_  ∧ _f'_ P _b'_  ∧  _f_=_f'_ ) → _b_=_b'_ ) |

Returning to our intuitive understanding of the nature of predicates,
we can see that this doesn't entirely capture the refinement of Relations that we want; P is not necessarily Total. 
We could express totality as

> ∀_f_ (∃_b_ (_f_ P _b_)

but that (combined with the above property) would just limit us to _functions_;
predicates must range over truth values. 
There are a few approaches we could take,
probably the easiest of which would be to associate variables _bT_ and _bF_ with "boolean true" and "boolean false". 
Then we could just say

> ∀_f_ (_f_ P _bT_ ∨ _f_ P _bF_)

Which suffices to get us a law-of-excluded-middle in this weird logic-inside-of-logic we've built. 


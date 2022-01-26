
# Introduction to Predicates


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
A single proposition (_e.g._ _p_​≜`"Six is prime."`) can be represented as a pair of form 
(_s_∈_S_, _R_) where _R_ is a [relation](https://en.wikipedia.org/wiki/Binary_relation) over _S_ and _B_
(_e.g._ (6, _IsPrime_)).

Not any relation _R_⊆_S_⨯_B_ will serve in the representation of a proposition!
It must be a **predicate**\*, a relation mapping _every_ element of _S_ to exactly one truth value.
We use the notation _F_(_s_)≜(_s_,1)∈_F_,
and we deliberately reuse the "¬" symbol to write ¬_F_(_s_)≜(_s_,0)∈_F_.

<sub>\* Here we consider only _unary_ predicates.
_Nullary_ predicates are the same as propositions.
Higher-artiy predicates are also possible.
</sub>

In the context of a relational representation of predicates and propositions,
we can introduce **quantifiers**.
(These will be re-introduced when we give predicate logic its own syntax.)

> ∀_s_∈_S_(_P_(_s_)) ≜ {(_s_,1) | _s_∈_S_} ⊆ _P_  
> ∃_s_∈_S_(_P_(_s_)) ≜ ∅ ≠ {(_s_,1) | _s_∈_S_} ∩ _P_

Typically the element-hood restriction on _s_ is omitted,
and _S_ is assumed to be the domain of _P_.

## Predicate Logic Syntax:

Predicates compose into formula just like propositions do. 

- We must assume both a set of **variables** 𝒱={_x_, _y_, _z_, ...}  
  and a set of predicates 𝓟 ≜ {_P_, _Q_, _R_, ...}.
- The set of atomic formula 𝓕 ≜ {⊤, ⊥}∪{_P_(_x_) | _P_∈𝓟 ∧ _x_∈𝒱).
- We may also have atomic formula for nullary predicates.
- All the connectives from propositional syntax are reused.
- Quantifiers are also connectives. _i.e._ for any _x_∈𝒱 and any _F_∈𝓕, ∀x(_F_)∈𝓕 and ∃x(_F_)∈𝓕.





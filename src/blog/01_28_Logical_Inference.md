
Two important qualifiers to learn: Universal and Existential. Universal in the context of predicates has symbol ∀ and means for all y 
that the Predicate P(y) evaluates to true. Existential has a symbol and means there exists a where the predicate P(y) evaluates to true.


In order to make some formulas more readable, substitution may be done so that all variables are not x. When we are substituting in such a fashion, 
we write A_[x/x_0](F) where x is the old variable name and x_0 is the new variable name. Note that we only replace free instances of x under this notation, 
where free denotes that x is not contained within a for all or exists statement 


Two formulas F and G are equivalent if they have the same truth value for all suitable structures, where a suitable structure if the interpretation function [*] 
is defined for every symbol in the universe. Essentially means that we can obtain some truth value for any query we could put in the interpretation function. 
Determining equivalence is easy when the formula is known, but very difficult when it is occluded, and thus info is only known by changing values of variables. 

One of the highlights in the lecture was the difference between pure logic and AI. Pure logic is searching for a universe to find some truth, whereas AI often assumes a Universe, 
and then seeks to find values or interpretation functions to make a formula true. 

Some new rules for predicate logic are an extension of demorgan laws for “for all” and for “there exists”. The negation of for all x P(x) is there exists x such that not P(x), 
and the negation of there exists x such that P(x) is for all x not P(x). as formulas, this is

Not ∀xP(x) =x not P(x)
Not xP(x) =∀x not P(x)

A key difference between propositional and predicate is that in predicate logic, we need to find a structure such that the mapping from the interpreted variables 
to the truth values makes the formula true. Whereas with propositional logic, one only needs to find values for the variables to make the formula true. 
With predicate logic, the focus is on the structure, whereas with propositional logic the focus is on the variables and their truth values. 

Before we dive deeper into inference rules in logic - we first want to differentiate between sequents and implications. In logic, sequents are defined that 
when all preceding conditions are true, then at least one of the following formulas is true. Conversely, implication is when the second proposition of a relationship 
is implied (or a consequence) from the first proposition. The professor importantly notes that we should think about a proof within logic as datum - a way that we can 
trace back and double check our reasoning for a problem.

Inference rules let us use previously defined information and combine it into new information - similar to that of an if-statement.


Inference Rules									Sequent Notation
And Elimination (Laymen terms - if we have two  	(P & Q ) |- P and(P & Q ) |- Q
propositions combined with an and, 
we can then derive P and Q

And Introduction(Laymen terms - If you 				P, Q |- P & Q
combine two propositions which are both true, 
then the conjunction of the two are considered true)

Or Introduction (Laymen terms - if proposition 		P |- P V Q
one is true, then either proposition one or 
proposition two has to be true)

Implication Elimination(Laymen terms - similar 		P → Q,  P |- Q
to an if-then statement in python 
in which P will imply Q.  

Bottom Elimination (Laymen terms - when comparing		⊥
 a proposition and a not-proposition leading to ⟂, 		-
 from there we can derive anything)						P




Not Elimination (Laymen terms - if proposition and 
its negation are true, then 						P ,not P →⊥
the statemnet is in itself false. More commonly
thought of as proof by contradiction)

Implication Introduction* (Laymen terms - 			P → Q,
we are to prove P → Q by assuming P and 
subsequently deducing Q from P)
 
Or Elimination* (Laymen terms - with two implications (P → Q), (R → Q), (P ⋁ R) ⊢ Q
(P to Q) or ( R to Q), if either P or R is true, 
then so must be Q

Not Introduction*(Laymen terms - 					(P → Q) ⋀  (P → ⅂Q) → ⅂P
start with P and get to contradiction
⊥ by showing not P)

* Require notion of scope

For more reliable information of Logic -  
Stanford has more lessons here: http://intrologic.stanford.edu/homepage/index.html

Some basic examples of rules of inference in context of AI 
https://www.javatpoint.com/rules-of-inference-in-artificial-intelligence
Some examples with 3 predicates
https://www.geeksforgeeks.org/mathematical-logic-rules-inference/

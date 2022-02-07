Setting the fundamentals for the rest of the semester - Monday’s class of CS295 Artificial Intelligence jumped quickly into some important concepts: 
Ontologies, propositions, knowledge, basis, connectives, and much more. This blog post, written by Matt Dierker and Preston Hunter, will aim to give you a quick, narrative-driven,
 recap of the content of class. If you have any questions or modifications that you would like added to this blog post - 
 please don’t hesitate to reach out to mdierker@uvm.edu or preston.hunter@uvm.edu.

The first concept that professor Tosch covered was that of of propositions and their inherit relation to the compositions of knowledge bases. 
Propositions, as defined within the class notes, are a singular, indivisible unit of data. For example: j ≜ “Matt is the roommate of Preston” or 
k ≜ “Preston dislikes using git”. Each of these sentences, similar to that of a variable definition within our code base, defines something that is inherently true. 
These propositions compromise the basis of a knowledge basis - is a form that aims to store our information. While in advanced AI, knowledge bases can become extremely large, 
attempting to capture large amounts of information for a program to iterate over, for our purposes this early on in the class we can consider it to be more similar 
to a list or dictionary. When we choose to access this stored data, we do so by either replacing propositions with their definitions or checking definitions against 
what we know (and have stored). Furthermore, for our classes purposed, we will abbreviate knowledge base as KB, simga/σ as a set of propositions, 
and our aforementioned ≜ as a  function to compare propositions (which returns a boolean). For more information on knowledge bases (KB) including relevant industry 
information, please follow the following link:
https://www.kmslh.com/blog/knowledge-base-in-ai-what-is-it-and-why-do-you-need-one/

Connectives are what join propositions together into formulas, which themselves are inductively defined.  The two most basic connectives, 
upon which all others can be defined, are negation and disjunction (or in other words OR). Other commonly used ones are conjunction (AND), and implication (->). 
For formulas F and G (F and G are elements of the set of propositions called atomic formulas), the below are also formulas
Negation: -F		-Conjunction: F and G
Disjunction: F or G 	- Implication: F->G


All propositions have a truth value of 0 or 1, and the function/assignment that maps from the propositions to their truth values {0,1} 
is A (Fancy A when written). Formulas are evaluated to truth values by assigning all of the atomic propositions their respective truth values, 
and then evaluating the effect/truth value of connectives on the propositions/truth values they connect.  



We can evaluate a formula in this manner, and we can make this simpler or more organized by breaking a formula down into subexpressions. E.G. 
P1 OR(P1 OR P2) has subexpressions (P1 OR P2) and P1

A helpful tool are truth tables, which for an arbitrary number of formulas, the truth value for every possible combination of truth values for the Formulas. 
A very helpful one is the one for formulas F and G, and the values for the connectives highlighted earlier


F|G|F and G| F or G| not F| F imply G
0 0|  0	   |  0	   |  1	  |  1
0 1|  0	   |  1	   |  1	  |  1
1 0|  0	   |  1	   |  0	  |  0
1 1|  1	   |  1	   |  0	  |  1

Sometimes we may come across a formula F (composed of other propositions by connectives) which always evaluates to 0 or 1 for its truth value, 
no matter the truth values for formulas that compose F. In this case F can be replaced with T if it is always 1 or ⊥ if it is always 0. 
These two special values/formulas we can add to our list of atomic formulas. 

The next thing that we defined was the conceptual idea of equivalence - meaning  the comparing of two formulas to determine if they are equivalent. 
In this concept, the formula is considered equivalent if and only if the return the same truth value for both the sides of formula. It is important to note that a 
suitable assignment must contain truth values for all of the included propositions. Professor Tosch notes that knowing how to compare these formulas will be imperative
to the rest of the course. For practice information, please review Wednesday’s (1/26) class notes and the iclicker equation of the day for today (1/24). 

To build upon the concept of equivalence within Artificial Intelligence, we should note that there are some scenarios that are used frequently enough where the they 
now have their own names. The first of these scenarios is known as a model, in which all possible values for a variable (A) is suitable or equal to 1 for another variable(F),
then we can say that A models F. This form is written as A |= F. Conversely, when there are not suitable assignments in which A |= F =1, then we would redefine this as 
F being unsatisfiable or a contradiction to A. If there is at least one instance in which A models F, then it’s listed as satisfiable.

Another concept that Professor Tosch discussed was that of Boolean Satisfiability, alternatively abbreviated as SAT. In SAT - we aim to find an assignment in 
which X is [[Y]]X = 1. In order to achieve SAT, three important things must occur. Firstly, we must Enumerate all possible assignments for Y, 
for all real numbers of X (X1, X2,X3…Xn). Additionally, for all values of Xi, ∈ all real numbers of X, when the model is satisfied, then return Xi. 
When there is not such assignments that exist, we must return unsatisfied or UNSAT. We can continue to build upon this concept in NP, specifically canonical NP-complete problems.  
When we define NP-complete - we are referencing problems in which we must use the same amount as computationally heavy NP problems, but not any more. 
These problems in particular can be checked in polynomial time. However, finding solutions may need to be found in exponential time - although the time may be reduced 
depending on use case.

Conjunctive normal form (CNF) is a way of rewriting formulas systematically suh that they are easier to perform the boolean satisfiability problem on. 
It involves rewriting all F->G as -F or G, then pushing all negations to atomic formulas and applying the distributive laws. Horn Formulas are in CNF and each clause 
has at most one positive atomic formula. Horn formulas have an efficient algorithm to solve the SAT problem for (Horn-SAT). 

One of the final concepts that we discussed in class was a comparison between complexity, algorithm, and Artificial Intelligence. 
Oftentimes we consider whether these types of problems would fall into the realm of artificial intelligence - and surprisingly, these are exactly the type of problems AI 
aims to solve. Firstly, when approaching these problems, it’s beneficial to categorize these problems into equivalence classes. 
Secondly, when approaching this from an algorithm perspective, we must aim to find a solution to model a problem instance that we will aim to recreate. 
Finally, we must focus that AI is typically aiming to work through complex boolean logic, thus returning primarily true/false results. 
The goal is to be able to build code that replicates common problems that we will encounter in the realm of work. Important to note that slower results and incorrect results 
are acceptable.

# Schedule

_This schedule is tentative and subject to change. It may be a bit ambitious._

[Supplmentary and optional background reading](syllabus.html#textbook) provided when appropriate. 

R&N == _Aritificial Intelligence: A Modern Approach_, Russell and Norvig, 3rd edition.

## References for Unit 1 (Logic)
For the unit on logic you may also want to consult:

* _Category Theory for the Sciences_, Spivak, [pdf](https://arxiv.org/pdf/1302.6946.pdf) 
* _Logic in Computer Science_, Huth and Ryan
* _Logic for Computer Scientists_, Schoening

Huth and Ryan is an excellent introductory text for temporal and epistemic logics, which we will touch on in Unit 3 (agent-based reasoning).

## References for Unit 3 (Agents: Belief and Time)

* _Advanced Data Analysis from an Elementary Point of View_, Part III, Shalizi, [pdf](https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/ADAfaEPoV.pdf)
* _Logic in Computer Science_, Huth and Ryan



| Date  | Topic  | Form  |  Deadlines & Notes |
|---:|---|---|---|
| Wed, Jan 19 | Intro: What is AI? | [Lecture](lectures/Lec1_Intro_AI.pdf) | |
| Fri, Jan 21 | Knowledge Representation | [Lecture](lectures/Lec2_Knowledge_Representation.pdf) | R&N: 12.1, 12.2<br/>[Set notation cheatsheet](https://www.maths.usyd.edu.au/u/UG/JM/MATH1901/r/PDF/cheat-sheet.pdf)<br/>[NSF Workshop: Research Challenges and Opportunitites in KR](https://corescholar.libraries.wright.edu/cgi/viewcontent.cgi?article=1217&context=cse) |
| Mon, Jan 24 | Propositional Logic | [Lecture](lectures/Lec3____Propositional_Logic.pdf) | **Add Deadline**<br/>R&N: 7.3  |
| Wed, Jan 26 | First Order (Predicate) Logic | [Lecture](lectures/Lec4____First_Order_Predicate_Logic.pdf) | **Theory Assignment 1 out** <br/> R&N 8.2 |
| Fri, Jan 28 | Logical Inference I | [Lecture](lectures/Lec5____Logical_Inference.pdf) | R&N 7.5 |
| Mon, Jan 31 | Review of Logical Inference | Michael Q&A | _No Teams broadcast today_ <br/> **[Programming Assignment 1](assignments/1/programming_assignment_1.html) out**|
| Wed, Feb 2  | Logical Inference II and Resolution | [Videos](https://youtube.com/playlist?list=PLy1dxKpUCh9iYTZir_k_ZpeTlDJW9A9bv) | **Theory Assignment 1 due (soft)** <br/> R&N 7.5, 9.5  |
| Fri, Feb 4  | Application: Law and Logic Programming | [Lecture](lectures/Lec7_Applications_Logic_AI_Law.pdf) | **Drop Deadline**<br/>**Theory Assignment 1 due (hard)** <br/> R&N 9.4|
| Mon, Feb 7  | Proofs as Planning and Intro to Search | [Lecture](lectures/Lec8_Planning_Intro_Search.pdf) | R&N 10.1, 10.2 |
| Wed, Feb 9  | Exam 1: Logic | Exam | |
| Fri, Feb 11 | Background: Discrete Probability Theory | Lecture | **Programming Assignment 1 due (soft)** |
| Mon, Feb 14 | **CANCELLED** |  ||
| Wed, Feb 16 | **CANCELLED** |  || 
| Fri, Feb 18 | Search Agents | [Lecture (Michael)](lectures/AI_M_Lecture1.pdf) | R&N 2.1-4| 
| Mon, Feb 21 | **President's Day** | **No Class** | |
| Wed, Feb 23 | Uninformed Search | [Lecture (Michael)](lectures/AI_M_Lecture2.pdf) | R&N 3.1-4 | 
| Fri, Feb 25 | In-Class Activity: Search | Lecture (Michael) || 
| Mon, Feb 28 | A* and Adversarial Search | [Lecture (Michael)](lectures/AI_M_Lecture4.pdf)| R&N 3.5-6, 5.1-3| 
| Wed, Mar 2  | Constraint Satisfaction Problems | [Lecture (Michael)](lectures/AI_M_Lecture5.pdf) | R&N 6.1-5 |
| Fri, Mar 4  | In-Class Actibity: CSP |  Lecture (Michael) || 
| Mon, Mar 7  | **Spring Recess** | **No Class** ||
| Wed, Mar 9  | **Spring Recess** | **No Class** ||
| Fri, Mar 11 | **Spring Recess** | **No Class** ||
| Mon, Mar 14 | AI Security Topics | Lecture (Michael)  ||
| Wed, Mar 16 | Uncertainty in States | [Lecture](lectures/Lec15_probabilistic_states.pdf) | R&N 12.1-4 | 
| Fri, Mar 18 | Queries and Partial Observability | [Lecture](lectures/Lec16_queries.pdf) | R&N 13.1-2 <br/> _We briefly discussed what a naive causal structure learning algorithm would look like. For a full treatment of constraint-based causal structure learning, see [Shalizi Ch. 25](https://www.stat.cmu.edu/~cshalizi/uADA/12/lectures/ch25.pdf)_|
| Mon, Mar 21 | Causal Graphical Models | [Lecture](lectures/Lec17_CGMs.pdf) | [Notebook exercises](code/cgms.html)<br/>[Actual notebook](code/cgms.ipynb) |
| Wed, Mar 23 | Modal Logics for Knowledge and Belief | [Lecture](lectures/Lec18_epistemic_logic.pdf) | [Modal Logic Playground](https://rkirsling.github.io/modallogic/)<br/>[DSL for belief programming with partial observability](https://dl.acm.org/doi/pdf/10.1145/3428268) |
| Fri, Mar 25 | Representing agent knowledge with $KT45^n$  | [Lecture](lectures/Lec19_epistemic_logic2.pdf)|[An Introduction to Logics of Knowledge and Belief](https://arxiv.org/pdf/1503.00806.pdf) | [ICAPS 2020 Tutorial on Epistemic Planning](https://www.youtube.com/watch?v=lmimHMB3X5M) |
| Mon, Mar 28 | Elementary Decision Theory | [Lecture](lectures/Lec20_decision_theory.pdf) | [Blog post](blog/03_31_decision_theory.html)|
| Wed, Mar 30 | Elementary Game Theory | [Lecture](lectures/Lec21_game_theory.pdf) |  R&N 17.5, 17.6<br/>[Epistemic Game Theory](https://plato.stanford.edu/entries/epistemic-game/)<br/>[Two-person Zero-sum Games](https://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/mat.pdf) _Note that in this document, Player 1 chooses a row, whereas our Player 1 chooses a column_ |
| Fri, Apr 1  | Summary: Acting under incomplete or uncertain knowledge | [Lecture](lectures/Lec22_agent_reasoning_summary.pdf) |[Probabilistic Modal Logic](https://www.aaai.org/Papers/AAAI/2007/AAAI07-077.pdf)<br/>[Factored Models for Probabilistic Modal Logic](https://www.aaai.org/Papers/AAAI/2008/AAAI08-086.pdf)|
| Mon, Apr 4  | Temporal Logic for Representing Transitions | Lecture | **Last day to Withdraw** <br/> R&N 14, 17| 
| Wed, Apr 6  | Exam Review | Review | |
| Fri, Apr 8  | Exam 3: Agent-based Reasoning | Exam |  |
| Mon, Apr 11 | Exam 3: Agent-based Reasoning | Make-Up Exam | |
| Wed, Apr 13 | Probabilistic Modeling Review | In-class Work | **[Probabilistic Modeling Worksheet out](https://www.overleaf.com/read/fdnmqtxhdpbp)**|
| Fri, Apr 15 | Exam and programming assignment review | In-class Unit 3 review | 
| Mon, Apr 18 | LTL Applications | Lecture | <div>[Intractability of LTL Objectives in RL](https://arxiv.org/pdf/2111.12679.pdf)<br/>[Learning Interpretable Models Expressed in LTL](https://www.cs.toronto.edu/~acamacho/papers/cam-mci-icaps19.pdf)<br/>[LTL as an Executable Semantics for Planning Languages](https://link.springer.com/content/pdf/10.1007/s10849-006-9022-1.pdf)<br/>[Decoy Allocation Games on Graphs with LTL](https://www.gamesec-conf.org/2020/GameSec_Proceeding_2020/Paper%203.4.pdf)</div> |
| Wed, Apr 20 | Markov Chains for Representing Transitions | Lecture ||
| Fri, Apr 22 | Markov Decision Processes   | Lecture |**Probabilistic Modeling worksheet due in class**|
| Mon, Apr 25 | Learning Programs via Genetic Programming | Lecture ||
| Wed, Apr 27 | Learning Programs via Program Synthesis | Lecture | **Peer-graded Probabilistic Modeling worksheet due in class**|
| Fri, Apr 29 | Counter-example Guided Inductive Search| Lecture | Probabilistic Modeling worksheet solutions |
| Mon, May 2 | More Program Synthesis | Lecture | 
| Wed, May 4 | Exam 4: Time and Programs | Exam | **Last Day of Classes**<br/>**All programming assignments due (hard)** |
| Thu, May 12 | **Final Exam** | 7:30am-10:15, VOTEY 207 |
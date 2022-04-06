From Coq Require Import Logic.
From Coq Require Import Setoids.Setoid.
From Coq Require Import Logic.Classical_Prop.

(** this is the most straightforward solution. *)
Definition exam1_q3_sol1: forall (T: Type) (x : T) (P Q R : T  -> Prop),
    ((forall x, P(x) \/ Q(x)) /\
    (exists x, ~Q(x)) /\
    (forall x, R(x) -> ~P(x))) -> exists x, ~R(x).
Proof. 
    intros T x P Q R [H1 [H2 H3]].
    inversion H2 as [x0 H]. 
    exists x0. unfold not. intros H4. 
    apply H3 in H4. 
    apply (conj H4) in H.
    apply and_not_or in H. apply H. apply H1.
Qed.

(** this solution instantiates in a different order, follows exam format. *)
Definition exam1_q3_so2: forall (T: Type) (x : T) (P Q R : T  -> Prop),
((forall x, P(x) \/ Q(x)) /\
(exists x, ~Q(x)) /\
(forall x, R(x) -> ~P(x))) -> exists x, ~R(x).
Proof. 
    intros T x P Q R [H1 [H2 H3]].
    (** open scope *)
    assert (A: forall x, ~R(x)).
    (** line 4 of proof. *)
    + intros x0. intros H4. 
      (** apply both instantiates and derives the conequent.
        this line combines lines 5 and 8 in the exam proof.
        you can think of this as if we just wrote ~P(x) on line 5. *)
      assert (H5and8:=H4). apply H3 in H5and8. 
      assert (H6: ((P x0) \/ (Q x0))). apply H1.
      (** this is equivalent to the assumption boxes that 
        assume each branch of the disjunction. *)
      inversion H6 as [H7 | H10].
      - apply H5and8. apply H7. 
      (** x1 needs to be the certificate that makes H2 true. *)
      - inversion H2 as [x1 H11]. apply H11. 
      (** Now we are stuck. Coq manages scope automatically and 
          enforces. Since proofs are correct by construction modulo 
          the tactics library, it won't let you try to instantiate
          the existential with the universally quantified variable. *)
Abort. 

# Assignment#3

*181220076 周韧哲*



### Q1

1. The class expression is in NNF,so we can directly write:
   $$
   S_0=\{x:\exist R.\exist E.\lnot C\sqcap\forall R.C \}
   $$
   The application of $\rightarrow_\sqcap$ gives:
   $$
   S_1=S_0\cup \{x:\exist R.\exist E.\lnot C,x:\forall R.C \}
   $$
   The application of $\rightarrow_\exists$ gives:
   $$
   S_2=S_1\cup \{(x,y):R,y:\exist E.\lnot C \}
   $$
   The application of $\rightarrow_\exists$ gives:
   $$
   S_3=S_2\cup \{(y,z):E,z:\lnot C \}
   $$
   The application of $\rightarrow_\forall$ gives:
   $$
   S_4=S_3\cup \{y:C \}
   $$
   No rule is applicable to $S_4$ and $S_4$ contains no clash. Thus, the concept is satisfiable. A model $\mathcal{I}$ of this concept is given by:
   $$
   \Delta^{\mathcal{I}}=\{x,y,z\},\quad C^\mathcal{I}=\{y\},\quad R^\mathcal{I}=\{(x,y)\},\quad E^\mathcal{I}=\{(y,z)\}
   $$

2. From TBox $A\sqsubseteq B$  we can know there $\exist A'$ s.t. $A=A'\sqcap B$.

   And then we can convert  (R some A) and (R only (not B)) into
   $$
   \exist R.(A' \sqcap B) \sqcap \forall R. \lnot B
   $$
   It is NNF, the initial constraint is:
   $$
   S_0=\{x:\exist R.(A' \sqcap B) \sqcap\forall R.\lnot B \}
   $$
   The application of $\rightarrow_\sqcap$ gives:
   $$
   S_1=S_0\cup \{x:\exist R.(A' \sqcap B),x:\forall R.\lnot B \}
   $$
   The application of $\rightarrow_\exists$ gives:
   $$
   S_2=S_1\cup \{(x,y):R,y:A' \sqcap B \}
   $$
   The application of $\rightarrow_\forall$ gives:
   $$
   S_3=S_2\cup\{y:\lnot B\}
   $$
   The application of $\rightarrow_\sqcap$ gives:
   $$
   S_4=S_3\cup\{y:B,y:A'\}
   $$
   $S_4$ contains clush: $\{y:B,y:\lnot B\}$.

   No rule is applicable to $S_4$ , and it contains clushes. So the class expression  *(R some A) and (R only (not B))*  is unsatisfiable w.r.t  *A SubClassOf B*.

3. To proof $(\exists R.A \sqcap \exists R.B)\sqsubseteq(\exists R.(A\sqcap B))$ , is to proof $\lnot((\exists R.A \sqcap \exists R.B)\sqsubseteq(\exists R.(A\sqcap B)))$ is unsatisfiable. Convert it into NNF:
   $$
   \exists R.A\sqcap\exists R.B\sqcap\forall R.(\lnot A \sqcup\lnot B)
   $$
   and then we get:
   $$
   S_0=\{x:\exists R.A\sqcap\exists R.B\sqcap\forall R.(\lnot A \sqcup\lnot B)\}
   $$
   The application of $\rightarrow_\sqcap$ gives:
   $$
   S_1=S_0\cup \{x:\exists R.A,x:\exists R.B,x:\forall R.(\lnot A \sqcup\lnot B)\}
   $$
   The application of $\rightarrow_\exists$ gives:
   $$
   S_2=S_1\cup \{(x,y):R,y:A\}
   $$
   The application of $\rightarrow_\exists$ gives:
   $$
   S_3=S_2\cup \{(x,z):R,z:B\}
   $$
   The application of $\rightarrow_\forall$ gives:
   $$
   S_4=S_3\cup \{y:\lnot A \sqcup\lnot B,z:\lnot A \sqcup\lnot B\}
   $$
   The application of $\rightarrow_\sqcup$ gives:
   $$
   S_5=S_4\cup \{y:\lnot A\}
   $$
   $S_5$ contains clush: $\{y:A,y:\lnot A\}$.

   So we get another branch:
   $$
   S_5^*=S_4\cup \{y:\lnot B\}
   $$
   The application of $\rightarrow_\sqcup$ gives:
   $$
   S_6=S_5^*\cup \{z:\lnot B\}
   $$
   $S_6$ contains clush: $\{z:B,z:\lnot B\}$.

   So we get another branch:
   $$
   S_6^*=S_5^*\cup \{z:\lnot A\}
   $$
   No rule is applicable to $S_6^*$ and $S_6^*$ contains no clash. Thus, the concept is satisfiable. Therefore, (R some A) and (R some B) is not subsumed by R some (A and B) .


## Q2

Please see the source code `A#3-181220076.java`.


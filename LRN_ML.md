## Machine Learning
Machine learning, its a branch of programming that translates abstract
concepts of mathematics.

##### Sources:
*Oracle*:
- https://docs.oracle.com/cd/B28359_01/datamine.111/b28129/toc.htm

## Apriori
*Authors*:Rakesh Agrawal and Ramakrishnan Srikant

*Problem*: Find a way to suggest meaningful purchases to a customer.

### terms

#### I (set of items):
I is denoted as a set of literals and represents a set of items.

#### P (transaction/Purchase):
P denotes the purchases made by a customer. It is a subset of I.

#### D (collection of P):
D is the set of P made on set I.

#### TID (an Id):
It is a unique identifier associated with each purchase P.

#### Association Rule:
It is defined on subsets X and Y of a purchase P. Where an implication X
implies Y means that existence of set X (subset of P) implies the
existence of Y (subset of P) where X and Y are mutually exclusive.

#### Support:
it is the percentage of purchases P, which contain X union Y, expressed
as a probability P(A,B).

#### Confidence:
It is the percentage of occurrence the association rule expressed
as a probability. 
A implies B: P(A,B)/P(A) or B implies A: P(A,B)/P(B).

#### minconf and minsuppourt
they are thresholds of confidence and support parameter which are
specified by the user.

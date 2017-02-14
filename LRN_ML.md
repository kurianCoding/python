## Machine Learning
Its a branch of mathematics which deals in creating machines that make
rules from data points.

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
existence of Y (subset of P) in the purchase P, where X and Y are mutually exclusive.

#### Support:
it is the percentage of purchases P, which contain X union Y, expressed
as a probability P(A,B).

#### Confidence:
It is the percentage of occurrence the association rule expressed
as a probability. 
A implies B: P(A,B)/P(A) or B implies A: P(A,B)/P(B).

#### Minconf and Minsuppourt
they are thresholds of confidence and support parameter which are
specified by the user.

#### apriori algorithm

pseudo code:

  L<sub>1</sub> =  1 item set which has support greater than min-support.

    for each new set L<sub>k-1</sub>:
        if L<sub>k-1</sub> = null:
	   break
        else:
	   C<sub>k</sub>=apriori-gen(L<sub>k-1</sub>)
           use this C<sub>k</sub> as the new L<sub>k</sub>
	   filter the elements of C<sub>k</sub> which have min-support.
	   assign this filtered set as the new L<sub>k-1</sub>

    return Union of all sets in L<sub>k</sub>

apriori-gen:

- input(L<sub>k-1</sub>)
- make all possible combinations of items in L<sub>k-1</sub>,
preventing duplication. 
- for each element so created find all the possible subsets, see if
these subsets are present in L<sub>k-1</sub> or any of the previous
itrerations. If not remove them from the list. 
- Return the remaining filtered list as the apriori-gen list.

## TOP 10 Machine Learning Algorithms

the links to all the representative papers
http://www.cs.uvm.edu/~icdm/algorithms/CandidateList.shtml

github link
https://github.com/josephmisiti/awesome-machine-learning/blob/master/books.md

### HITS Algorithm

HITS algorithm is hyperlink based ranking tool. It tries to guess the
most relevant pages not just on the number of links that a web page has
but also on the way the links are organized. It filters the most
relevant links by a series of filtering techniques. 

#### Terms

##### _Query_ 
A query is  a string which is searched in pages to find the pages
relevance w.r.t to that string.

##### _W_
W is the set of all web pages.

##### _E_
E is the set of all edges (directional) connecting web pages W.

##### _G(W,E)_
A mapping induced on the set of web pages W using edges in E.

##### _In-degree_
A parameter which indicates the number of links point *towards* the
page.

##### _Out-degree_
A parameter which indicates the number of links pointing *to other*
pages from this page.

##### _Hub_
Is a web page that *links to* a lot of authoritative web pages.

##### _Authority_
A web page that has the most relevant information to our query.

#### How it works
Following pesudo code illustrates the working of this algorithm.

Iterate(G,k):

- for all page p in G:
    - update value of all x<sub>p</sub>
    - update value of all y<sub>p</sub>
    	
- normalize X and Y
    
- return x <sub>k</sub> and y<sub>k</sub>
    	
Filter(G,k,c):
    c is a parameter that affects the depth and breadth of our search
    G is the graph
    the k node near which to find the behaviour of pages
    x,y=Iterate(G,k)
    return the c largest x as the authorities.
    return the c largest y as hubs.
    

#### Pseudo code

#### Draw backs

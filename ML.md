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

*Algorithm*
- collect the set of all pages which have high occurence of  the query
  string or tokens. Call this set R<sub>query</sub>.

- For each page in R<sub>query</sub> add all the pages which are pointed
  to from here.

- For each page in superset add all the pages which point to
  pages in R<sub>query</sub>. Keep a maximum ceiling d for such pages.

This resulting set is now S<sub>query</sub>

- From this set S<sub>query</sub> we remove links that point to the same
domain. We get G<sub>query</sub>.

- On the set S<sub>query</sub> define operations  &#921; and &#927; 
	- &#921;:
    the authority of a page x is defined as the sum of the hub weights
    of all the pages pointing to that page.
	- &#927;:
    the hub weight of a page y is defined as the sum of all authorities
    of all the pages that this page points to.

- Authority x and hub weight y are  updated and normalised by dividing x
and y of each page by the sum of squares of x and y of all the web pages
in G<sub>query</sub> After applying &#921; and &#927;.
- Repeat &#921; and &#927; and normalisation until the x and y of all
  pages in G<sub>query</sub> converge within allowable limit.

#### Pseudo code

#### Draw backs

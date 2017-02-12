## this class signifies the node/page which will be sorted
class Page:
    def __init__ (self):
         self.referTo=0
         self.referFrom=0
         self.score=0
         self.title=""


## Itrate will take in the graph and the new page to be added and update the new
## values of x and y for each page
def iterate():
    return
## filter will take in the updated values of the page and return which of the pages 
## are hubs and which are authorities
def filterHubsAuthorities(array):
    return hubs,authorities

## returns pages with normalized scores for x and y
def normalize(array):
    return normalized

## hits algorithm for sorting.
def hits(pages):
    for page in pages:
        pages=iterate(page,pages)

    pages=normalize(pages)
    return

## take inputs
def takeInput():
    splitIntput=raw_input("enter the size of incidence the matrix").split(" ")
    row=int(splitIntput[1])
    column=int(splitIntput[2])
    InputPages=[row]
    for i in range(row):
        getrow=raw_input().split(" ")
        page=Page()
        page.title=""
        for j in range(column):
            if(int(getrow[j])>0):
                page.referTo+=1
            else:
                page.referFrom+=1
        print InputPages
        InputPages[i]=page
    return

def printMatrix(array,title):
    return

def main ():
    inputArray=takeInput()
    rankedArray=hits(inputArray)
    hubs,authorities=filterHubsAuthorities(rankedArray)
    printMatrix(hubs,"hubs") 
    printMatrix(authorities,"authorities") 
    return

main()

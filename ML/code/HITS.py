## Itrate will take in the graph and the new page to be added and update the new
## values of x and y for each page
def itrate():
    return
## filter will take in the updated values of the page and return which of the pages 
## are hubs and which are authorities
def filterHubsAuthorities(array):
    return hubs,authorities

## returns pages with normalized scores for x and y
def normalize():
    return

## hits algorithm for sorting.
def hits():
    for each page in pages:
        pages=iterate(page,pages)
    pages=normalize(pages)
    return

## take inputs
def takeInput():
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

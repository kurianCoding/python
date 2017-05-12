# a progeram to calculate erdos number
# it requires the erdos number of one
# of the individuals and based on the
# connection between that individual
# and you, you can get your erdos
# number

# a class to hold the persons name and the names
# of all the people he has done research with and 
# make a list of it

class res:
    def __init__():
        # initialize all the variables which are used in
        # the model
        this.colabs=array()
        this.erdos=100
        this.name=''
        return

    # a method to add colabs
    def addColab(newres):
        # add a colab with name and erdos number
        this.colabs.push(newres.name)
        if newres.erdos<100&&this.erdos>(newres.erdos+1):
            this.erdos=newres.erdos+1
        return

    # a method which will take the erdos number of an
    # individual and assign it to that persons class
    def setErdosNo(erdos):
        this.erdos=erdos
        return
    
    # this method goes through erdos numbers of all the
    # colabs of the person and then finds the erdos number
    # this person
    def getErdosNo():
        # get erdos number of the person
        for person in this.colabs:
            if person.erdos>(this.erdos+1):
                this.erdos=person.erdos+1

        return this.erdos
    def __toString()__:
        return this.name+" "+this.erdos


# TODO
# a method which will iterate over all the co authors
# of an individual and calculate the erdos number of
# all the co authors by matching them with entries
# already in the list

# TODO
# a method which will take all the erdos numbers of the
# people in the list and print them

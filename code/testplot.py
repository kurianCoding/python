import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pylab as pl
figure=plt.figure()
ax=figure.add_subplot(111)
x=[1,2,3,4,5]
y=[2,4,6]
ax.hist(x,11)
figure.savefig('foo.png')

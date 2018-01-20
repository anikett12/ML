import numpy as np
from matplotlib import pyplot as plt
def costfunction(x, y,alpha,terminate):
    t= np.array([[0,0,0]])
    m = np.size(x,1)
    g = np.ones((3, m))
    g[1:,:]=x

    k=np.sum( np.dot(np.log(1/(1+np.exp((-np.dot(t,g))))),np.transpose(y))+ np.dot(np.log(1-(1/(1+np.exp((-np.dot(t,g)))))),np.transpose(1-y)))
    J= (1/(2*m))*k

    for i in range(0,terminate):
        t= t- alpha*(1/m)*(np.dot((1/(1+np.exp((-np.dot(t,g))))-y),(np.transpose(g))))
    return (t)


def answer():
    x = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[2,3,5,4,6,5,7,8,8,9]])
    y = np.array([[0, 1, 0, 0, 1, 0, 1, 0, 0, 1]])
    q=np.size(x,1)
    alpha=0.001
    terminate = 5000
    b=np.array([[0,0,0]])
    b = costfunction(x,y,alpha,terminate)

    for i in range(1,q):
        if y[0:1,(i)]==0 :
           plt.plot(x[0:1, (i)], x[1:2, (i)], 'ro')
        else :  plt.plot(x[0:1, (i)], x[1:2, (i)], 'bo')
    plt.show()
    print(b)

answer()




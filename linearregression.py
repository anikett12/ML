import numpy as np

def costfunction(x, y,alpha,terminate):
    t= np.array([[0,0]])
    m = np.size(x)
    g = np.ones((2, m))
    g[1:,:]=x

    k=np.sum(np.dot(t,g)-y)
    J= (1/(2*m))*k

    for i in range(0,terminate):
        t= t- alpha*(1/m)*(np.dot(((np.dot(t,g))-y),(np.transpose(g))))
    return (t)



def answer():
    x = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
    y = np.array([[1, 3, 2, 5, 7, 8, 8, 9, 10, 12]])
    alpha=0.001
    terminate = 5000
    b=np.array([[0,0]])
    b = costfunction(x,y,alpha,terminate)
    print(b)

answer()



















import numpy as np

X=np.array([[1,0,0,1],[1,0,1,0],[0,1,0,1]])

y=np.array([[1],[0],[1]])

def sigmoid (x):
    return 1/(1 + np.exp(-x))




Xsize = 4
Asize = 3
Bsize=4
Ysize = 1

t= np.ones((3,5))
t[:,1:]=X
theta1=np.random.uniform(size=(Asize,Xsize+1 ))
theta2=np.random.uniform(size=(Bsize,Asize+1 ))
theta3=np.random.uniform(size=(Ysize,Bsize+1))
for i in (1,1000):
    Layer_1= sigmoid(np.dot(theta1,np.transpose(t)))

    S = np.ones((4, 3))
    S[1:,:] = Layer_1
    Layer_2 = sigmoid(np.dot(theta2,(S)))
    T = np.ones((5, 3))
    T[1:,:] = Layer_2
    output = sigmoid(np.dot(theta3, T))
    E= np.transpose(y)-output

    E1= (np.dot(np.transpose(theta3),(E))*T*(1-T))
    o=E1[1:,:]
    E2=(np.dot(np.transpose(theta2),o)*S*(1-S))
    p=E2[1:,:]
    derivative=(np.dot((E),np.transpose(T))/3)
    derivative1= (np.dot(o,np.transpose(S))/3)
    derivative2= (np.dot(p,t)/3)
    theta3 = theta3- ((1/3)*0.001*derivative)
    theta2 = theta2-((1/3)*0.001*derivative1)
    theta1 = theta1 - ((1/3)*0.001*derivative2)
print(theta1)
print(theta2)
print(theta3)






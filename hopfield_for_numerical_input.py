# -*- coding: utf-8 -*-
"""Hopfield for numerical input

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IvCkWU-7vcAGJP9_ttTqY7O-KcYOu-p2
"""

import numpy as np
class HOP:

  def __init__(self,X,input,sync=False,epochs=1000):
      
      self.X=X
      self.input=input
      self.sync=sync
      self.epochs=epochs
      
    
  def fit(self):
    n=X.shape[1]
    p=np.dot(self.X,np.transpose(self.X)).shape[0] #or 1 no difference
    w=np.dot(self.X,np.transpose(self.X)) - n*np.eye(p,dtype=int)
    a =[] 
    a.append(self.input)
    for i in range(1,self.epochs):
      a.append(np.sign(np.dot(w,a[i-1])))  
      if(np.array_equal(a[i],a[i-1])):
        print(a[i])
        break
      else:
        pass
      while(self.sync==False):
        for j in range(self.input.shape[0]):
          if(a[i][j]!=a[i-1][j]):
            for q in range(j+1,self.input.shape[0]):
              a[i][q]=a[i-1][q]
        break                 
#Data
X = np.array([[1,1,1,1],[1,-1,-1,1]]).T  
x = np.array([[1,1,1,-1]]).T                
#definig an object
b=HOP(X,x)
b.fit()
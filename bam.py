# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:04:22 2021

@author: shneb
"""
import numpy as np
import matplotlib.pyplot as plt
pattern_1=np.array([[-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,
                     -1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1]])
pattern_2=np.array([[1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,
                    1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1]])
pattern_3=np.array([[1,1,1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,
                    -1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1]])
pattern_4=np.array([[1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,
                    -1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1]])
pattern_5=np.array([[1,1,1,1,1 ,1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1,
                    -1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1]])
pattern_6=np.array([[1,1,1,1,1 ,1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1,
                    1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1]])
#pattern 1 --> pattern 2 , pattern 2 --> pattern 1
#pattern 3 --> pattern 4 , pattern 4 --> pattern 3
#pattern 5 --> pattern 6 , pattern 6 --> pattern 5
weight_1=(np.dot(pattern_1.T,pattern_2))
weight_2=(np.dot(pattern_3.T,pattern_4))
weight_3=(np.dot(pattern_5.T,pattern_6))
weight=weight_1+weight_2+weight_3

test=np.array([[1,1,1,1,1 ,1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1,
                    -1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1]])
print("\n")
print("In case text matrix is equal to pattern 5:")
print("\n")
print(test)
print("\n")
y=np.dot(test,weight) #For bidirectional change formula y=np.dot(test,weight.T)
print("y=np.dot(test,weight)")
print("\n")
y[y<0]=-1
y[y>0]=1
print(y)
print("\n")
comparison= y==pattern_6
equal_arrays=comparison.all()
if equal_arrays==True:
    print("KNOWN PATTERN")
else:
   print("THIS IS NOT EXPECTED OUTPUT" )
print("\n")
plt.imshow(y.reshape(8,5))

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sum_expL= sum(expL)
    result=[]
    for i in expL:
        result.append(float(i/sum_expL))
    return result

print(softmax([1,2,3]))
print(softmax([101,102,100]))
print(softmax([-101,-102,-103]))    
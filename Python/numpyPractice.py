import numpy as np

a = np.array([[1, 2, 3],[4,5,6],[7,8,9]])
print(a)
print(a+2) #all entities are increae by 2 , a**3
type(a) #numpy.ndarray -> n dimensional array

b = np.array([[1,2,3]] , dtype= str )
print (type(b))

print (len(b))
print (a.ndim) # tells dimensions of array

print(a.shape) #tells no of rows and columns

print(b.dtype)

print(a[0,2]) #print 3rd elemnt of 0th row
print(a[0:])
print(a[:,0]) #first element of all rows

a[0,2] =100 #assignment

x = np.zeros((3,3) , dtype=bool) #creates a 2d array of 3x3 with 0s
print(x);

y = np.ones((3,3) , dtype=int) #creates a 2d array of 3x3 with 1s
print(y);

z = np.full((3,3) ,100, dtype=str) #creates a 2d array of 3x3 with 100s
print(z);

n = np.random.rand(4,4) #matrix of random numbers
print(n)

m = np.random.randint(-8,8, size = (4,4)) #matrix of random numbers
print(m)

i =np.identity(5) #to create an identity matrix - diaogonal 1 all other elems = 0

print(i)


#Exercises

# extract first 3 rows of last 5 cols - a [:3 ,-5:]

# given a positive number n greater than 2 , create a numpy array of size(nxn) with all zeroes such that the ones make a shape of +
n=3
byTwo = (int)(n/2)
print(byTwo)
plus = np.zeros((3,3))
plus[:,byTwo] =1
plus[byTwo, :]=1
print (plus)


#maths and stats functions on array
# a.min() or np.min(a) , max , a**3 ,a.mean() ,np.mean(a),np.sum(a),a.sum()
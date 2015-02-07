import fileinput
import sys

def cloth():
  
  #arrays to hold raw input and size/value results 
  input = []
  dims = []

  #recursive function
  def maxVal(X, Y):
    for i in range(1, X):
      for j in range(1, Y):
        if(maxp[i][j] != -1):
          return maxp[i][j]
        else:
          a = 0
          b = 0
          for x in range(0, i):
            if(maxp[x][j]+maxp[i-x][j] > a):
              a = maxp[x][j]+maxp[i-x][j]

          for y in range(0, j):
            if(maxp[i][j-y]+maxp[i][y] > b):
              b = maxp[i][j-y]+maxp[i][y]

          maxp[i][j] = getMax(a, b, price[i][j])
          return maxVal(i-1,j-1)
  
  #Read the txt file line by line
  for line in fileinput.input():
    line = line.split() 
    input.append(line)  

  print "Reading", fileinput.filename()
  
  #set values based on first 3 inputs from the file
  X = int(input[0][0])
  Y = int(input[0][1])
  n = int(input[1][0])
  
  #X*Y for price of possible pieces and max prices
  price = [[-1]*Y for _ in range(X)]
  maxp = [[-1]*Y for _ in range(X)] 
  maxp[0][0] = 0

  #fill the dimension array from the input array
  for i in range(2, len(input)-1):
    dims.append(input[i])
  
  #fill prices from the dimension array
  for i in range(0, n-1):
    if(price[int(dims[i][0])][int(dims[i][1])] < int(dims[i][2])):
      price[int(dims[i][0])][int(dims[i][1])] = int(dims[i][2]) 
  
  #call the recursive max value function based on the size of the cloth
  maxVal(X-1, Y-1)
  
  print "Maximum Return: ", maxp[X-1][Y-1], '\n'

#return the maximum of three values
def getMax(a, b, c):
  if(a > b & a > c):
    return a
  elif(b > a & b > c):
    return b
  else:
    return c

if __name__ == '__main__':
  cloth()

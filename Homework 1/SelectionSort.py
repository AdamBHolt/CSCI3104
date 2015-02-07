import random
import time

def main():
  p=2
  for x in range(1, 11):
    start = time.time()
    n = pow(10, p)
    nums = []
    for i in range(1, n):
      nums.append(RandomNum())
    print nums
    SelectionSort(nums)
    print nums
    print "n = 10^", p ," Test ", x, " - Runtime: ", time.time() - start
  
def SelectionSort(A):
  for i in range(0, len(A)-1):
    for j in range(i+1, len(A)):
        imin = i
        if(A[j] > A[imin]):
            imin = j
        temp = A[j]
        A[j] = A[imin]
        A[imin] = temp
  return A

def RandomNum():
  return random.randint(0,1000000) 

if __name__ == "__main__":
    main()

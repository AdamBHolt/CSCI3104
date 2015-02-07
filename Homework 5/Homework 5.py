import fileinput
import sys

def wordlist():
  nodes = []
  graph = {}
  maxChain = 1
  loop = 0
  
  for word in fileinput.input():
    nodes.append(word)  
    if len(word)-2 > maxChain:
      maxChain = len(word)-2

  nodes.sort()
  nodes.sort(lambda x,y: cmp(len(x), len(y))) 
  
  while len(nodes[loop]) < 4:
    loop = loop + 1

  for i in range(0, loop): 
    list = []
    list.append(nodes[i])
    for j in range(i, len(nodes)):
      if compareWords(nodes[i], nodes[j]) == 1:
        i = j
        list.append(nodes[j])
    if len(list) == maxChain:
       printArray(list)

#compare words to see if they match or chain 
def compareWords(w1, w2):
  w1 = ''.join(sorted(w1))
  w2 = ''.join(sorted(w2))

  if len(w1)==len(w2):
    if w1 == w2:
      return 0
    else:
      return -1
  elif abs(len(w1)-len(w2))==1:
    w1 = sorted(w1)
    w2 = sorted(w2)
    if len(w1) < len(w2):
      if matchLetters(w1,w2):    
        return 1
      else:
        return -1
    elif len(w2) < len(w1):
      if matchLetters(w2,w1):
        return 1
      else:
        return -1
  else:
    return -1

#compare words that have different lengths
def matchLetters(w1, w2):
  matches = 0
  word1 = w1
  word2 = w2  
  
  for i in range(1, len(word1)):
    if word1[i] == word1[i-1]:
      word1[i] = '\0'
 
  for i in range(1, len(word2)):
    if word2[i] == word2[i-1]:
      word2[i] = '\0' 
 
  for ch1 in word1:
    found = False
    for ch2 in w2:
      if ch1 == ch2:
        found = True
    if found == True:
      matches = matches + 1
 
  if matches == len(word1):
    return True
  else:
    return False

def printArray(list):
  for word in list:
    sys.stdout.write(word)

if __name__ == '__main__':
  wordlist()

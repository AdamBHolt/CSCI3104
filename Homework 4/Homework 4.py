import fileinput

def wordlist():
  nodes = []
  graph = {}

  for word in fileinput.input():
    nodes.append(word)  

  nodes.sort(lambda x,y: cmp(len(x), len(y))) 


  for node in nodes:
    graph.update({node:[]})

  for node1 in nodes:
    for node2 in nodes:
      if compareWords(node1, node2) == 1:
        graph[node].append(node2)

  print graph

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

  for ch1 in w1:
    found = False
    for ch2 in w2:
      if ch1 == ch2:
        found = True
    if found == True:
      matches = matches + 1
      
  if matches == len(w1):
    return True
  else:
    return False

if __name__ == '__main__':
  wordlist()

# python3

import sys
import threading
import numpy as np

class Tree:
    def __init__(self, n, parent):
      self.n = n
      self.parents = np.array([int(p) for p in parents.split()])
      self.h = 0

def compute_height(n, parents):
    max_height = 0

    for x in range(n-1):
        current_h = 1
        curr = parents[x]

        storage = [curr]

        while curr.parent != -1:
            if curr.h > 0:
                current_h = current_h + curr.h
                break
            storage.append(curr)
            current_h += 1
        for st in storage:
            st.h = current_h
            height -= 1

    max_height = max([st.h for st in parents])
    return max_height






    #max_height = 0

    #rewrite from list to numpy array !!!, tests 21-25???

    #par_split = parents.split()
    #par_split = map(int, par_split)
    #par_split = list(par_split)
    #ar_split = np.array(par_split)
    #print(par_split)

    #already_was = {}

    #for i in range(n):
     #   if i not in already_was:
      #      current_h = 0
       #     curr = i
        #    while curr > -1:
         #       if curr in already_was:
          #          current_h += already_was[curr]
           #         break
            #    current_h += 1
             #   curr = par_split[curr]
              #  already_was[i] = current_h
        #max_height = max(max_height, already_was[i])
                

def main():
    text = input()
    if 'F' in text and not 'a' in text:
        file_name = input()
        file = "./test/" + file_name
        #print(file)
        with open(file) as f:
            num = f.readline()
            text = f.readline()
    if 'I' in text:
        num = input()
        text = input()
    
    print(compute_height(int(num), list(maptext))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

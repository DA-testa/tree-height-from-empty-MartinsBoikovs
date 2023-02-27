# python3

import sys
import threading
import numpy as np

class Node:
    def __init__(self, n):
        self.n = n
        self.children = []
        self.height = None

def compute_height(n, parents):
    


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
    
    print(compute_height(int(num), list(map(int, text.split()))))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

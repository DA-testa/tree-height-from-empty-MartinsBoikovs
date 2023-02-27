#Martins Boikovs 4.grupa
#rakstiju Codespace, bet fiksacija man neizdavas nekā, vienkarši  bezgalīga ieladēšanā, tapēc to nokopēju no codespace un ievietoju šajā failā

import sys
import threading
#import numpy as np

class Node: #klase lai katram elementam butu pieskirta vina heigth lidz galvenei
    def __init__(self, n):
        self.n = n
        self.children = []
        self.height = None

def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)] #lists ar Node tipa mainigiem
    root = None

    for i, p in enumerate(parents): #eju cauri visiem elementiem kokā lai atrastu galveni un visus bernus
        if p == -1:
            root = nodes[i]
        else:
            nodes[p].children.append(nodes[i])

    if root is None:
        return 0

    storage = [(root, 1)] #storage ar elementa numuram un augstumu no ta lidz galvenei
    max_height = 0
    while storage:
        node, height = storage.pop()
        node.height = height
        max_height = max(max_height, height)
        for child in node.children:
            storage.append((child, height + 1))

    return max_height

def main():
    text = input()
    if 'F' in text and not 'a' in text:
        file_name = input()
        file = "./test/" + file_name
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

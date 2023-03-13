# Anastasija Andrejeva, 18.grupa, 221RDC028

import sys
import threading
import os

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    tree = None

    for i, j in enumerate(parents):
        if j == -1:
            tree = i    
        else:
            children[j].append(i)

    def max_height(value):
        height = 1
        
        if not children[value]:
            return height
        else:
            for child in children[value]:
                height = max(height, max_height(child))

            return height + 1
    return max_height(tree)

def main():
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:
        fileName = input()
        path = './test/'    
        mape = os.path.join(path, fileName)
        if "a" in fileName:
            print("Faila nosaukumā ir kļūda")
            return
            
        else:
            try:
                with open(mape) as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
            except Exception as error:
                print("Error", str(error))
                return
                  
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return
            
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

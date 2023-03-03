import sys
import threading

def compute_height(n, parents):
    m = [[] for _ in range(n)]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i    
        else:
            m[parent].append(i)

    def max_height(value):
        tree = 1
        
        if not m[value]:
            return tree
        else:
            for child in m[value]:
                tree = max(tree, max_height(child))

            return tree + 1
    return max_height(root)

def main():
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:
 
        file = input()
        if "a" in file:
                print("Error")
                return      
        else:
            with open (file, mode="r") as file: 
                count = int (file.readline ())
                text = file.readline ()
        
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return
            
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

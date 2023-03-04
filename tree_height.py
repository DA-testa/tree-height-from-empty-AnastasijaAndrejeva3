import sys
import threading

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = None

    for i in range(n):
        if parents[i] == -1:
            root = i    
        else:
            children[parents[i]].append(i)

    def max_height(value):
        height = 1
        
        if not children[value]:
            return height
        else:
            for child in children[value]:
                height = max(height, max_height(child))

            return height + 1
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
            with open (file, mode="r") as f: 
                count = int(f.readline())
                parents = list(map(int, f.readline().split()))
                n = len(parents)
                  
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return
            
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

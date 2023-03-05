
import sys
import threading

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = None

    for i, j in in enumerate(parents):
        if j == -1:
            root = i    
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
    return max_height(root)

def main():
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:
 
	path = './test/'
        file = input()
        folder = path + file
        if "a" not in file:
            try:
                with open(folder) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
            except Exception as e:
                print("Kluda:(", str(e))
                return
            
        else:
            print("Kluda")
            return
                  
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return
            
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()

import sys
import time
import threading
from collection import nametuple
import namedtuple

elem = namedtuple("elem", ["vertiba", "dzilums", "apmeklējums"])

def main(): 
    ievade = input ()
    text = ""
    count = 0
    if "I" in ievade: 
        count = int(input())
        text = input() 
    elif "F" in ievade:
        FName = input("Ievadiet faila nosaukumu: ")
        if "a" in FName:
            print("Faila nosaukumā nedrīkst būt burts 'a'")
        else:
            pl = time.time()
            with open(FName, mode="r") as file: 
                count = int(file.readline ())
                text = file.readline()

    text = text.split()
    text = list(map(int, text)) 
    m = [elem(val, 0, False) for val in text]
    max_height = 0
    for i in range (count) :
        val = m[i]
        if not val.apmeklējums:
            tail [i]
            height = 1
            while val.vertiba != -1:
                tail.append(val.vertiba)
                val = m[val.vertiba]
                height += 1
                if val.apmeklējums:
                    height += val.dzilums
                    break
                if height > max_height:
                    max_height = height
            n = val.dzilums
            for j in range(len(tail) -1, -1, -1):
                node = tail[j]
                if m[node] = elem(m[node].vertiba, n, True)
                n += 1

    print (max_height) 
#laiks2 = time.time()
#print (laiks2 - laiks1)
sys.setrecursionlimit (10**7)
threading.stack_size (2**27) 
threading. Thread (target-main).start()

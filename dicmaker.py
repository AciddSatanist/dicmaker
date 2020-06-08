import itertools
import sys
import os
import random

os.system("clear")
os.system("figlet DicMaker1.1")

def line():
    print("-"*60)
    print("-"*60)

line()
print("[+]input Keyword for make dictionary ")
print("ex: <keyword1>(space)<keyword2>(space)<keyword3>(space)...")
line()
word = input("[+]Enter the KeyWord: ")
name = input("[+]ENter the file name (without the extension)")

array = word.split()
origin = array

print("[+]Element Count: {}".format(len(array)))

dictio = {}

s = set(array)

counts = len(array)
dic_array = []

with open(name + '.txt', 'w') as f: 

    for i in range(counts ** counts):
        random.shuffle(array)
    
        roll = ' '
        for x in array:
            roll += x
        
        

        print(roll)
        f.write("%s\n" % roll)

os.system("sudo sort -u " + name + ".txt" + " -o " + name + ".txt")    
os.system("figlet Processed")
print("[*]Deleted overlapping lines...")






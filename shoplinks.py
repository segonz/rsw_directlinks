import webbrowser
import time
import os
import csv

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

BASE = "http://shopalphacomm.com/"
#new = 2
#webbrowser.open_new_tab(BASE)
#time.sleep(2)
''' text = open("items.csv",'r')
items=text.readlines()
 '''
file = open('items.csv', "rb")
reader = csv.reader(file)
count = 1
for row in reader:
    line_out = str(count) + ". Opening: " + row[0]
    print line_out
    webbrowser.open_new_tab(BASE + row[0] + "?quantity=" + row[1])
    time.sleep(1)
    count = count + 1


''' for i in range(len(items)):
    #webbrowser.open(BASE + items[i],new=new)
    if (i+1) % 10 == 0:
        print "Press Any Key To Continue: "
        raw_input()

    webbrowser.open_new_tab(BASE + items[i])
    print i + 1, ": Opening", items[i]
    time.sleep(1) '''
    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:43:35 2020

@author: user
"""
import re
n=list()
r=list()
li=list()
temp=list()
fistval=list()
file=open("sample_input.txt",'r')
for i in file:
    pat=re.findall(r'\d',i)
    fistval.append(pat)
    pa=re.findall(r'\d\d+',i)
    n.append(pa)
first=fistval[0]
finp=int(first[0])

for k in range(4,len(n)):
    z=n[k]
    r.append(z[0])
    temp.append(z[0])
for i in range(0, len(r)): 
    r[i] = int(r[i])
    temp[i]=int(r[i])
temp.sort()
for se in range(0,len(r)):
    if(r[0]==temp[se]):
        see=se+finp
        for se in range(se,see):
            li.append(temp[se])

minmum=min(li)
maximum=max(li)
difference=maximum-minmum
for c in range(0,len(li)):
    li[c]=str(li[c])
filew=open("sample_output.txt",'w')
file=open("sample_input.txt",'r')
for i in file:
    for x in range(0,len(li)):
        search=li[x]
        if(re.findall(search,i)):
            filew.write(i)
            filew.write("\n")
filew.write("And Difference Between the Chosen Goodie with Highest Price and the Lowest Price Is: ")
filew.write(str(difference))
filew.write("\n")
filew.close()
    
    
        
            
    
    

    



    
    
    
    
    


    

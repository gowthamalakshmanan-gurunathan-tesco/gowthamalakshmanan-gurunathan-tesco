'''
Created on 04-Apr-2021

@author: Gowtham Lakshman
'''

import requests


url = 'https://www.random.org/integers/?num=1&min=1&max=1000000&col=5&base=10&format=plain&rnd=new'

i=0

while i < 5:
    
    x = requests.get(url)
    
    x=int(x.text)
        
    if(x%2==0):
        print("No")
    else:
        print("Yes")

    i = i +1


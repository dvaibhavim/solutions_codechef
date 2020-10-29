# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:07:54 2020

@author: lenovo
"""

import json 
from logpy import Relation, facts, run, conde, var, eq 

# Check if 'x' is the parent of 'y' 
def parent(x, y): 
    return conde([father(x, y)], [mother(x, y)]) 

# Check if 'x' is the grandparent of 'y' 
def grandparent(x, y): 
    temp = var() 
    return conde((parent(x, temp), parent(temp, y))) 

# Check for sibling relationship between 'a' and 'b'   
def sibling(x, y): 
    temp = var() 
    return conde((parent(temp, x), parent(temp, y))) 

# Check if x is y's uncle 
def uncle(x, y): 
    temp = var() 
    return conde((father(temp, x), grandparent(temp, y))) 

if __name__=='__main__': 
    father = Relation() 
    mother = Relation() 
    
# =============================================================================
# with open('RELATIONSHIPS.json') as f: 
#         d = json.loads(f.read()) 
    #Relationships Paternal-Uncle Maternal-Uncle Paternal-Aunt Maternal-Aunt Sister-In-Law Brother-In-Law Son Daughter Siblings
    
# =============================================================================
d =   {"father":[{"John":"William"},{"John":"David"},{"John":"Adam"},{"William":"Chris"},{"William":"Stephanie"},{"David":"Wayne"},{"David":"Tiffany"},{"David":"Julie"},{"David":"Neil"},{"David":"Peter"},{"Adam":"Sophia"}],"mother":[{"Megan":"William"},{"Megan":"David"},{"Megan":"Adam"},{"Emma":"Stephanie"},{"Emma":"Chris"},{"Olivia":"Tiffany"},{"Olivia":"Julie"},{"Olivia":"Neil"},{"Olivia":"Peter"},{"Lily":"Sophia"}]}
       
for item in d['father']: 
        facts(father, (list(item.keys())[0], list(item.values())[0])) 
 
for item in d['mother']: 
    facts(mother, (list(item.keys())[0], list(item.values())[0])) 





        
x = var()
# John's children 
name = 'John' 
output = run(0, x, father(name, x)) 
print("\nList of " + name + "'s children:") 
for item in output: 
    print(item) 

    
    
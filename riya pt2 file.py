#!/usr/bin/env python
# coding: utf-8

# In[2]:


#vivaque 
#ans1
# (a). It will print the value of for range 0 to 4.
#         Output:- 1,2,3,4
# (b). It will print all the values of I present in the list.
#         Output:- 1,2,3,4,5,6
#ans2
#Output:- abcdefghij
#ans3
#By using join function for example:
#def listToString(s):  
#str1 = " " 
#return (str1.join(s)) 
#s = ['Geeks', 'for', 'Geeks'] 
#print(listToString(s))


#execution ans2
# creating a blank dictonary
semester4 = {} 
  
## adding the value to the dictonary
semester4["student_name"] = ["abc","xyz","def"] 
semester4["expirement_items"] = ["test_tube", "chemical", "stirrer","water"]
semester4["num_of_items"]=[10,10,5,50]


## printing the values of the dictonary

for val in semester4.values(): 
        print(val) 


## adding the faculty_assigned as key and a,b,c,d as a value to the existing dictonary semester4


semester4["faculty_assigned"]=["a","b","c","d"]

## showing the value of the dictonary after adding the new elemenet
for val in semester4.values(): 
        print(val)


## sorting the value of the empirement_items and printing them as a new line using loop

for i in sorted (semester4["expirement_items"]) :  
         print(i) 


## changing the value of num_of_items to 4
for val in semester4.items():
            semester4["num_of_items"]={4,4,4,4}

## printing the entire dictonary after performing all the operations
            
print(semester4.items())



#printing the value of the dictonary using silicing

## setting the range 
value = 3
    
slicing = dict(list(semester4.items())[0: value])  
        
# printing result   
print("Dictionary by slilicing is  : " + str(slicing)) 
        


# In[ ]:





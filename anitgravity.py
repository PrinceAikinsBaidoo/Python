#import antigravity
import math as mt
import re   # Importing Regular Expression module

# Using dir command to list out all the modules in anitgravity and math
#x = dir(antigravity)
y = dir(mt)

print(mt.gamma(2))
print(pow(2, 3))
print(abs(-4))
print(mt.sqrt(3))

text1 = "This is a test sentence for this case.\n THis is a test for the second case."
i = re.findall("a.*test", text1) #Without absolute referencing - search for anything containing the extract
j = re.search("^a.*test$", text1)    #With absolute referencing - searches for the exact extract
k = re.search("a.*test$", text1)    #With absolute referencing
print(i, " \n" ,j, "\n" ,k)

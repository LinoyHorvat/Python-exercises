
''' Exercise #1. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
a = 1 # Replace ??? with a positive number (int/float) of your choice.
b = 2 # Replace ??? with a positive number (int/float) of your choice.

# Write the rest of the code for question 1 below here.
c=(a**2+(b/2.0)**2)**0.5
print 'Length of c is '+str(c)
print 'Area is '+str(c*(b/2.0))
print 'Circumference is '+str(a*4.0)

#########################################
# Question 2 - do not delete this comment
#########################################
some_str ="uygouygfouwqyteewf" # Replace ??? with string of your choice.

# Write the rest of the code for question 2 below here.
if len(some_str)>6 and some_str [5] == "a" and some_str[6] == "b" and some_str[-2] == "c": print 'Yes'
else: print 'No'


#########################################
# Question 3 - do not delete this comment
#########################################
x = 2 # Replace ??? with a positive number (int/float) of your choice.
y = 3 # Replace ??? with a positive number (int/float) of your choice.
z = 2 # Replace ??? with a positive integer of your choice.

# Write the rest of the code for question 3 below here.
s= (x+y+z)/2.0

if x+y>z and x+z>y and y+z>x:
    print "The triangle's circumference is " + str(x+y+z)
    print "The triangle's area is " + str((s*(s-x)*(s-y)*(s-z))**0.5)

else:
    z=((x**2+y**2)**0.5)
    s=(x+y+z)/2.0
    print "These edges cannot form a triangle, but for z=" +str(z) + " we get:"
    print "The triangle's circumference is " + str(x+y+z)
    print "The triangle's area is " + str((s*(s-x)*(s-y)*(s-z))**0.5)
    

#########################################
# Question 4 - do not delete this comment
#########################################
a1 =1 # Replace ??? with a positive number (int/float) of your choice.
a2 =2 # Replace ??? with a positive number (int/float) of your choice.
n  =2 # Replace ??? with an integer > 2 of your choice.

# Write the rest of the code for question 4 below here.
q=float(a2)/(a1)
print "The "+str(n)+" number in this series is "+str(a1*(q**(n-1)))


#########################################
# Question 5 - do not delete this comment
#########################################
donor ='A' # Replace ??? with ('AB'/'A'/'B','O').
recipient ='A' # Replace ??? with ('AB'/'A'/'B','O').

# Write the rest of the code for question 5 below here.

if donor!='AB' and donor!='A' and donor!='B'and donor!='O'or recipient!='AB' and recipient!='A'and recipient!='B'and recipient!='O': print 'Invalid input'
elif recipient=='AB' or recipient==donor or donor=='O': print "Yes"
else: print "No"

#########################################
# Question 6 - do not delete this comment
#########################################
str1 = 'cvhggGhgvc'  # Replace ??? with a string of your choice.

# Write the rest of the code for question 6 below here.
a= len(str1)/2-1
if len(str1)<4 or str1[a]!='g' and str1[a]!='G': print 'No'
elif (len(str1)%2)==0 and str1[0]==str1[-1] and str1[1]==str1[-2]: print 'Yes'
else: print "No"


#########################################
# Question 7 - do not delete this comment
#########################################
str2 = 'Al6nhomo' # Replace ??? with a string of your choice.

# Write the rest of the code for question 7 below here.

if str2[2]=='9': print str2[-1]+str2[1]+str(0)+str2[3:-1]+str2[0]
elif str.isdigit(str2[2]):print str2[-1]+str2[1]+str(int(str2[2])+1)+str2[3:-1]+str2[0] 
elif str.isalpha(str2[2]):print str2[-1]+str2[1]+str2[2:-1]+str2[0]



''' Exercise #2. Python for Engineers.'''
# i didn't finish question: 1(b), 5, 6.
#########################################
# Question 1 - do not delete this comment
#########################################
numbers = [13,3,4,5,5,6,123,34342] # Replace ??? with a list of positive numbers (int/float).
# Write a code with for loop below here.
# Write a code with for loop below here.
n=0.0
for i in numbers:
    if i>n:
        n=i
print n
# Write a code with while loop below here.
l=0
while l<len(numbers)-1:
    if numbers[l]>numbers[l+1]:
        i=numbers[l]
    else: i=numbers[l+1]
    l+=1
print i
########################################
# Question 2 - do not delete this comment
#########################################
A = [-7,6,3,1,2,-3,1,-7] # Replace ??? with a list of numbers (int/float).
# Write the rest of the code for question 2 below here.
count=0
n= 0.0
for i in A:
    if i>3:
        n+=i
        count+=1
if count==0: print 0 #count=1
else: print float(n/count)
#########################################
# Question 3 - do not delete this comment
#########################################
B = [10,2,12,14,26,40] # Replace ??? with a list of numbers (int/float).

# Write the code for question 3 below here.
n=0
count=0
for i in B:
    if n<(len(B)-2) and B[n+2]==B[n]+B[n+1]:
        n=n+1
        count +=1
if count==(len(B)-2): print True
else: print B[2]
#########################################
# Question 4 - do not delete this comment
#########################################
str_lst = ["Python","is","The Best","language!!!!"] # Replace ??? with a list of strings.

# Write the code for question 4 below here.
lst=[]
for i in str_lst:
    if len(i)%2==0 and len(i)%3!=0:
        n=i
        l=0
        while len (n)>l:
            lst.append(n[l:l+2])
            l+=2
    elif len(i)%3==0:
        b=i
        h=0
        while len(b)>h:
               lst.append(b[h:h+3])
               h+=3
print lst
#########################################
# Question 5 - do not delete this comment
#########################################
rep_str = 'liiiiiiin' # Replace ??? with a string of your choice.
k = 5 # Replace ??? with a positive int of your choice.

# Write the code for question 5 below here.
l=-1
count=0
if k==0: print "Nothing found for the string " +str(rep_str) +'!'
elif k==1: print "The first substring of length 1 is " +str(rep_str[0]) +'!'
else:
    for i in rep_str:
        l+=1
        count+=1
        if k*i==rep_str[l:l+k]:
            print "The first substring of length "+str(k) +" is " +str(k*i)+"!"
            break
if count==len(rep_str): print "Nothing found for the string " +str(rep_str) +'!'
#########################################
# Question 6 - do not delete this comment
#########################################
mat = [[1,2,9],[20.22,4,7],[35,40.8437]] # Replace ??? with a list of lists of numbers (int/float).

# Write the code for question 6 below here.
n=0.0
for i in mat:
    small=i
    for i in small:
        if i>n: n=i
print n



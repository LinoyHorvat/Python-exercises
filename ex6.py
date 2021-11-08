#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(str1):
    if len(str1)==0:
        return str1
    else:
        return str1[-1] + reverse_string(str1[:-1])
print reverse_string("abc")

#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if lst==[]:
        return -1
    elif len(lst)==1:
        return lst
    else:
        if lst[0]<lst[1]:
            return find_maximum(lst[1:])
        else:
            lst.remove(lst[1])
            return find_maximum(lst)
print find_maximum([9,3,0,10])

#########################################
# Question 3 - do not delete this comment
#########################################
def frog_path_exists(n, short_jump, long_jump):
    if n<1:
        return False
    elif n==1:
        return True
    else:
        op1=frog_path_exists(n-short_jump,short_jump,long_jump)
        op2=frog_path_exists(n-long_jump,short_jump,long_jump)
        op3=frog_path_exists(n-long_jump-short_jump,short_jump,long_jump)
        return op1 or op2 or op3

print frog_path_exists(10,3,2)

#########################################
# Question 4 - do not delete this comment
#########################################
def frog_longest_path(n, short_jump, long_jump):
    if n<1:
        return -float('inf')
    elif n==1:
        return 0
    else:
        op1=+1+frog_longest_path(n-short_jump,short_jump,long_jump)
        op2=+1+frog_longest_path(n-long_jump,short_jump,long_jump)
    return max(op1,op2)

print frog_longest_path(0,2,9)

#######################
# main code - do not delete this comment
# You can add more validation cases below
#########################

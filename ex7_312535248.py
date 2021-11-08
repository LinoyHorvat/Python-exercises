''' Exercise #7. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def Q(n, memo=None):
    if n < 3:
        return 1
    if memo == None:
        memo = {}
    memo_key=(n)
    if memo_key not in memo:
        a=Q(n-1,memo)
        b=Q(n-a,memo)
        c=Q(n-2,memo)
        d=Q(n-c,memo)
        memo[memo_key]=b+d
    return memo[memo_key]
print Q(200)
#########################################
# Question 2 - do not delete this comment
#########################################
def frog_path_exists(n, short_jump, long_jump, memo=None):
    if n < 1:
        return False
    elif n == 1:
        return True
    if memo==None:
        memo={}
    memo_key=(n,short_jump,long_jump)
    if memo_key not in memo:
        op1 = frog_path_exists(n - short_jump, short_jump, long_jump,memo)
        op2 = frog_path_exists(n - long_jump, short_jump, long_jump,memo)
        memo[memo_key]= op1 or op2
    return memo[memo_key]
print frog_path_exists(99,2,4)
#########################################
# Question 3 - do not delete this comment
#########################################

def s_to_i(t):
    return int(t[1])
def sort_students(students_grades):
    sor=sorted(students_grades,key=s_to_i)
    return sor

x = [('jon', '88'), ('bran', '100'), ('arya', '93'), ('dan', '88')]
print sort_students(x)
#########################################
# Question 4 - do not delete this comment
#########################################
def search_student(grade, students_grades, start, stop):
    if start>=stop:
        print 'No relevant student was found'
        return None
    middle=(stop+start)/2
    if int(students_grades[middle][1])==grade:
        return students_grades[middle][0]
    elif grade<int(students_grades[middle][1]):
        return search_student(grade,students_grades,start,middle)
    else:
        return search_student(grade,students_grades,middle+1,stop)
x = [('jon', '80'), ('dan', '88'), ('arya', '93'), ('bran', '96')]
print search_student(96, x, 0, len(x))
#########################################
# Question 5 - do not delete this comment
#########################################
def pythy(rides, S, T, memo=None):
    if len(rides)==0 or S<0 or T<0:
        return 0
    if memo==None:
        memo={}
    key=(S,T,len(rides))
    if key not in memo:
        if T>rides[0][2] and S>rides[0][1]:
            memo[key]=max(rides[0][0]+pythy(rides[1:],S-rides[0][1],T-rides[0][2]),pythy(rides[1:],S,T,memo))
        else:
            memo[key]=pythy(rides[1:],S,T,memo)
        return memo[key]
rides = [(16, 1, 4), (17, 2, 9), (3, 17, 10)]
print pythy(rides, 100, 200)

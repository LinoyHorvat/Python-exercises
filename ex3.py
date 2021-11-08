#########################################
# Question 1 - do not delete this comment
#########################################
def flip_float_parts(num):
    str1=str(num).split(".")
    str2=str1[1]+'.'+str1[0]
    return float(str2)
print flip_float_parts(10.0)
#########################################
# Question 2 - do not delete this comment
#########################################
def sum_according_to_divisor(num_lst):
    list2=[]
    list3=[]
    list_else=[]
    for i in num_lst:
        if i % 2==0:
            list2.append(i)
        elif i%3==0 and i%2!=0:
            list3.append(i)
        else:
            list_else.append(i)
    a=sum(list2)
    b=sum(list3)
    c=sum(list_else)
    list1=[a,b,0,c]
    return list1
print sum_according_to_divisor([2,2,6,7])
#########################################
# Question 3 - do not delete this comment
#########################################
def final_digits_sum(num):
    while num>9:
        a=0
        n=str(num)
        for i in n:
            a=a+int(i)
        num=a
    return a       
print final_digits_sum(987654321)
def final_digits_sum_string(num_str, n):
    m=str(num_str)
    i=0
    lst1=[]
    while i<len(m)-n+1:
        lst1.append(final_digits_sum(m[i:i+n]))
        i+=1
    g=''
    for i in lst1:
        g=g+str(i)
    return g
print final_digits_sum_string(86586247, 3)
#################################
# Question 4 - do not delete this comment
#########################################
def switch_couples_in_lst(lst,couples_lst):
    i=0
    j=0
    while j<len(couples_lst):
        while i<len(lst):
            if lst[i]==couples_lst[j][0]:
                lst[i]=couples_lst[j][1]
                print lst
            elif lst[i]==couples_lst[j][1]:
                lst[i]=couples_lst[j][0]
                print lst
            i+=1
        j+=1
        i=0
    return 'sofi='+str(lst)
lst=[5,6,5,12]
couples_lst = [[5,12], [5,12]]
print switch_couples_in_lst(lst,couples_lst)
#########################################
# Question 5 - do not delete this comment
#########################################
def add_scalar_to_mat(mat, n):
    mat_rows=len(mat)
    mat_columns=len(mat[0])
    for i in range(mat_rows):
        for j in range(mat_columns):
            mat[i][j]=mat[i][j]+n
    return mat
print add_scalar_to_mat([[2,4,6,8,10,12],[2,4,6,8,10,12]], 2)
#########################################
# Question 6 - do not delete this comment
#########################################
def reshape_lst(lst, ncols):
    if len(lst)%ncols==0:
        i=0
        v=0
        n_lst=[]
        while i<(len(lst)/ncols):
            n_lst.append(lst[v:v+ncols])
            i+=1
            v+=ncols
        return n_lst
    else:
        return 'invalid row length'
print reshape_lst([1,2,3,4,5,6,7,8,9,10,11,12],2)
#########################################
# Question 7 - do not delete this comment
#########################################
def map_names_to_grades(names, grades):
    d={}
    i=0
    while i<len(names):
        d[names[i]]=grades[i]
        i+=1
    return d
print map_names_to_grades(["Yossi", "Yafa", "Moti"], [100, 95, 97])
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

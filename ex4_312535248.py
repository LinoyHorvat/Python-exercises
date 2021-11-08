#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_element(lst):
    dic={}
    lst2=[]
    for i in lst:
        n=dic.get(i,0)
        n+=1
        dic[i]=n
    if lst==[]:
        return []
    else:
        lst3=dic.keys()
        s_lst3=sorted(lst3,key=dic.get,reverse=True)
        lst2.append(s_lst3[0])
        lst4=dic.values()
        s_lst4=sorted(lst4,reverse=True)
        m=1
        for i in s_lst4:
            if s_lst4[0]==s_lst4[m]:
                lst2.append(s_lst3[m])
                m+=1
        return lst2             
print most_popular_element(["python", 2, 3, "python", 2, 2, "python"])
#########################################
# Question 2 - do not delete this comment
#########################################
def map_keys_to_values(keys, values):
    dic={}
    i=0
    for k in keys:
        if i<=len(keys):
            dic[k]=values[i]
            i+=1
    return dic
print map_keys_to_values(["a", "b", "a"], [15, 1, 6])
def rewrite_text(text, words1, words2):
    i=0
    n=0
    t=text.split()
    dic1=map_keys_to_values(words1, words2)
    for word in t:
        for k in dic1:
            if k==word:
                t[n]=dic1[k]
                i+=1
        n+=1
    j=0
    a=''
    while j<len(t)-1:
        a+=str(t[j])+' '
        j+=1
    return a+str(t[-1])
print rewrite_text("I know python and I like it", ["I", "python", "I", "I"], ["Yossi", "java", "Ronit", "Rina"])
#########################################
# Question 3 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    i=0
    dic={}
    while i<len(tuples_lst):
        if dic.has_key(tuples_lst[i][0]):
            dic[tuples_lst[i][0]].append(tuples_lst[i][1])
        else:
            dic[tuples_lst[i][0]]=[tuples_lst[i][1]]
        i+=1
    return dic
print courses_per_student([("Rina", "Math"), ("Yossi", "Chemistry"), ("Riki", "python"), ("Rina", "python"), ("Yossi", "biology")])

def swap_students_courses(students_dict):
    lst=students_dict.values()
    lst2 = []
    print lst2
    for a in range(len(lst)):
        for b in range(len(lst[a])):
            lst2.append(lst[a][b].lower())
    dic={}
    for i in range(len(lst)):
        dic[lst2[i]]=[]
    for a in students_dict:
        for b in range(len(students_dict[a])):
            for c in dic:
                if students_dict[a][b].lower()==c:
                    dic[c]+=[a]
    return dic
print swap_students_courses({'Rina': ['Math', 'python'], 'Yossi': ['Chemistry', 'biology'], 'Riki': ['python']})

########################################
# Question 4 - do not delete this comment
#########################################
def sum_sparse_matrices(mat1, mat2):
    dic={}
    dic.update(mat1)
    dic.update(mat2)
    for i in mat1:
        for j in mat2:
          if i==j:
            dic[i]=dic[i]+mat1[i]           
    return dic   
d1 = {(0,1): 2, (3,5): 1, (3,3): -10}
d2 = {(0,1): -5, (3,3): 8}
print sum_sparse_matrices(d1, d2)
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

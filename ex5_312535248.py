#########################################
# Question 1 - do not delete this comment
#########################################
def copy_no_spaces(infile, outfile):
    infile = open(infile, "r")
    outfile=open(outfile,'w')
    for line in infile:
        for i in range(len(line)):
            if line[i]!=' ':
                outfile.write(line[i])
            elif line[i]==' ' or line[i+1]=='  ':
                outfile.write('')
    infile.close()
    outfile.close()
copy_no_spaces("/Users/admin/Desktop/ex5/demo1.txt","/Users/admin/Desktop/ex5/demo2.txt")
#########################################
# Question 2 - do not delete this comment
#########################################
def check_election(votes):
    try:
        votes1=[]
        for elem in votes:
            votes1.append([int(elem)])
        dic={}
        for num in votes:
            if num in dic:
                dic[num]=dic[num]+1
            else: dic.update({num:1})
        for k in dic.keys():
            if dic[k]==max(dic.values()):
                return k
    except ValueError:
        return -1
print check_election([1,1,1,2,2])
#######################################
 #Question 3 - do not delete this comment
#######################################
def get_csv_matrix(filename):
    filename=open(filename,'r')
    try:
        lst=[]
        for elm in filename:
            num=elm.replace('\r\n','').split(',')
            if num!='' :
                lst.append(num)
        row=lst[0]
        for l in lst:
            if len(l)!=len(row):
                return 'None'
                break           
        n=0
        m=0
        while m<len(lst):
            while n<len(lst[m]):
                if lst[m][n].isdigit():
                    lst[m][n]=float(lst[m][n])
                else:
                    w=lst[m][n]
                    lst.remove(w)
                    print lst
                n+=1
            m+=1
            n=0
        return lst
    except ValueError:
         return "None"
    finally:
             filename.close()
print get_csv_matrix("/Users/admin/Desktop/ex5/good.csv")
 #########################################
# Question 4 - do not delete this comment
#########################################
def find_word_in_file(word, filename):
    try:
        filename = open(filename,'r')
        i=0
        tuple1=()
        done=False
        for line in filename:
            word1=line.replace(',','').replace('.','').replace('?','').replace('!','').split()
            j=0
            for w in word1:
                if w.lower()==word.lower():
                    tuple1=(i+1,j+1)
                    done=True
                    break
                j+=1
            if done:
                break
            i+=1
        if len(tuple1)==0:
            return "None"
        else:
            return tuple1
    except IOError:
        return "File not found" 
print find_word_in_file("donald", "/Users/admin/Desktop/ex5/demo4.txt")

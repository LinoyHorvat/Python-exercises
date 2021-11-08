import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import os
#########################################
# Question 1 - do not delete this comment
#########################################
def load_training_data(filename):
    '''
    This functions loads a table from file and returns 3 arrays containing its data, its column headers and its row headers
    :param filename: a filename containing the table to be read
    :return: data - an two dimensional array containing the values
             column_names - a one dimensional array containing column headers
             row_names - a one dimensional array containing row headers
    '''
    f= open(filename, 'r')
    header_line = f.readline()
    header_line = header_line.strip(',\n')
    column_names = header_line.split(',')
    mat= []
    row_names = []
    for line in f:
        tokens = line.split(',')
        row_names.append(tokens[0])
        values = [float(n) for n in tokens[1:]]
        mat.append(values)
    f.close()
    row_names = np.asarray(row_names)
    column_names = np.asarray(column_names)
    column_names=[i.strip() for i in column_names]
    data = np.asarray(mat,dtype=float)
    return data, column_names,row_names
#########################################
# Question 2 - do not delete this comment
#########################################
def get_highest_weight_loss_trainee(data, column_names, row_names):
    loss = np.array(data[:, 0] - data[:, -1])
    i=np.argmax(loss)
    return row_names[i]
#########################################
# Question 3 - do not delete this comment
#########################################
def get_diff_data(data, column_names, row_names):
    a=np.zeros(data.shape)
    a[:,1:]=data[:,0:-1]
    b=np.zeros(data.shape)
    b[:,1:]=data[:,1:]
    return b-a
#########################################
# Question 4 - do not delete this comment
#########################################
def get_highest_loss_month(data, column_names, row_names):
    mat=get_diff_data(data, column_names, row_names)
    sum_loss=-np.array(sum(mat[:]))
    i = np.argmax(sum_loss)
    return column_names[i]
#########################################
# Question 5 - do not delete this comment
#########################################
def get_relative_diff_table(data, column_names, row_names):
    mat = get_diff_data(data, column_names, row_names)
    d=data[:,:-1]
    m=mat[:,1:]
    return m/d
#########################################
# Question 6 - do not delete this comment
#########################################
def compute_bmi(weight_data, weight_row_names,height_data, height_row_names):
    weight_row_names = list(weight_row_names)
    height_row_names = list(height_row_names)
    a = np.zeros(len(height_data), dtype=int)
    for i in range(len(weight_data)):
        a[i] = height_row_names.index(weight_row_names[i])
    height_row_names = np.asarray(height_row_names)
    height_row_names = height_row_names[a]
    height_data = height_data[a]
    weight_row_names = np.asarray(weight_row_names)
    bmi = weight_data/ (height_data/100)**2
    return  bmi
#########################################
# Question 7 - do not delete this comment
#########################################
def count_successfull_trainees(bmi_data):
    f=bmi_data[:,0]
    l=bmi_data[:,-1]
    b=np.logical_or(f>25,f<18.5)
    a=np.logical_and(l<25,l>18.5)
    i=0
    j=0
    count=0
    for n in b:
        if n==a[i]:
            count+=1
        i+=1
    return count
######################################################################
######################################################################
######################################################################
############################## Part B ################################
######################################################################
######################################################################
######################################################################
def show_image(im):
    plt.figure()
    plt.imshow(im, plt.cm.gray)
    plt.show()
#########################################
# Question 1 - do not delete this comment
#########################################
def reduce_image(img_filename, k):
    im=misc.imread(img_filename)
    new_n=im.shape[0]/k
    new_m=im.shape[1]/k
    new_mat=np.zeros(new_n,new_m)
    for j in range(new_mat.shape[1]):
        for i in range(new_mat.shape[1]):
            curr_range_l=range(j*k,min(j+1)*k,im.shape[0])
            curr_range = range(i * k, min((j + 1) * i, im.shape[1]))
            new_mat[:,j]=im[:,curr_range].mean()
    return new_mat
#########################################
# Question 2 - do not delete this comment
#########################################
def image_negative(img_filename):
    im=misc.imread(img_filename)
    new_mat=255-im
    return new_mat
#########################################
# Question 3 - do not delete this comment
#########################################
def create_chess_board(n, m, k):
    o=np.tile(np.array(255),(k,k))
    i=np.tile(np.array(0),(k,k))
    j=np.hstack((o,i))
    i=np.hstack((i,o))
    a=np.vstack((j,i))
    c = np.tile(a,(n/2,m/2))
    return c 
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

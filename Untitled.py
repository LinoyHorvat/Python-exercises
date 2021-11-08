import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

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
    data = np.asarray(mat,dtype=float)
    return data, column_names,row_names
    pass

#########################################
# Question 2 - do not delete this comment
#########################################
def get_highest_weight_loss_trainee(data, column_names, row_names):
    total_loss = data[:,-1]-data[:,0]
    index = np.argmin(total_loss)
    highest_name = row_names[index]
    return highest_name
    pass

#########################################
# Question 3 - do not delete this comment
#########################################
def get_diff_data(data, column_names, row_names):
    data_new1 = np.zeros(data.shape,dtype=float)
    data_new1[:,1:] = data[:,:-1]
    data_new1[:,0] = data[:,0]
    data_new1 = data - data_new1
    return data_new1
    pass

#########################################
# Question 4 - do not delete this comment
#########################################
def get_highest_loss_month(data, column_names, row_names):
    diff_mat = get_diff_data(data, column_names, row_names)
    column_sum = diff_mat.sum(axis=0)
    index = np.argmin(column_sum)
    best_loss_month = column_names[index]
    return best_loss_month
    pass


#########################################
# Question 5 - do not delete this comment
#########################################
def get_relative_diff_table(data, column_names, row_names):
    diff_mat = get_diff_data(data, column_names, row_names)
    data_mat = diff_mat /(data)
    return data_mat

#########################################
# Question 6 - do not delete this comment
#########################################
def compute_bmi(weight_data, weight_row_names,height_data, height_row_names):
    perm = np.zeros(len(height_data), dtype=int)
    height_row_names = list(height_row_names)
    weight_row_names = list(weight_row_names)
    for i in range(len(height_data)):
        perm[i] = height_row_names.index(weight_row_names[i])
    height_row_names = np.asarray(height_row_names)
    weight_row_names = np.asarray(weight_row_names)
    height_row_names = height_row_names[perm]
    height_data = height_data[perm]
    bmi_data = weight_data/ (height_data/100)**2
    return  bmi_data
    pass
data, column_names, row_names = load_training_data("/Users/admin/Desktop/ex10/weight_input.csv")
height_data, height_column_names, height_row_names = load_training_data("/Users/admin/Desktop/ex10/height_input.csv")
bmi_data = compute_bmi(data, row_names, height_data, height_row_names)
print bmi_data

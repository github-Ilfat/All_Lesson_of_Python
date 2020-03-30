# Среднее арифметическое
list_temp = [1,5,2,'12',6,12.2,2,53]

sum = 0
if(len(list_temp)>0):
    for el in list_temp:
        sum+=float(el)
    print(sum/len(list_temp))
else:
    print('List is empty!')
def transpose(matrix1, matrix2): 
    for i in range(len(matrix1[0])): 
        row =[] 
        for item in matrix1: 
            row.append(item[i]) 
        matrix2.append(row) 
    return matrix2 
  
matrix1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]] 
matrix2 = [] 
print(transpose(matrix1, matrix2)) 
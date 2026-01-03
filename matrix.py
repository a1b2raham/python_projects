
matrix=[]

def print_matrix(matrix):
    print()
    for l in range(len(matrix)):
        for k in range(len(matrix[0])):
            if matrix[l][k]== -0.0:
                print(0,end="|")
            else:
                print(matrix[l][k],end="|")
        print()
        
    print()
def find_deter(matrix):
    
    deter=float(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
    return deter


def find_determinant(deter_list,matrix):
    determinant = float(matrix[0][0]*deter_list[0] + matrix[0][1]*deter_list[1] + matrix[0][2]*deter_list[2])
    return determinant
    
def cofactor_matrix(matrix):
    cofactor=[]
    var=1
    chk=True
    for s in range(3):
        empty=[]
        for g in range(3):
            
            first = [sublist[:] for sublist in matrix]
                
            del first[s]
            for sublist in first:
                sublist.pop(g)
        
            empty.append(float(var*find_deter(first)))
            var=var*-1
        if chk:
            determinant = find_determinant(empty,matrix)
            chk = False
            
        cofactor.append(empty)

        
    return cofactor,determinant
     
def transpose_matrix(matrix):
    transpose=[sublist[:] for sublist in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[i][j]=float(matrix[j][i])
            
        
    return transpose

def find_inverse(adjoint,deter):
    inverse=[]
    for element in adjoint:
        a=[]
        a=[round(float(x/deter),2) for x in element]
        
        inverse.append(a)
        
    return inverse

def cross(matrixa,matrixb):
    i=len(matrixa)
    x= len(matrixb)
    j= len(matrixa[0])
    y= len(matrixb[0])
    matrix=[]
    if j!=x:
        print("the given matrixs cannot be cross multiplied")
        return
    else:
        for n in range(i):
           a=[] 
           for k in range(y):
              temp=0
              for l in range(j):
                  temp += matrixa[n][l]*matrixb[l][k]
              a.append(temp)  
           matrix.append(a)
    print_matrix(matrix)
           
def main(matrix):
    print("The given program can calculate the cofactor , adjoint and inverse matrix of a given matrix\n")
    print("Please enter the elements of matrix \n")
    chk= True
    while chk:
        
        print()
        for i in range(3):
            a=[]
            j=0
            while j<3:
                  
                  try:
                      element = float(input(f"enter element in row {i+1} and column {j+1}: "))
                  except:
                      print("\nPlease enter an number \n ")
                      continue
                  a.append(float(element))
                  j=j+1              
            matrix.append(a)
        print("\nThe given matrix is: ")        
        print_matrix(matrix)        
        cofactor,determinant=cofactor_matrix(matrix)
        
        adjoint=transpose_matrix(cofactor)
        
        print("The cofactor matrix of the given matrix is: ")
        print_matrix(cofactor)

        print("The adjoint matrix of the given matrix is: ")
        print_matrix(adjoint)
        print(f"The determinant of the given matrix is {determinant} \n")
        if determinant==0:
            print("determinant is zero, unable to find inverse \n")
        else:
            print("The inverse matrix of the given matrix is: ")
            print_matrix(find_inverse(adjoint,determinant))
        
        cross(matrix,transpose_matrix(matrix))
        while True:
                
            out=input("Do you wish to continue(y/n): ").lower()
            if out=="n":
                chk= False
                break
            elif out== "y":
                break
            else:
                print(" invalid response")        
            
            
    

main(matrix)








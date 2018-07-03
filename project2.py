def dot(vector01,vector02):
  '''
  This function calculates the dot product of the two vectors. This algorithim makes sure the lengths are equal to each other and if they do not equal each other, then the function does not run the code. This takes the lengths of vector01 and vector02 and multiplies each element together and creates a new list. This then takes the list and each element in the list and adds them together and comes up with a single integer.
  '''
  C = [ ]
  #C is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
    #If the lengths of the vectors are not equal to each other, then the algorithim does not compute and returns none.
  for i in range(len(vector01)):
    if type(vector01[i]) != int and type(vector01[i]) != float and type(vector01[i]) != complex:
      print('error')
      return None
    if type(vector02[i]) != int and type(vector02[i]) != float and type(vector02[i]) != complex:
      print('error')
      return None
    A.append(vector01[i] - vector02[i])
  #For the length of the vector i.
    C.append(vector01[i] * vector02[i])
    #multiplies each element together and creates a list C.
  D = 0
  #A new integer D is made.
  for i in range(len(C)):
    D = D + C[i]
  return D
  #The function then adds the elements in C toghether to get a single integer, D.

def vecSubtraction(vector01,vector02):
  '''
  This function adds to vectors together. This algorithim makes sure the lengths of the vectors are equal to each other. If the vector lengths are not equal to each other, then this function does not compute the outcome. This takes the vectors and subtract each element from the list and creates a single vector.
  '''
  A = [ ]
  #A is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
    #If the lengths of the lists vector01 and vector02 do not equal each other, then this prints an error and returns none.
  for i in range(len(vector01)):
    if type(vector01[i]) != int and type(vector01[i]) != float and type(vector01[i]) != complex:
      print('error')
      return None
    if type(vector02[i]) != int and type(vector02[i]) != float and type(vector02[i]) != complex:
      print('error')
      return None
    A.append(vector01[i] - vector02[i])
    #This subtracts the lengths of vector01 and vector02 and adds each element of the list together.
  return A
  #This returns the list A.

def scalarMultVec(scalar,vector):
  '''
  This function takes a scalar and a vector and multiplies them together to create a single vector. If the scalar is equal to a list, the function does not run and computes and error. This takes the scalar and multiplies each element in the vector. This function 
  then creates a new vector.
  '''
  if type(scalar) != int and type(scalar) != float and type(scalar) != complex:
    print('error')
    return None
    #If the scalar is not an interger, float, or complex, it will return none.
  A = [ ]
  #A is an empty list.
  for i in range(len(vector)):
    if type(vector[i]) != int and type(vector[i]) != float and type(vector[i]) != complex:
      print('error')
      return None
    #For the length of the vector.
    A.append(vector[i] * scalar)
    #For each element in length i, multiply by the scalar.
  return A
  #This creates a new list for A and returns A.

def norm2(vector):
  '''
  This function calculates the two norm. The result is the norm of the vector. This takes the absolute value of every element and squares them. This adds the result of the after each element is squared. Then, the function takes the square root of the result to return
  the two norm.
  '''
  result = 0
  for i in range(len(vector)):
    if type(vector[i]) != int and type(vector[i]) != float and type(vector[i]) != complex:
      print('error')
      return None
    result = result +abs(vector[i])**2
    #Takes each element and squares the element and adds them together.
  result = result**.5
  #This takes the result and raises it to the half power, which is equivalent to a square root.
  return result

def modGramSchmidt(A):
  '''
  This function calculates the modified Gram Schmidt process. This takes in the matrix A and computes q and r. This normalizes the matrix A to get q. Then, this does the dot product to get a scalar. Then, the scalar is multiplied with q columns and creates a new row of A. Then, this functions appends the list for q and takes each element of r that is calculated and put each r in a matrix.
  '''
  n = len(A)
  m = len(A[0])
  r = [[0]*n for row in range(n)]
  q = [ ]
  for i in range(n):
    for j in range(m):
      if type(A[i][j]) != int and type(A[i][j]) != float and type(A[i][j]) != complex:
        print('error')
        return None
    r[i][i] = norm2(A[i])
    #taking the 2 norm of the column A.
    scalar = 1/r[i][i]
    #creating a scalar
    qi = scalarMultVec(scalar,A[i])
    #qi is a temporary variable. This is multiplying each element of A by the scalar. 
    q.append(qi)
    #This is appending the list of q together.
    for j in range(i + 1,n):
      r[j][i] = dot(q[i],A[j])
      B = scalarMultVec(r[j][i],q[i])
      #This is a temporary variable for the scalarMultVec function.
      A[j] = vecSubtraction(A[j],B)
      #
  return [q, r]

A = [[1,1,1,1,1,1,1,1,1,1],[.55,.6,.65,.7,.75,.8,.85,.9,.95,1],[.3025,.36,.4225,.49,.5625,.64,.7225,.81,.9025,1],[.166375,.216,.274625,.343,.421875,.512,.614125,.729,.857375,1]]

qr = modGramSchmidt(A)

def transposeMatVec(q,y):
  '''
  This function takes the transpose of the matrix q and by the vector y. This takes the matrix q and switches the rows and columns. Then, this takes the matrix q and multiples by vector y to get a new vector C.
  '''
  C = []
  print(len(q))
  print(len(y))

  #This is the empty set C that is being solved for
  for i in range(len(q)):
    for j in range(len(q[0])):
      if type(q[i][j]) != int and type(q[i][j]) != float and type(q[i][j]) != complex:
        print('error')
        return None
  #This iterates the block executing the length of the matrix.
    total = 0
    for j in range(len(y)):
      if type(y[j]) != int and type(y[j]) != float and type(y[j]) != complex:
        print('error')
        return None

    for j in range(len(q)):
      for i in range(len(q[0])):
        total = total + (q[j][i] * y[j])
      #This is multiplying the transpose matrix and vector toghether and adding the total to the product.
    C.append(total)
    #This adds the product together.
  return C
  #This is returning the data to make the vector C
y = [1.102,1.099,1.017,1.111,1.117,1.152,1.265,1.380,1.575,1.857]
C = transposeMatVec(qr[0],y)

def vecDiviUpperTriMat(C,r):
  '''
  This takes the matrix r and the answer C to solve for x. This takes the reverse itiration of r. For j, this starts at the element i + 1 and goes to length C. This takes the element in C and subtracts the product of the matrix times the element in C. Then, divide the answer by the diagonal of r. This then returns the vector x that solves the equation rx=C.
  '''

  x = C
  #Defining x as C.
  for i in reversed(range(len(r))):
    for j in range(r[0]):
      if type(r[i][j]) != int and type(r[i][j]) != float and type(r[i][j]) != complex:
        print('error')
        return None
  #This iterates the list backwards.
    for j in range(i + 1, len(C)):
      if type(C[j]) != int and type(C[j]) != float and type(C[j]) != complex:
        print('error')
        return None
      x[i] = x[i] - (r[i][j] * x[j])
      #Matrix r multiplied by C and then vector C subtracted by the product.
    x[i] = x[i] / r[i][i]
    #Takes result from the previous answer and divides by the diagonal of r.
  return x
#returns the answer x.




print(vecDiviUpperTriMat(C,qr[1]))

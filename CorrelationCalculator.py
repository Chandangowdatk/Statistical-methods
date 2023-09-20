import math

def sumofSquares(copy):
    temp = 0
    for i in copy:
        temp += i**2
    return temp

def zfinder(xcopy, ycopy):
    zList = []
    temp = 0
    for i in range(len(xcopy)):
        temp = xcopy[i] - ycopy[i]
        zList.append(temp)
    return zList

x = []
y = []
z = []

# Input a single line of integers separated by spaces
input_line = input("Enter values of x separated by spaces: ")
# Split the input line by spaces and convert the parts to integers using map()
x = list(map(int, input_line.split()))
input_line = input("Enter values of y separated by spaces: ")
y = list(map(int, input_line.split()))

z = zfinder(x, y) 

sumXsquare = sumofSquares(x)
sumYsquare = sumofSquares(y)
sumZsquare = sumofSquares(z)

# variablese related to coefficient of correlation formula
meanX = sum(x)/len(x)
meanY = sum(y)/len(y)
meanZ = sum(z)/len(z)

sumSquareX = sumXsquare/len(x)-(meanX**2)
sumSquareY = sumYsquare/len(y)-(meanY**2)
sumSquareZ = sumZsquare/len(z)-(meanZ**2)

sqrtofX = math.sqrt(sumSquareX)
sqrtofY = math.sqrt(sumSquareY)

numerator = sumSquareX + sumSquareY - sumSquareZ
denominator = 2*sqrtofX*sqrtofY

coefficientOfCorelation = numerator / denominator

print("\u2211x: ",sum(x))
print("\u2211y: ",sum(y))
print("\u2211z: ",sum(z))

print("\u2211x²: ",sumXsquare)
print("\u2211y²: ",sumYsquare)
print("\u2211z²: ",sumZsquare)

print("x bar value: ", meanX)
print("y bar value: ", meanY)
print("z bar value: ", meanZ)

print("Summation square of x: ", sumSquareX)
print("Summation square of y: ", sumSquareY)
print("Summation square of z: ", sumSquareZ)

print("Coefficient of corelation: ", coefficientOfCorelation)

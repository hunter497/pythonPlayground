#Square an integer, the hard way
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

inputSquare = int(input("Please enter a number to square: "))
ansInput = 0
itersInputLeft = inputSquare
while (itersInputLeft != 0):
    ansInput = ansInput + inputSquare
    itersInputLeft = itersInputLeft - 1
print(str(inputSquare) + '*' + str(inputSquare) + ' = ' + str(ansInput))
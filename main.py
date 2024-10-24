import math

def circleAreaCalc():
  var=float(input("Enter the radius of the circle: "))
  var=pow(var,2)
  var=var*math.pi
  print(var)

def degreeToRadians():
  var=float(input("Enter the degree: "))
  var=math.radians(var)
  print(var)

def squareRoot():
  var=float(input("Enter the number to squareroot: "))
  var=math.sqrt(var)
  print(var)

def ceilAndFloor():
  var=float("Enter the number to round up and down: ")
  print("Ceil: ",math.ceil(var))
  print("Floor: ",math.floor(var))

def hypotenuse():
  var1=float(input("Enter 1 side of a right angle triangle: "))
  var2=float(input("Enter the other side of the right angle triangle: "))
  var1=pow(var1,2)
  var2=pow(var2,2)
  var=var1+var2
  var=math.sqrt(var)
  print(var)

def logCalc():
  var=float(input("Enter a number to find the natural log, the log of base 10 and log of base 2: "))
  print("Natural: ",math.log(var))
  print("Base 10: ",math.log(var,10))
  print("Base 2: ",math.log(var,2))

def trigCalc():
  var=float(input("Enter the angle in degrees to calc sin, cos and tan: "))
  var=math.radians(var)
  print("Sin: ",math.sin(var))
  print("Cos: ",math.cos(var))
  print("Tan: ",math.tan(var))

def powVs2Asterik():
  var=int(input("Enter a number to raise to the power of 2: "))
  print(pow(var,2))
  print(var**2)

def euclideanDistance():
  oneX=float(input("Enter the first var x coordinate: "))
  oneY=float(input("Enter the first var y coordinate: "))
  oneZ=float(input("Enter the first var z coordinate: "))
  twoX=float(input("Enter the second var x coordinate: "))
  twoY=float(input("Enter the second var y coordinate: "))
  twoZ=float(input("Enter the second var z coordinate: "))

  threeX=math.fabs(oneX-twoX)
  threeY=math.fabs(oneY-twoY)
  threeZ=math.fabs(oneZ-twoZ)

  threeX=pow(threeX,2)
  threeY=pow(threeY,2)
  threeZ=pow(threeZ,2)

  var=threeX+threeY+threeZ
  var=math.sqrt(var)
  print(var)

def greatestCommonDivider():
  var1=int(input("Enter the first integer number for the GCD: "))
  var2=int(input("Enter the second integer number for the GCD: "))
  print(math.gcd(var1,var2))

def mathComb():
  var1=int(input("How many variables are in the list: "))
  var2=int(input("How many variables do you want to pick at once from the list: "))
  print(math.comb(var1,var2))

def factorialOfInt():
  var=int(input("Enter a positive integer to find the factorial: "))
  print(math.factorial(var))

init=input("Enter the function you want to use: ")

match init:
  case "1":
    circleAreaCalc()
  case "2":
    degreeToRadians()
  case "3":
    squareRoot()
  case "4":
    ceilAndFloor()
  case "5":
    hypotenuse()
  case "6":
    logCalc()
  case "7":
    trigCalc()
  case "8":
    powVs2Asterik()
  case "9":
    euclideanDistance()
  case "10":
    greatestCommonDivider()
  case "11":
    mathComb()
  case "12":
    factorialOfInt()
    

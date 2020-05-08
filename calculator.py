import math
def raise_to_power(base_num,pow_num):
 return base_num**pow_num
def inverse(num):
 k = float(1/num)
 return k
def fact(n,r):
 r=1
 while n>1:
  r *= n
  n = n-1
 return r
def divide(num1,num2):
 if num2!= 0:
  return num1/num2
def add(num1,num2):
 return num1+num2
def sub(num1,num2):
 return num1-num2
def mul(num1,num2):
 return num1*num2

try:
	num1 =float(input("enter the 1st number "))
	op = input("enter an operator : ")
	num2 =float(input("enter the 2nd number "))
	if op == "+":
 		print(add(num1,num2))
	elif op == "-":
  		print(sub(num1,num2))
	elif op == "*":
 		print(mul(num1,num2))
	elif op == "/":
  		print(divide(num1,num2))
	elif op == "%":
 		print(num1 % num2)

	elif op == "^":
		p=int(num1)
		q=int(num2)
		print(raise_to_power(p,q))
	elif op == "!":
 		if num1 == num2:
  			print(fact(num1,num2))
	 	else:
  			print("num1 and num2 should be equal ")
	elif op =="r":
		if num1 == num2:
			print(math.sqrt(num1))
		else:
			print("num1 and num2 should be equal ")

	elif op =="ln":
 		if num1 == num2:
  			print(math.log(num1))
	 	else:
  			print("num1 and num2 should be equal ")
	
	elif op =="sin":
 		if num1 == num2:
  			print(math.sin(num1))
 		else:
  			print("num1 and num2 should be equal ")
	elif op =="cos":
 		if num1 == num2:
  			print(math.cos(num1))
 		else:
  			print("num1 and num2 should be equal ")
	elif op =="tan":
 		if num1 == num2:
  			print(math.tan(num1))
 		else:
  			print("num1 and num2 should be equal ")
	elif op =="inv":
 		if num1 == num2:
  			print(inverse(num1))
 		else:
  			s = divide(num1,num2)
  			print(inverse(s))
	elif op=="ncr":
  		a = fact(num1,1)
  		b = fact(num2,1)
  		c = num1-num2
  		d = fact(c,1)
  		e = b*d
  		print(a/e)
	elif op=="sin_degree":
 		if num1 == num2:
  			print(round(math.sin(math.radians(num1)),1))
 		else:
  			print("num1 and num2 should be equal")
	elif op=="cos_degree":
 		if num1 == num2:
  			print(round(math.cos(math.radians(num1)),1))
 		else:
  			print("num1 and num2 should be equal")
	elif op=="tan_degree":
 		if num1 == num2:
  			print(round(math.tan(math.radians(num1)),1))
 		else:
  			print("num1 and num2 should be equal")
	elif op=="abs":
 		if num1==num2:
  			print(abs(num1))
 		else:
  			print(abs(num1))
  			print(abs(num2))
	elif op =="pi":
 		if num1==num2:
  			q=math.pi
  			print(q)
  			op1 = input("enter the operation to be performed with pi: ")
  			if op1 == "*":
  				print(mul(num1,q))
  			if op1 == "/":
   				print(divide(num1,q))
  			if op1 =="inv":
  				s = divide(num1,q)
  				print(inverse(s))
  			if op1 == "+":
   				print(add(num1,q))
  			if op1 == "-":
		   		print(divide(num1,q))
	elif op =="e":
 		print("the value of e is ")
 		print(math.e)
 		if num1==num2:
  			print(math.exp(num1))

except Exception as e:
		print(e)


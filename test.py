# C3 q 1

#hours = int(input("enter hours "))
#rate = float( input ("enter rate "))
# overtime = 0
# new_overtime = 0 
# old_pay = 0
# time = 0
# if hours > 40: 
# 	overtime = (hours - 40)
# 	new_overtime = overtime * (1.5 * rate)
# 	time = (hours - overtime) * rate
# 	pay = time + new_overtime
# 	print (pay)
# else: 
# 	pay = hours * rate 


# x= 0 
# count = 0 
# total = 0 
# average = 0 
#x= input("enter something") 
# while x != "done" :
# 	x= input("enter something") 
# 	try: 
# 		if x == int(x): 
# 			count = count + 1
# 			totatl = x + total
# 	average = total / count
# 	except: 
# 		print("you must enter a number") 



# x = []
# y = ""
# while y != "Done": 
# 	y = (input("enter number and say stop when you are done "))
# 	if y == "done":
# 		break
# 	else:
# 		x.append(y)
# maxi = 0 
# mini = 0 
# for each in x: 
# 	if maxi >= int(each): 
# 		maxi = each
# 	elif mini <= int(each):
# 		mini = each
# print (maxi)
# print (mini)



# x = input ("enter a string ")
# y = x.split()
# print (y)
# for each in y:
# 	for letter in each:
# 		print(letter)


# fruit = "fruit"
# index = len(fruit) - 1
# while index >= 0:
# 	letter = fruit[index]
# 	print (letter)
# 	index = index - 1

# x = input('press y to stop')
# z = 0
# while x != 'y':
# 	x = input('press y to stop')
# 	print (z)

# x = [] 
# while True: 
# 	y = input("enter a number and done when true ")
# 	try:
# 		x.append(float(y))
# 	except: 
# 		break
# maxi = max(x)
# print (maxi) 
# mini = min(x)
# print (mini)

# hours = int(input("enter hour"))
# rate = float(input("enter hour"))
# gross = hours * rate
# new = str(gross)
# print('%.2f' % gross)


# x = [] 
# y = ""
# while y != "done":
# 	y = input("enter number and say done when done")
# 	try:
# 		y1 = int(y)
# 	except:
# 		continue
# 	x.append(y1)
# # mini = 0 
# # maxi = 0 
# # for each in x:
# # 	if each <= mini:
# # 		mini = each
# # 	elif each >= maxi:
# # 		maxi = each
# # print (mini)
# # print (maxi)
# print(max(x))
# print(min(x))


# #CHAPTER 9 E3
# import string
# fname = 'mbox-short.txt'
# try:
# 	x = open(fname)
# except:
# 	print("file cannot be opened")
# 	exit()
# counts = dict()
# for line in x:
# 	line = line.rstrip()
# 	for each in line:
# 		if each.startswith('From'): 
# 			continue 
# 		word = line.split()
# 		if word not in counts:
# 			counts[word] = 1
# 		else:
# 			counts[word] += 1
# print (counts)




#-------------------------------------------------------

#CHAPTER 2 E 3 
# hours = int(input("enter a number "))
# rate = float(input("enter a rate "))
# pay = hours * rate 
# print (pay)


# CHAPTER 2 E 4
# width = 17 
# height =  12
# print (width//2)   # 8 
# print (width/2.0)    # 
# print (height/3)   # 



#CHAPTER 3 E 1 
# hours = int(input("enter a number "))
# rate = float(input("enter a rate "))
# overtime = 0
# new_rate = 0 
# pay = 0
# if hours > 40: 
# 	overtime = hours - 40
# 	new_rate = overtime* (1.5*10)
# 	pay = new_rate + (40*rate)
# else: 
# 	pay = hours * rate 
# print (pay)



#CHAPTER 3 E 2
# try:
# 	hours = int(input("enter a number "))
# 	rate = float(input("enter a rate "))
# 	overtime = 0
# 	new_rate = 0 
# 	pay = 0
# 	if hours > 40: 
# 		overtime = hours - 40
# 		new_rate = overtime* (1.5*10)
# 		pay = new_rate + (40*rate)
# 	else: 
# 		pay = hours * rate 
# 	print (pay)
# except: 
# 	print("Error, please enter numerical value")

#CHAPTER 4 E 6 

# def countepay(hours,rate):
# 	hours = int(input("enter a number "))
# 	rate = float(input("enter a rate "))
# 	overtime = 0
# 	new_rate = 0 
# 	pay = 0
# 	if hours > 40: 
# 		overtime = hours - 40
# 		new_rate = overtime* (1.5*10)
# 		pay = new_rate + (40*rate)
# 	else: 
# 		pay = hours * rate 
# 	return (pay)

# print (countepay(45,10))

#CHAPTER 5
# x = []
# y = ""
# while y != "done": 
# 	y = (input("enter number and say stop when you are done "))
# 	if y == "done":
# 		break
# 	else:
# 		x.append(int(y))
# maxi = x[0] 
# mini = x[1]
# for each in x: 
# 	if maxi >= int(each): 
# 		maxi = each
# 	elif mini <= int(each):
# 		mini = each
# print (maxi)
# print (mini)

#CHAPTER 5	

# y = ""
# total = 0 
# count = 0
# average = 0
# while y != "done": 
# 		y = (input("enter number and say stop when you are done "))
# 		if y == "done":
# 			break
# 		else:
# 			try:
# 				total = int(y) + total
# 				count +=1
# 				average = count / total
# 			except:
# 				print ("enter a number")

#or

# nums= []
# total = 0
# count = 0
# while True:
# 	n = input("enter a number")
# 	if n == 'done':
# 		break
# 	try:
# 		nums.append(int(n))
# 		total = total +int(n)
# 		count +=1 
# 	except:
# 		print ('invalid input')
# print (total)
# print(count)
# print (total/count)
		


#CHAPTER 6 E 1 
# fruit = "fruit"
# index = len(fruit) - 1
# while index >= 0:
# 	letter = fruit[index]
# 	print (letter)
# 	index = index - 1

# x = input('press y to stop')
# z = 0
# while x != 'y':
# 	x = input('press y to stop')
# 	print (z)

#CHAPTER 8 E 6 
# x = []
# y = (input("enter a list of numbers and put done when finished ")
# while True:
# 	y =input("enter a number ")
# 	if y == 'done':
# 		break
# 	try:
# 		x.append(int(y))
# 	except:
# 		print ("enter a number or done")
# print (max(x))
# print (min(x))



# #CHAPTER 10 E 3
# import string
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# counts = dict()
# for line in fhand:
#     line = line.rstrip()
#     line = line.translate(line.maketrans('','',string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#     	for letter in word:
#         	if letter not in counts:
#         		counts[letter] = 1
#         	else:
#         		counts[letter] += 1
# print (counts)

# import re
# x = "2002-19-12"

# y = re.findall('\d+[-/]\d+[-/]\d+', x)
# print (y)





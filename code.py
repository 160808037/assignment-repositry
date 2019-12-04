# x = 20
# x += 1
# print(x)
# a = input("what is your a:  ")
# b = input("what is your b:  ")
# c= ((int(a)**2) + (int(b)**2))**0.5
# print(c)
# a= int(input("what is your a:  "))
# b= int(input ("what is your b: " ))
# c= int(input ("what is your c: "  )
# x1= (-b + ((b**2)-(4*a*b))**0.5)/2*a
# x2= (-b - ((b**2)-(4*a*b))**0.5) /2*a
# age = int(input("please enter your age : "))

# can_drink = age >= 20
# can_pay_tax =age>= 18
# can_take_pension =age > 60
# can_retire =age ==40

# statement = f"can drink:{can_drink}\ncan pay tax:{can_pay_tax}\ncan take pension:{can_take_pension}\ncan retire:{can_retire}"
# print(statement)
# characters_name= "paul"
# print (characters_name+" is my real name")
# phrase ="giraffe academy"
# print(phrase.replace("giraffe", "elephant"))
# my_num= 2
# print(abs(my_num))
# print(pow(4, my_num))
# print(round(3.7))
# name= input("enter our name:")
# age= input("enter our age:")

# print("hello "+name+"!" "you're "+ age+".")
# num1 = input("enter a number")
# num2 = input("enter another number")
# result = int(num1) + int(num2)
# print(result)
# num1 = input("enter a number")
# num2 = input("enter another number")
# result = float(num1) + float(num2)
# print(result)
# colour= input("enter a colour:")
# plural_noun=input("enter a plural noun:")
# celebrity= input("enter A CELEBRITY:")
# print("roses are " + colour)
# print(plural_noun + " are blue")
# print("i love " +celebrity)
# lucky_numbers =["4" , "8" ,"16" ,"23", "42"]
# friends = ["kevin", "karen", "jim"]
# friends.extend(lucky_numbers)
# print(friends)
# lucky_numbers =["4" , "8" ,"16" ,"23", "42"]
# friends = ["kevin", "karen", "jim"]
# friends.append("creed")
# print(friends)lucky_numbers =["4" , "8" ,"16" ,"23", "42"]
# friends = ["kevin", "karen", "jim"]
# friends.insert(1, "kelly")
# print(friends)
# friends = ["kevin", "karen", "jim"]
# friends.remove("jim")
# print(friends)
# friends = ["kevin", "karen", "jim"]
# print(friends.count("jim"))friends = ["kevin", "karen", "jim"]
# friends = ["kevin", "karen", "jim"]
# friends[0]='joseph'
# print(friends)
# friends.sort()
# print(friends)friends = ["kevin", "karen", "jim"]
# lucky_numbers =[43 , 8 ,16 ,23]
# friends = ["kevin", "karen", "jim"]
# lucky_numbers.reverse()
# print(lucky_numbers)
# coordinates =[(4, 5),(6, 7)]
# print(coordinates[0:2])
# def say_hi(name , age=13):
#     print("hello " + name + " you are ", + age)


# say_hi( "mike")
# say_hi( "steve")   
# def cube(num) :
#     return num*num*num

# result=cube(4)
# print(result)    

# i wake up
# if i'm hungry 
#     i eat breakfast.

# i leave my house 
# if it's cloudy
#     i bring an umbrella
# otherwise 
#     i bring sunglasses.

# im at a restaurant
# if i want meat 
#      i order a streak
# otherwise if i want pasta
#      i orde spaghetti & meatballs
# otherwise
#      i order a salad.
# is_male = False

# if is_male:
#     print("you are a male")
# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("you are a male and tall")
# elif is_male and not is_tall:
#     print("you are a short male")
# elif not (is_male) and not is_tall:
#     print("you are not male and not tall")
# else:
#     print("you are either not male or not tall or both")

# word =input("please enter word:")

# reversed_word = word[::-1]

# print(f"{word} is a palindrome : {word ==reversed_word} ")
# word =input("please enter word:").lower()

# response = 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word
# print(f"{word} contains vowels :{response}")
# a = int(input("type a number:"))
# b = int(input("type a number:"))
# c = int(input("type a number:"))
# d = int(input("type a number:"))
# x = ((a*d) + (c*b))
# y = (b*d)
# print(f"{x}/{y}")


# fraction = input("enter a fraction in the format a/b + c/d and press enter to solve :")
# splitted_fraction = fraction.split("+")
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]

# splitted_frac1 = frac1.split("/")
# splitted_frac2 = frac2.split("/")

# a= int(splitted_frac1[0])
# b= int(splitted_frac1[1])
# c= int(splitted_frac2[0])
# d= int(splitted_frac2[1])

# print(fraction)
# print(splitted_fraction)
# print(splitted_frac1)
# print(splitted_frac2)
# x = ((a*d) + (c*b))
# y = (b*d)
# print(f"{x}/{y}")
# dog = input("please input your dob in the format yyyy-mm-dd" )
# year= dog.split("-")
# print(year[1])
# print(1,2,3,sep="\n")
# print(1,2,3,sep="\n", end = "-")
# print(1,2,3,sep="\n")
# print("new line")
# file= open("my_data.csv", 'w')
# print(1,2,3,4, file = file,sep =",")
# file= open("my_data.csv", 'w')
# print("Name
# 
# ","Age","State","Due",file= file,sep =",")
# print("ade",20,"osunstate",20000,file= file,sep =",")
# file = open("my_data.csv",  'w')
# details = input("enter your details in this format name,age,state,dues:" )
# splitted_details = details.split (",")
# print( splitted_details[0] , splitted_details[1], splitted_details[2] , splitted_details[3] ,file = file,sep ="," )

# filename = "lyrics.txt.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics)

# filename ="file.csv"
# mode = "w"
# file=open(filename, mode)
# text = "atha,science,eating"
# file.write(text)

# for i in range(5):
#     print (i)
# def max_num(num1, num2, num3) :
#     if num1>= num2 and num1>= num3:
#         return num1
#     elif num2 >= num1 and num2>= num3:
#         re+turn num2
#     else:
#         return num3


# print(max_num(3,54,5))

                            # CALCULATOR
# num1=float(input("type a number:"))
# op = input ("enter operator:")
# num2 = float(input ("enter a second number:"))

# if op == "+":
#     print (num1 +num2)
# elif op=="-" :
#     print (num1-num2)
# elif op== "/":
#     print( num1/num2)
# elif op== "*":
#     print( num1*num2)
# else:
#     print("syntax error")

                            #   DICTIONARIES
                
# monthconversions = {
#         "1": "january",
#         "feb":"febrary",}
# print(monthconversions.get("1","not a valid key")

                #  BUILT IN FUNCTIONS
# my_range=range(20,60,2)
# print(my_range)
# print(type(my_range))
# print(list(my_range))
# print(list(reversed(my_range)))

# x=[1,2,5,3,10,1,0,4]
# print(sorted(x,reverse=True))

# x= list("joseph")
# print(sorted(x))
# my_list=["seed","bee","a","checked","print"]
# print(sorted(my_list,key=len,reverse=True))
# my_dict=dict(a=20,b=30)
# print(my_dict)
# print(my_dict['a'])
# x= set("abimbola")
# print(set(x))

# nums = [1,2,3,4,5,]
# mapped = map(lambda x: x*2, nums)
# print(list(mapped))
# names= ["ade","bola","john"]
# mapped = map(lambda x: "Mr " +x, names)
# print(list(mapped))
                    
                    # COMMON STRING OPERATIONS
# word= [0,0,0,0]
# print (any(word))
# word = "PRINCIPLE".lower()
# print(word)
# word = input("please input a word that starts with 'PRE' :")
# replace_word =word.replace("pre", "post")
# print(replace_word)
# text= ['gem' , 'hem' ,'blem','chem']
# mapped= map (lambda x : x.replace("e","a"), text)
# print(list(mapped))
# my_data = [1,3,1,2,2,4]
# mean = sum(my_data)/len(my_data)
# mapped = list (map(lambda x : (x-mean)**2, my_data))
# print((mapped))
# sum_of_squares =sum (mapped)
# print(sum_of_squares/((len(my_data))-1))
# a =["hello world"]
# print(''.join(a))
# filename = "SNOW.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics.find("Lupita"))
# print(lyrics.count("Brown"))
# filename = "SNOW.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics.find("Lupita"))
# print(lyrics.count("Brown"))
            #  while loop
# i =12
# while i<=10:
#     print(i)
#     i += 1
    
# print("done with loop")

            #    BUILDING A GUESSING GAME
# word= "girraffe"
# guess = ""
# guess_count =0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#        guess = input("enter guess:")
#        guess_count +=1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#            print("you lose")
# else:
#     print("you win")

                        #fore  LOOPING
# friends = ["jim", "karen","kevin"]

# for index in range(len(friends)):
#     print(friends[index])
                                    #    ASSIGNMENT 1
# import random 
# for x in range(2):
#    print(random.randint(1,6))
# if random.randint is (6,6) is True:
#     print("you win")
# else:
#     print("try again")
#                             #   ASSIGNMENT 2
# three_friends = ["bola", "chisom", "james"]
# no_of_friends = (len(three_friends))
# candies = int(input("number of candies:"))
# a =int(candies/no_of_friends)
# remainder = int(candies % 3)
# statement = f' number of candy to be shared is : {a}\n number of candies to be crushed : {remainder}'
# print(statement)
            #   ASSIGNMEN


# health = input('answer with yes or no, are you okay:')
# if health == 'yes':
#      print('get a life')
    
# else: 
#     question_2= str(input('answer with yes or no, do you have pains:'))
#     print(question_2)
     
#     if question_2 == 'no':
#         print('unable to diagnose now') 
#     else:
#         question_3 = input('answer with yes or no, did you sleep well:')
#         print(question_3)

#         if question_3 == 'no':
#            print('try to sleep')

#         else:
#             question_4 = input('answer with yes or no, have you done hard work:')
#             print(question_4)
            
#             if question_4 == 'yes':
#                print('have some pain killer')

#             else:
#                 question_5 =input('answer with yes or no, do you have a fever:')
#                 print(question_5)


#                 if question_5 == "no":
#                    print("inconclusive phase see a doctor")

#                 else:
#                     question_6 =input("answer with yes or no : are you vomitting:")
#                     print(question_6)

#                     if question_6 == "yes":
#                        print("please see doctor")

#                     else:
#                         print("take some antimaleria")

# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)

# for i in range (200):
#     # print(i)
#     mean = sum(range(20))/ len(range(20))
#     # print(mean)
    # print(i,i-mean)

# print("x","|","x-x-bar")
# print('_','|','_____')
# mean = sum(range(5))/ len(range(5))

# for i in range (5):
#     print(i,"|",i-mean)

# print("x".center(4),"|","x-mean".center(9),"|","(x-mean)**2".center(15), sep="")
# print('____'.center(4),'|','_________'.center(9),'|','_______________'.center(15), sep="")
# n=7
# mean = sum(range(n))/ len(range(n))
# for i in range (n):
#     print(f"{i}".center(4),"|",f"{i-mean}".center(9),"|",f"{(i-mean)**2}".center(15), sep="")

# names= ["john", "clam"]
# for i in names:
#     print("hello,",i)

# vowel = ('a','e','i','o','u')
# word= input('write a word:')
# total_vowels = 0
# for letter in (vowel_sounds):
#     if letter in word:
#         print(letter)
#         total_vowels = total_vowels + 1

# print(f"total_vowels : {total_vowels}")


# print(f"vowel    |  count")
# print(f"_________|_________")
# total_vowels = 0
# for vowel in vowel:
#     if vowel in word:

#     # print(vowel)
#        count = word.count(vowel)
#        total_vowel = total_vowels + count
#        print(f"{vowel.center(9)} | {str(count).center(9)}")

# print(f"total_vowels : {total_vowels}")
# for i in word:
#     print(i)
#     if i == "?":



#         break

# filename = "twist.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
filename = "twist.txt"
mode = "r" #read mode open
data = open(filename, mode)
words = data.read()
for index in range(len(words)):
    print(words[4])
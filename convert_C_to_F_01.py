# FILE NAME - convert_C_to_F_01.py

# NAME: Sheri Facey
# DATE: 02/18/2025
# BRIEF DESCRIPTION: Converting Celcius to Fahrenheit 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########



Celsius = float(input('Enter a temperature in Celsius: '))

C_to_F = Celsius * 9/5 + 32
print()
print(f'{Celsius} degrees Celsius is {C_to_F} degrees Fahrenheit.')






########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?
Its not a full number its a number with a decimal point




2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?
   Im not sure but using a float in some cases might give a more accurate value




'''

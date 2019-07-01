"""
Design a program which:
Read a list of integers from user input.
Find all pairs of numbers in the list whose product is even and whose sum is odd.
Print out a formatted list of the pairs.
"""

user_intergers= input("Enter a List of numbers seperated by a space: ")
integer_list=user_intergers.split()


#change all elements to integers
for i in range(len(integer_list)):
    integer_list[i]=int(integer_list[i])


output_list= []
#Find and check all possible combinations
for i in range(len(integer_list)):
    #swap element to front
    integer_list[i], integer_list[0]=integer_list[0],integer_list[i]
    for k in range(1,len(integer_list)):
        product=integer_list[i]*integer_list[k]
        sum= integer_list[i]+integer_list[k]
        if product%2==0:
            if sum%2!=0:
                #Only add to output list if it is a unique pair
                element=[integer_list[i],integer_list[k]]
                reverse_element=[integer_list[k],integer_list[i]]
                if element not in output_list:
                    if reverse_element not in output_list:
                        output_list.append(element)

print("All the pairs in this List of integers are:")
for element in output_list:
    print(f"{element[0]} , {element[1]}")
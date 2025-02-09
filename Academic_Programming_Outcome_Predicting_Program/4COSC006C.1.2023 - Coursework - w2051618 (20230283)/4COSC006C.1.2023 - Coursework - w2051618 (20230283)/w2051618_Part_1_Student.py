# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solu􀆟on.
# Student ID: 20230283
# UoW Student ID: w2051618
# Date: 18/11/2023

def input_data(marks):#Function to input results
    while True:
        try:
            results= int(input(f"Please enter your credits at {marks} : "))#Input results
            if results % 20 == 0 and 0 <= results <= 120:
                   break
            else:
                print("Out of range\n")#Validate the out of range error
        except ValueError:
            print("Integer required\n")#Validate the value error
    return results

print("Hello!!! Welcome to the progression prediction program for Staff!!!")#Display the introduction message
while True:
    Pass = input_data('pass')#Input pass results
    Defer = input_data('defer')#Input defer results
    Fail = input_data('fail')#Input fail results

    if Pass + Defer + Fail == 120:#Checking if total adds up to 120
        if Pass == 120:
            print("Progress\n")#Display the prediction of the student's progress
        elif Pass == 100:
            print("Progress (module trailer)\n")#Display the prediction of the student's progress
        elif Pass < 100 and Fail < 80:
            print( "Do not progress - module retriever\n")#Display the prediction of the student's progress
        elif Fail >= 80:
            print("Excluded\n")#Display the prediction of the student's progress
        print("Ending the program.......")#Display the program ending message
        break
    else:
        print("Total Incorrect")#Display if the total doesn't add up to 120





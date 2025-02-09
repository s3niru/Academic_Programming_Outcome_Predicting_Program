# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solu􀆟on.
# Student ID: 20230283
# UoW Student ID: w2051618
# Date: 18/11/2023
from graphics import *#Importing necessary codes from graphics.py to create the histogram

def creating_histogram(progress_students,retriever_students,trailer_students,exclude_students,total_students):#Function to create the histogram
    win = GraphWin("---Progression Data---", 750, 650)#Display the histogram window name
    win.setBackground("White")#Set the background color of the histogram to white

    X_line = Line(Point(0, 510), Point(750, 510))#Create the X asis line
    X_line.setWidth(2)
    X_line.draw(win)

    Y_line = Line(Point(85, 100), Point(85, 600))#Crete the Y axis line
    Y_line.setWidth(2)
    Y_line.draw(win)

    students_text = Text(Point(40, 300), "Number\n of\n Students")#Display the Y axis representation
    students_text.draw(win)

    Progress = Rectangle(Point(100, 500), Point(220, 500 - 10 * progress_students))#Create the rectangle that represents the number of students who received "Progress"
    Progress.setFill("Green")#Make the color of the rectangle Green
    Progress.setOutline("Black")#Make the color of the outline of the rectangle Black
    Progress.draw(win)
    Progress_text = Text(Point(160, 550), "Progress")#Naming the rectangle "Progress"
    Progress_text.draw(win)
    progress_students_text = Text(Point(160, 490 - 10 * progress_students), str(progress_students))#Display the number of students
    progress_students_text.draw(win)

    Module_retriever = Rectangle(Point(235, 500), Point(355, 500 - 10 * retriever_students))#Create the rectangle that represents the number of students who received "Progress(module retriver)"
    Module_retriever.setFill("Yellow")#Make the color of the rectangle Yellow
    Module_retriever.setOutline("Black")#Make the color of the outline of the rectangle Black
    Module_retriever.draw(win)
    Module_retriever_text = Text(Point(295, 550), "Retriver")#Naming the rectangle "Trailer"
    Module_retriever_text.draw(win)
    retriever_students_text = Text(Point(295, 490 - 10 * retriever_students), str(retriever_students))#Display the number of students
    retriever_students_text.draw(win)

    Trailer = Rectangle(Point(378, 500), Point(498, 500 - 10 * trailer_students))#Create the rectangle that represents the number of students who received "Module retriver"
    Trailer.setFill("Blue")#Make the color of the rectangle Blue
    Trailer.setOutline("Black")#Make the color of the outline of the rectangle Black
    Trailer.draw(win)
    Trailer_text = Text(Point(438, 550), "Trailer")#Naming the rectangle "Retriver"
    Trailer_text.draw(win)
    trailer_students_text = Text(Point(438, 490 - 10 * trailer_students), str(trailer_students))#Display the number of students
    trailer_students_text.draw(win)

    Exclude = Rectangle(Point(515, 500), Point(635, 500 - 10 * exclude_students))#Create the rectangle that represents the number of students who received "Excliuded"
    Exclude.setFill("Red")#Make the color of the rectangle Red
    Exclude.setOutline("Black")#Make the color of the outline of the rectangle Black
    Exclude.draw(win)
    Exclude_text = Text(Point(575, 550), "Exclude")#Naming the rectangle "Exclude"
    Exclude_text.draw(win)
    exclude_students_text = Text(Point(575, 490 - 10 * exclude_students), str(exclude_students))#Display the number of students
    exclude_students_text.draw(win)
    
    Total = Text(Point(350,600),f'{total_students} outcomes in total')#Display the number of outcomes
    Total.draw(win)


def printing_list(list):#Finction to display each element in every list
    for x in list:
        print(x)#Display element

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


print("Hello!!! Welcome to the progression prediction program for Staff!!!\n")#Display the introduction message

choice = 'y'
progress = 0
retriever = 0
trailer = 0
exclude = 0
total = 0

progress_list = []
retriever_list = []
trailer_list = []
exclude_list = []

while choice == 'y':
    Pass = input_data('pass')#Input pass results
    Defer = input_data('defer')#Input defer results
    Fail = input_data('fail')#Input fail results


    if Pass + Defer + Fail == 120:#Checking if total adds up to 120
        if Pass == 120:
            progress += 1
            print("Progress\n")#Display the prediction of the student's progress
            progress_list.append(f'Progress -{Pass},{Defer},{Fail}')#Add the results to progress_list
        elif Pass == 100:
            trailer += 1
            print("Progress (module trailer)\n")#Display the prediction of the student's progress
            trailer_list.append(f'Progress (module trailer) -{Pass},{Defer},{Fail}')#Add the results to trailer_list
        elif Pass < 100 and Fail < 80:
            retriever += 1
            print("Do not progress - module retriever\n")#Display the prediction of the student's progress
            retriever_list.append(f'Module retriever -{Pass},{Defer},{Fail}')#Add the results to retriever_list
        elif Fail >= 80:
            exclude += 1
            print("Excluded\n")#Display the prediction of the student's progress
            exclude_list.append(f'Exclude -{Pass},{Defer},{Fail}')#Add the results to exclude_list
        total += 1
    else:
        print("Total Incorrect\n")#Display if the total doesn't add up to 120
    while True:
        print("\nWould you like to enter a another set of data ?")#Check if the user wants to continue
        choice = input("Enter y for yes or q to quit and view results : ")#Input 'y' or  'q'
        if choice == 'y':
            break#if the user enters 'y' th program continues
        elif choice == 'q':#if the user enters 'q' program ends

            print("\n---Progression Data---")#Display the end results
            print("Progress - ",progress)
            print("Retriever - ",retriever)
            print("Trailer - ",trailer)
            print("Excluded - ",exclude,"\n")
            creating_histogram(progress, retriever, trailer, exclude, total)#Display the histogram which represents the end results
            printing_list(progress_list)#Display progress_list
            printing_list(trailer_list)#Display trailer_list
            printing_list(retriever_list)#Display retriever_list
            printing_list(exclude_list)#Display exclude_list

            print("\nEnding the program.......")#Display the program ending message
           
            break
        else :
            print("Please enter y or q ")#Validating the error if user enters input something other than 'y' or 'q'










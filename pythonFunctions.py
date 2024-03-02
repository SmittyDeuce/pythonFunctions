# 1. The Welcoming Program
# Objective:
# The aim of this assignment is to create a simple program that greets users and responds based on their input.

# Task 1: Code a program that asks for the user's name and prints a personalized greeting.
def greeting():
    name = input("What is your name? ")
    print(f"Pleased to meet you {name}!!!")

# greeting()
    
# Task 2: Modify the program to ask the user how they are feeling today and respond with a comforting message if they're feeling down, or a cheerful one if they're happy.
def greeting():
    name = input("What is your name? ")
    print(f"Pleased to meet you {name}!!!")
    mood = input("How are you feeling today?: (Down/Cheerful): ")
    if mood.lower() == "down":
        print(f"Cheerup {name} it'll all get better :P")
    if mood.lower() == "cheerful":
        print(f"That's what we love to hear!!!")
# greeting()
        
# Task 3: Add error handling to ensure that the user inputs a string for their name and not a number or special character.
def greeting():
    name = input("What is your name? ")
    if name.isalpha():
        print(f"Pleased to meet you {name}")
        mood = input("How are you feeling today?: (Down/Cheerful): ")
        if mood.lower() == "down":
            print(f"Cheerup {name} it'll all get better :P")
        if mood.lower() == "cheerful":
            print(f"That's what we love to hear!!!")
    else:
        print("INVALID RESPONSE")
# greeting()


# 2. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
def addition(num1, num2):
    print(num1 + num2)

# addition(3,4)

def subtraction(num1, num2):
    print(num1 - num2)

# subtraction(23, 14)

def multiplication(num1, num2):
    print(num1 * num2)
# multiplication(9,3)

def division(num1, num2):
    print(num1 / num2)

# division(10, 5)

# Task 2: Implement user input to receive numbers and an operation choice.
def operationChoice():
    operation = input("choose an arithmetic operation (add, subtract, times, divide: respond with (1,2,3,4) ")
    if operation == '1':
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        addition(num1, num2)
    elif operation == '2':
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        subtraction(num1, num2)
    elif operation == '3':
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        multiplication(num1, num2)
    elif operation == '4':
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        division(num1, num2)
    else:
        print("Invalid Response")
# operationChoice()

# Task 3: Ensure your program can handle division by zero and other potential errors.
def operationChoice():
    operation = input("choose an arithmetic operation (add, subtract, times, divide: respond with (1,2,3,4) ")
    if operation.isalpha():
        print("Respoond with 1,2,3,4")
    elif int(operation) == 1:
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        addition(num1, num2)
    elif int(operation) == 2:
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        subtraction(num1, num2)
    elif int(operation) == 3:
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        multiplication(num1, num2)
    elif int(operation) == 4:
        num1 = int(input("enter a number "))
        num2 = int(input("enter second number "))
        if num2 == 0:
            print("CAN'T DIVIDE BY ZERO")
        else:
            division(num1, num2)
    else:
        print("Invalid Response")
# operationChoice()


# 3. The Temperature Converter
# Objective:
# The aim of this assignment is to write a program that converts temperatures between Fahrenheit and Celsius.
# Task 1: Code a function that converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(temperature):
    resInFahrenheit = (temperature * 9/5) + 32
    print(resInFahrenheit)
# celsius_to_fahrenheit(3)

# Task 2: Code a function that converts Fahrenheit to Celsius.
def fahrenheit_to_celsius(temperature):
    resInCelsius = (temperature - 32) * 5/9
    print(resInCelsius)
# fahrenheit_to_celsius(3)

# Task 3: Implement a user interface that asks the user which conversion they want to perform and calls the appropriate function.
def tempConversion():
    celsiusOrFahrenheit = input("press 'C' to convert Celsius to Fahrenheit 'F' to convert Fahrenheit to Celsius ")
    if celsiusOrFahrenheit.lower() == "c":
        temperature = int(input("Enter a temp "))
        celsius_to_fahrenheit(temperature)
    elif celsiusOrFahrenheit.lower == "f":
        temperature = int(input("Enter a temp "))
        fahrenheit_to_celsius(temperature)
    else:
        print("Invalid Response")
# tempConversion()
        
# 4. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
def listMaker():
    shoppingList =[]
    while True:
        addItem = input("What would you like to add? (enter 'done' to finish) ")
        if addItem.lower() == "done":
            break
        else:
            shoppingList.append(addItem)
            print(shoppingList)
# listMaker()




# Task 2: Include a feature to remove items from the list.
def listMaker():
    shoppingList =[]
    while True:
        addItem = input("What would you like to add? (enter 'done' to finish) ")
        if addItem.lower() == "done":
            break
        else:
            shoppingList.append(addItem)
            print(shoppingList)
    
    while True:
        completed = input("What have you managed to acquire? (enter 'done when finished) ")
        if completed.lower() == "done":
            print("here is your List:", shoppingList)
            break
        else:
            shoppingList.remove(completed)
            print("Here is your updated list:",shoppingList)
# listMaker()


# Task 3: Add a function that prints out the entire list in a formatted way.
def listMaker():
    shoppingList =[]
    while True:
        addItem = input("What would you like to add? (enter 'done' to finish) ")
        if addItem.lower() == "done":
            break
        else:
            shoppingList.append(addItem)
            print(shoppingList)
    
    while True:
        completed = input("What have you managed to acquire? (enter 'done when finished) ")
        if completed.lower() == "done":
            print("here is your List:", shoppingList)
            break
        else:
            shoppingList.remove(completed)
            print("Here is your updated list:",shoppingList)

    for items in shoppingList:
        print(f" you still need to buy {items}")
# listMaker()


# 5. The Grade Analyzer
# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
grades = [90, 85, 70, 95, 60, 75, 80, 92, 88, 85, 45, 30, 55, 65, 72]
def avgGrades(gradelist):
    count = 0
    for idx in range(len(gradelist)):
      count += gradelist[idx]
    print(count / len(gradelist))

# avgGrades(grades)


# Task 2: Implement a function to find the highest and lowest grade.
def high_low_grade(gradelist):
    highNum = 0
    lowNum = float("inf")
    for idx in range(len(gradelist)):
        if gradelist[idx] > highNum:
            highNum = gradelist[idx]

        if gradelist[idx] < lowNum:
            lowNum = gradelist[idx]
    print(f'Your highest grade is {highNum} and lowest is {lowNum}')
# high_low_grade(grades)

# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
def letterGrades(gradelist):
    gradesObj = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for grade in gradelist:
        if grade >= 90:
            gradesObj["A"].append(grade)
        elif grade >= 80:
            gradesObj["B"].append(grade)
        elif grade >= 70:
            gradesObj["C"].append(grade)
        elif grade >= 60:
            gradesObj["D"].append(grade)
        else:
            gradesObj["F"].append(grade)
    print(gradesObj)
# letterGrades(grades)


# 6. The Daily Planner
# Objective:
# The aim of this assignment is to create a simple daily planner that can add, remove, and display tasks.

# Task 1: Write a function to add a task with a time slot.
from datetime import datetime
def taskTimeSlot():
    taskObj ={}
    while True:
        taskName = input("What is the Task: (enter 'done' when finished) ")
        if taskName.lower() == 'done':
            print(f"Todays timeframe and tasks: {taskObj}")
            break
        else:
            taskTime = input("What time do you need to start this task: (1-24) ")
            taskTime = int(taskTime)
            if taskTime > 24 or taskTime < 1:
                print("respond with num: 1-24 ")
                continue
            if taskTime not in taskObj:
                taskObj[taskTime] = []
            taskObj[taskTime].append(taskName)
            print(taskObj)


taskTimeSlot()
# Task 2: Code a function to remove a task.
# Task 3: Implement a display function that shows all tasks in order of time.

# 7. The Quiz Game
# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.

# 8. The Journey Planner
# Objective:
# The aim of this assignment is to create a program that plans a journey, calculating travel times and stops.

# Task 1: Code a function that calculates travel time based on distance and speed.
# Task 2: Create a feature that suggests stops based on the length of the journey.
# Task 3: Implement user input for starting point, destination, and preferred travel speed.

# 9. The Personal Library Organizer
# Objective:
# The aim of this assignment is to create a system that organizes a personal library of books.

# Task 1: Write a function to add books with title, author, and genre.
# Task 2: Code a search function to find books by title or author.
# Task 3: Implement a way to display books sorted by genre or author.

# 10. The Fitness Tracker
# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Develop a function to log different fitness activities and their duration.
# Task 2: Write a function that estimates calories burned based on the activity and duration.
# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

# Each of these assignments is designed to challenge the learner to apply the concepts discussed, such as user input, type conversion, string formatting, and function creation, while also ensuring they practice error handling and user-friendly output formatting.
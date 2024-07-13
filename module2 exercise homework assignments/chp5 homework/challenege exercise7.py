## Author: Francisco Bumanglag
## Project: Stadium Seating 
## Assignment: Module 2 Project 5
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


#definition of calculations function
def calculations(num_a_tickets, num_b_tickets, num_c_tickets):
    class_a_tickets = 20.00
    class_b_tickets = 15.00
    class_c_tickets = 10.00

    #perform calculations on A, B, and C ticket prices and store in income variable
    income = (num_a_tickets * class_a_tickets) + (num_b_tickets * class_b_tickets) + (num_c_tickets * class_c_tickets)
    #return the income variable back to the main function
    return income

#definition of main function -- user input
def main():
    a_tickets = int(input("How many A Class Tickets were sold: "))  # class A
    b_tickets = int(input("How many B Class Tickets were sold: "))  # class B
    c_tickets = int(input("How many C Class Tickets were sold: "))  # class C

    #declare income variable and pass it to the calculations function
    #along with arguments for A, B, and C tickets
    income = calculations(a_tickets, b_tickets, c_tickets)

    print("The total income generated from ticket sales is: $", income)

#call the main function to start the program
main()

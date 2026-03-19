# Name: Caleb Schneringer
# Date: 3/14/2026
# Program: Math Application
# Description: Creates problems for the user to solve, then provides the anser to the same problem.

# Imports
import random

# Global Variables

CHOICE_EASY = 1
CHOICE_NORMAL = 2
CHOICE_HARD = 3

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
# Functions
def Problem_Formater(list, problem_type):
    # This Function is used to create the string format of the problem to print
    # This Function returns as a string 
    Num_list = list
    if problem_type == ADDITION:
        return f"{Num_list[0]} + {Num_list[1]}?"
    elif problem_type == SUBTRACTION:
        return f"{Num_list[0]} - {Num_list[1]}?"
    elif problem_type == MULTIPLICATION:
        return f"{Num_list[0]} * {Num_list[1]}?"
    elif problem_type == DIVISION:
        return f"{Num_list[0]} / {Num_list[1]}?"
    else:
        print("problem in Problem_Formater")

def Problem_Answer(list, problem_type):
    Num_list = list
    if problem_type == ADDITION:
        return Num_list[0] + Num_list[1]
    elif problem_type == SUBTRACTION:
        return Num_list[0] - Num_list[1]
    elif problem_type == MULTIPLICATION:
        return Num_list[0] * Num_list[1]
    elif problem_type == DIVISION:
        return Num_list[0] / Num_list[1]
    else:
        print("problem in Problem_Answer")

def Problem_Type_Chooser(difficulty):
    # Local Variables
    Minimum = 1
    Maximum = 4

    # Makes difficulty represent it's level in numbers
    if difficulty == "easy":
        difficulty = CHOICE_EASY
    elif difficulty == "normal":
        difficulty = CHOICE_NORMAL
    elif difficulty == "hard":
        difficulty = CHOICE_HARD
    else:
        print("Problem in constant conversion in Problem_Type_Chooser")

    # Once converted, depending on chosen difficulty option for problems are chosen
    # For example, if easy, randint can only chose between 1 and 2 which equates to 1 = additon
    # and 2 = subtraction, as the Global Variables state.

    if difficulty == 1:
        Maximum = 2
    elif difficulty == 2:
        Maximum = 3
    elif difficulty == 3:
        Maximum = 4
    else:
        print("Problem in Max problem type in Problem_Type_Chooser")

    return random.randint(Minimum, Maximum)

def Generate_Numbers(problem_type):
    # I created the variables that will store our numbers then put them in a list so that they can
    # be transfered between functions easily and in a pair.
    n1 = 0
    n2 = 0
    list = [n1, n2]

    # The code below Generates the numbers for each Problem.
    # Depending on what type of problem we are useing, the number generator is varied
    # to keep out negative and decimal number for answers then returns them as a list.
    if problem_type == ADDITION:
        n1 = random.randint(10, 60)
        n2 = random.randint(10, 60)
        list = [n1, n2]
        return list

    elif problem_type == SUBTRACTION:
        while True:
            n1 = random.randint(10, 60)
            n2 = random.randint(10, 50)
            if n1 > n2:
                list = [n1, n2]
                return list

    elif problem_type == MULTIPLICATION:
        n1 = random.randint(1, 12)
        n2 = random.randint(1, 12)
        list = [n1, n2]
        return list
    elif problem_type == DIVISION:
        while True:
            n1 = random.randrange(1, 100, 2)
            n2 = random.randrange(1, 10, 2)
            if n1 > n2:
                if n1 % n2 == 0:
                    list = [n1, n2]
                    return list

    else:
        print("Problem with generating numbers")

def Find_Results(answer, guess):
    # Checks to see if the the user guess equals the answer found by the program.
    # It returns a string statement.
    statement = ""
    if answer == guess:
        return f"You are correct! The answer is {answer}"
    elif answer != guess:
        return f"You are Incorrect! The answer is {answer}"

def Main():
    Play_Flag = "y"
    # While loop for repeating the game
    while Play_Flag.lower() == "y":
        print("Welcome to the math game!")
        

        # Ask's user for their difficulty
        # EASY = 'addition' and 'subtraction'
        # NORMAL = 'addition' and 'subtraction' and 'multiplication'
        # HARD = 'addition' and 'subtraction' and 'multiplication' and 'division'
        print(" Please answer in (easy, medium, or hard)")

        # Checks to make sure that difficulty is valid.
        while True:
            Difficulty = input("Choose a difficulty! (EASY: Addition and Subtraction), (NORMAL: Previous + Multiplicaiton), (HARD: Previous + Division.)\n")
            if Difficulty.lower() in ("easy", "medium", "hard"):
                break
        

        playing = True

        while playing:
            # This finds what type of problem we are dealing with (addition, subtraction ect.) and is set to a intiger. 
            problem_type = Problem_Type_Chooser(Difficulty.lower())
            # Using the type of problem we are creating, we generate the numbers used in the problem.
            Numbers_List = Generate_Numbers(problem_type)
            # Prints out the format of the question so the user can solve it.
            # I could put it in the input, but i didnt feel like it.
            print(Problem_Formater(Numbers_List, problem_type))
            # Ask's user for their answer
            User_Guess = int(input("Your Answer: "))
            # The computer finds the answer
            Answer = Problem_Answer(Numbers_List, problem_type)
            # the computer and user compare answers, and depending on that, a print statement is used.
            print(Find_Results(Answer, User_Guess))
            # Asks the user if they would like to play agian then uses an if statement to exit if not.
            Play_Again = input("Would you like to play again? (y/n): ")
            if Play_Again.lower() == "n":
                break
            # prints for added line
            print()
        # If a user ends up here they had to have said no to the play again.
        # Due to that we set the Play_Flag to n.
        Play_Flag = "n"

if __name__ == "__main__":       
    Main()

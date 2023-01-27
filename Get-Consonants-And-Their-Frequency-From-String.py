#   COMSATS University Islamabad Lahore Campus
#   FA22-BSE-(A) = Theory Exam

#   Use pseudo code/flowchart/python code to write algorithm for the following problem. Keep in mind that marking criteria will be based on your solution design in term of understandability and modularity i-e using proper functions for tasks, manageable variables etc.

#   A function in a program that keeps taking text input from user and return the number if consonants in the text. It also prints the number of times each consonants appear in the text inputs until user enters"stop"

'''

    Example Output

    Word: Terminal
    Output:        5[1 1 1 1 1]
    Word: Exam
    Output:        2[1 1]
    Word: Possession
    Output:        5[1 3 1]

'''

#   Solution:

def NumberOfConsonants():

    PrimeText = ""        # String Of Non Repeat Consonants
    ConsSTR = ""          # String of All Consonants
    consonants = 0        # Number Of Consonants
    Frequency = 0         # Count consonants in ConsSTR

    for i in text:

        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':

            consonants += 1
            ConsSTR += i

            if i not in PrimeText:          # Checking Non Repeat consonants
                PrimeText = PrimeText+i     # if not occurs before add it in PrimeText String

    if consonants == 0:
        print("Non consonants in text")     # All Words Are Vowels
        return

    # print(PrimeText)
    # print(ConsSTR)

    print(f" Output:\t   {consonants}[", end='')

    # Calculate Frequency Of Consonants

    for z in PrimeText:            # Loop For PrimeText Characters
        for y in ConsSTR:          # Loop For ConsSTR Characters
            if z == y:             # Checking is PrimeText Found in ConsSTR
                Frequency += 1

        if Frequency != 0:
            print(Frequency, end=' ')

        Frequency = 0              # Set to Zero(0) for next occurrence

    print("\b]")

# Main Function

global text                        # Defining Global Variable
text="Umair Ali - FA22-BSE-137"

while (text != "stop"):

    text = input(" Word:  ")
    text = text.lower()

    flag=text.isalpha()

    if flag==True:
        NumberOfConsonants()
    else:
        print(" Enter only Alphabets")


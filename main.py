""" Created by: Leo Martinez III in Spring 2022 """

def project2(S):
    if len(S) < 2: # Base case
        return True
    else:
        if S[0] == S[-1]: # Program checks if the first and last letter of the word match
            return project2(S[1:len(S) - 1]) # If so, the program will recall itself and continue on (recursion)
        else:
            return False
userInput=str(input("Enter string: ")) # User input (string)
if(project2(userInput)==True): # Program checks the user input
    print("True, the word is a palindrome.")
else:
    print("False, the word is NOT a palindrome.")

""" Runtime of the program: O(n), the function is linear. """

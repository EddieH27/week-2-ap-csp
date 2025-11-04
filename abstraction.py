# abstraction is when i hide
# the complex details for something
# a lot more simple
# personal information
#a function allows us to wrap data or
#information into a special box or enclosure for resuse

# def personalInformation():
#     question1 = input("how old are you?")
#     question2 = input("where do you live?")
#     question3 = input("what school do you go to?")
#     print(question1 + question2 + question3)

# personalInformation()
# personalInformation()
# personalInformation()

def guessAge():
    q1 = int(input("what year were you born?"))
    q2 = int(input("what year is it now?"))
    answer = q2 - q1
    result = print(f'you are {answer} years old.')
guessAge()
guessAge()
guessAge()

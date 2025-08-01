# input output in python 

# n = input('Enter a number: ')
# print(n)

# Data types - gfg

def dataSize(str):
    if (str == 'Character'):
        return 1
    if (str == 'Integer'):
        return 4
    if (str == 'Long'):
        return 8
    if (str == 'Float'):
        return 4
    if (str == 'Double'):
        return 8

# ans = dataSize('Character')
# print(ans)

# If ElseIF

# Given marks of a student, print on the screen:

# Grade A if marks >= 90
# Grade B if marks >= 70
# Grade C if marks >= 50
# Grade D if marks >= 35
# Fail, otherwise.

def studentGrade(marks):
    if (type(marks) != int):
        print('Please enter a valid number')
        return
    if (marks >= 90): print('Grade A')
    elif (marks >= 70): print('Grade B')
    elif (marks >= 50): print('Grade C')
    elif (marks >= 35): print('Grade D')
    else:
        print('Fail')


# studentGrade(91)
# studentGrade(84)
# studentGrade(55)
# studentGrade(15)

# Switch Case

# Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
# Ensure only the 1st letter of the answer is capitalised.

def dayToWeek(day):
    match day:
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Satday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid day')

# dayToWeek(3)
# dayToWeek(1)
# dayToWeek(8)





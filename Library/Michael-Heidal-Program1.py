# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Mike Heidal
# Last Modified: 25 September 2018 
# ---------------------------------------
# A GPA calculator.
# ---------------------------------------

def translate(grade):
    if (grade == "A") or (grade == "a"):
        return 4.0
    elif (grade == "A-") or (grade == "a-"):
        return 3.7
    elif (grade == "B+") or (grade == "b+"):
        return 3.3
    elif (grade == "B") or (grade == "b"):
        return 3.0
    elif (grade == "B-") or (grade == "b-"):
        return 2.7
    elif (grade == "C+") or (grade == "c+"):
        return 2.3
    elif (grade == "C") or (grade == "c"):
        return 2.0
    elif (grade == "C-") or (grade == "c-"):
        return 1.7
    elif (grade == "D+") or (grade == "d+"):
        return 1.3
    elif (grade == "D") or (grade == "d"):
        return 1.0
    elif (grade == "F") or (grade == "f"):
        return 0.0


def main():
    gradecreds = 0
    nCreds = 0

    nClasses = int(input("Enter number of courses taken: "))
    
    for i in range(nClasses):
        grade = translate(input("Enter grade for course " + str(i + 1) + ": "))
        cred = int(input("Enter credits for course " + str(i+1) + ": "))
        gradecreds += + (grade * cred)
        nCreds = nCreds + cred

    gpa = gradecreds / nCreds

    print("Your GPA is", round(gpa, 2))

main()

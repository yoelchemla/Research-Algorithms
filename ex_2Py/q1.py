import re
import txt as txt

# for the match email, i used by this website-
# https://www.tutorialspoint.com/python-program-to-validate-email-address

reg = r'([A-Za-z0-9]+[--_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

"""
this function take an address email and check if the email is legal
if not match -> return false
else -> return true
"""


def check_legal(s):
    if not re.match(reg, s):
        return False
    return True


"""
this function open the file, and create a list that split by a new line.
check if the condition (legal email) exist
if yes -> add to the valid list
if no -> add to the invalid list
and print the lists.

"""

def check_from_the_file(file_text):
    valid = []
    invalid = []

    # file open used by the website -
    # https://www.w3schools.com/python/python_file_open.asp

    f = open(file_text, "r")
    lst = list(f.read().split("\n"))
    for i in lst:
          if check_legal(i):
             valid.append(i)
          else:
             invalid.append(i)

    print("list of emails valid: ")
    print(valid)
    print()
    print("list of emails invalid: ")
    print(invalid)

if __name__ == '__main__':
    # print(check_legal("abc..def@mail.com"))

    # the emails address used by -
    # https://help.xmatters.com/ondemand/trial/valid_email_format.htm

    check_from_the_file("txt")

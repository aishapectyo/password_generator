import string
import random


def random_password_generator(length=10, chars=string.ascii_letters + string.digits + '!@#$%^&*()'):
    """
    Returns a string of random characters. It may contain upper 
    and lowercase letters, and numbers.
    The default size is a password of size 10.
    Please note that the characters are made up of A-Z, a-z and 0-9.
    The function takes in the length and character types as arguments.
    """
    password = ''.join(random.choice(chars) for _ in range(length))
    return password



#Random library

my_list = ["nib", "pen", "brush", "sumi", "ink", "paper"]
random.choice(my_list)
random.randint(0, 10)
for i in range(3):
    print random.randrange(0, 30, 1)

random.random()
random.uniform(1, 10) #1.0+


#String library
my_string = "dank meme"
string.upper(my_string)
string.split(my_string)
string.join(string.split(my_string), "+")
string.replace(my_string, "dank", "savage")
string.join(my_string, "dankiest")

#Test function
]my_password = random_password_generator(length=8)



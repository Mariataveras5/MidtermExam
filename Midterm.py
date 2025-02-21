from itertools import count

#Question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

#Question 2
print((3+10**2/2) or 70.0)

#Question 3
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#Question 4 *
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

#Question 5
def pattern_matches(text):
    """
    function that finds all words that start with "C" and end with "jeb"
    :param text: text to look into
    :return: number of matches
    """
    count = 0
    words = text.split()  # Split text into words

    for word in words:
        if word.startswith("C") and word.endswith("jeb"):
            count += 1
    return count

text = "In the distant land of Carmojeb, there lived a wise old sage named Caldrijeb.He spent his days studying the ancient texts of Crispjeb, a legendary book said to contain the secrets of the universe. One day, a traveler from Celorijeb arrived, seeking knowledge about the lost city of Cyndrijeb. Caldrijeb, stroking his beard, said, Only those with a pure heart can uncover the truth hidden within Celestijeb.As they spoke, the mischievous trickster Zalborjeb appeared, laughing wildly. You seek the city? You’ll have to cross the dangerous Mordijeb river first! The traveler hesitated, remembering the tales of the monstrous Grallijeb lurking in the waters. But his determination was strong. Then I shall go, for destiny awaits in Crespojeb!"
print(pattern_matches(text))

#Question 6
#Mutable objects can be changed after being created:
list = [1, 2, 3, 4, 5, 6]
print("Original list:", list)
list[0] = 4    # first element in the list is modified
print("Modified:", list)

#Immutable objects cannot be changed after creation:
string = "this is my programming exam"
print(string)
new_string = string.replace("t", "T")
print(new_string) # string remains the same, changes to string are only stored in new_string

#Attempting to modify the string will give you an error:

#Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

changed_numbers = []
for number in random_numbers:

print(changed_numbers)


#Question 8

def valid_url(url):
    valid = False

    # Check if URL starts with "http://" or "https://"
    if url.startswith("http://"):
        # Check if there is at least one dot
        if "." in url:
            # Check if there are no spaces
            if " " not in url:
                # Split by dot and check if the last part is not empty
                parts = url.split(".")
                if len(parts[-1]) > 0:
                    valid = True  # If all conditions are met, the URL is valid

    return valid
print(valid_url("https://docs.python.org/3/library/stdtypes.html"))
print(valid_url("http://docs.python.org/3/library/stdtypes.html"))
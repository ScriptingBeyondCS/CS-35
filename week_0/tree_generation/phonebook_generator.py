import csv
import random
def create_phonebook(n):
    """ creates n text files in the current directory,
        each containing a first name, last name,
        and a phone number.
    """
    numbers = phone_number_generator(n) #a list of phone numbers
    first_names = csv_to_list('firstNames.csv') #list of possible first names
    last_names = csv_to_list('lastNames.csv') #list of possible last names
    for i in range(n): #loop to create n entries in the phonebook
        f = open(str(i)+".txt", 'w+') #create a text file we can write to
        name1 = random.choice(first_names) #pick a first name
        name2 = random.choice(last_names) #pick a last name
        order = random.choice([0,1]) #decide if order is "first last" or "last, first"
        if order: 
            f.write(numbers[i] + '\n' + name1 + ' ' + name2) #write to file we created earlier
        else: f.write(numbers[i] + '\n' + name2 + ', ' + name1) #same as above

def csv_to_list(filename):
    """ creates a list of the contents of the csv
    """
    out = []
    with open(filename, newline = '') as f: #open csv file containing names
        reader = csv.reader(f) #read the file
        for row in reader: #loop over rows of the file  
            out += row #add contents of row (a name) to the final list
    return out #return list

def phone_number_generator(n):
    """ Takes as input an int n, and randomly generates 
        a list of n phone numbers of various styles 
    """
    output = []
    for i in range(n):
        number = generator(random.choice(range(10))) #randomly picks a style of number
        output += [number]
    return output

#helper function for phone_number_generator
def generator(style):
    """ outputs a number consistent with style
        specified by the input
    """
    num = autogenerator() #calls autogenerator to create ten digit string
    if style == 0:
        return num #1234567890
    elif style == 1:
        return '(' + num[:3] + ')' + num[3:] #(123)4567890
    elif style == 2:
        return '(' + num[:3] + ')' + num[3:6] + '-' + num[6:] #(123)456-7890
    elif style == 3:
        return num[:3] + '.' + num[3:6] + '.' + num[6:] #123.456.7890
    elif style == 4:
        return '442-' + num[3:6] + '-' + num[6:] #442-456-7890
    elif style == 5:
        return '402 ' + num[3:] #402 4567890
    elif style == 6:
        return '(909) ' + num[3:6] + '-' + num[6:] #(909) 456-7890
    elif style == 7:
        return '442 ' + num[3:6] + ' ' + num[6:] #442 456 7890
    elif style == 8:
        return '(760)' + num[3:] #(760)4567890
    else:
        return num[3:] #4567890

#helper function for generator
def autogenerator():
    """ creates ten digit string of numbers
        that could be a phone number
    """
    number = '0'
    while number[0] not in '23456789': #check if valid phone number (area codes don't start with 1 or 0)
        number = ''
        for i in range(10):
            digit = random.choice(range(10)) #pick a random number
            number += str(digit) 
    return number 

create_phonebook(4)
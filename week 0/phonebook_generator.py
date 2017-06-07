from phone_number_generator import phone_number_gen
import csv
import random
def create_phonebook(n):
    """ creates n text files in the current directory,
        each containing a first name, last name,
        and a phone number.
    """
    numbers = phone_number_gen(n) #a list of phone numbers
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
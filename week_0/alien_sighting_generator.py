import os
import os.path
import random
import itertools

def generate_alien_sighting_files(num_files):
    for i in range(num_files):
        f = open("alien_sighting"+str(i+1), "w+")
        f.write("Alien sighting diary entry number " + str(i+1))
        f.write("I saw an alien with three eyes...")

def main():
    generate_alien_sighting_files(5)
if __name__ == '__main__':
    main()

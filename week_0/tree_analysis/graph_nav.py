import os
import os.path

def theseus():
    """
    theseus checks if a directory has been visited by
    our graph navigator function yet.  If the directory
    has not been visited, theseus will write out a .txt
    file ('string.txt') to indicate that the directory
    has indeed been visited, and then return True,
    meaning the graph_nav function should return to the
    parent directory.  Else, theseus returns False,
    indicating that the directory has not been visited
    yet.
    """
    if os.path.exists('./string.txt'):
        return True
    else:
        return False

def graph_nav():
    """
    graph_nav() runs through a directory graph, and
    collects information along the way.  In this case,
    it determines the total number of directories
    contained in the structure.
    """
    global num_visited # so that we don't have to pass this each call
    if theseus():      # if we've visited this directory already
        os.chdir('..') # leave it
        return
    else:              # if we haven't....
        num_visited += 1 # add 1 to the num of dirs we've visited
        write_this = open('string.txt', 'w') # mark that we've visited
        write_this.write('been here done that') # ibid
        write_this.close()
        curr_path = os.getcwd() # so that we can find stuff despite symlinks
        for dir in os.listdir('.'): # get all the things in our current dir
            if os.path.isdir(dir):  # if the thing is a dir
                os.chdir(dir)       # go to it
                graph_nav()         # and recurse
            # this elif is because of the weird way symlinks work.
            # need to give an absolute path (hence the join and curr_path)
            elif os.path.isdir(os.path.join(curr_path,dir)):
                os.chdir(os.path.join(curr_path,dir))
                graph_nav()
            else:
                pass
        os.chdir('..') # move back out
        return

def main():
    """
    main takes no arguments.  Essentailly just initializes the graph
    navigator, and the global tallies for num directories visited.
    """
    global first_dir # so that we can return to where we started
    first_dir = os.getcwd()
    global num_visited # so that we don't need to pass this each call
    num_visited = 0
    graph_nav()
    num_visited -= 1 # off by 1 error (accidentally goes up 1 to far at end)
    os.chdir(first_dir)
    return num_visited # return total result

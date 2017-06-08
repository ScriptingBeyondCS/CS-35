import os
import os.path

num_visited = 0

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
    global num_visited
    # if 'string.txt' in [file for file in os.listdir('.') if os.path.isfile(f))]:
    if os.path.exists('./string.txt'):
        return True
    else:
        return False

def graph_nav():
    """
    graph_nav() runs through a directory graph, and
    returns associated values.
    """
    global num_visited
    os.system('tree -a')
    if theseus():
        os.chdir('..')
        return
    else:
        num_visited += 1
        write_this = open('string.txt', 'w')
        write_this.write('been here done that')
        write_this.close()
        curr_path = os.getcwd()
        for dir in os.listdir('.'):
            if os.path.isdir(dir):
                os.chdir(dir)
                graph_nav()
            elif os.path.isdir(os.path.join(curr_path,dir)):
                os.chdir(os.path.join(curr_path,dir))
                graph_nav()
            else:
                pass
        os.chdir('..')
        return

def main():
    global first_dir
    first_dir = os.getcwd()
    global num_visited
    num_visited = 0
    graph_nav()
    os.chdir(first_dir)
    return num_visited

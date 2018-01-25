class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    RED = '\033[91m'
    YELLOW = '\033[35m'
print bcolors.HEADER + "This is a test" 
print bcolors.ENDC + "Another test"
print bcolors.RED + "One " + bcolors.YELLOW + "more"

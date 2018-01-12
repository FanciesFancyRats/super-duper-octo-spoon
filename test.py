CSI="\x1b["
print CSI+"31;40M" + "Colored Text" + CSI + "0m"
from termcolor import colored

print colored('hello', 'red'), colored('world', 'green')

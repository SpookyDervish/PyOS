import os

from kernel.kernel import kmain


# * This line makes sure we boot from the current directory :)
os.chdir(os.path.dirname(__file__))
# Boot into the system
kmain()
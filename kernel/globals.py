"""
########################################
# KERNEL GLOBALS
########################################

Global variables used in the kernel. This file contains the declarations;
storage space for the variables is allocated in table.c, because EXTERN is
defined as extern unless the _TABLE definition is seen. We rely on the 
compiler's default initialization (0) for several global variables.
"""


from rich.console import Console


class Global():
    console = Console()
# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> [--arg_opt=<arg_opt>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg1>            Takes any value (this is a required positional argument)
[<arg_opt>]       Takes any value (this is an optiotnal positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main():
    print(opt)
    print(type(opt))

if __name__ == "__main__":
    main()

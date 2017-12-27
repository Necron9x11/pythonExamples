This is every ittreration of the examples from the Python argparse library tutorial at https://docs.python.org/3.5/howto/argparse.html#id1

The files are commented and the comments are more or less sequential in nature, beginning from the first changes and moving on through the last from file to file. Mostly. :/

The tutorial covers:
 - Importing the argument parser library: i.e. : "import argparser"
 - Creating an argument parser argument with "parser = argparse.ArgumentParser"
 - Short and long options: i.e. "-v" versus "--verbose"
 - Adding arguments with the .add_argument() method: i.e.: parser.add_argument(["argument"])
 - Using the .parse_args() method to access the arguments created: i.e.: "args = parser.parse_args()"
 - Enhancing the output of the -h/--help flag by providing a help= parameter to each .add_argument call: i.e: help="'this is some help text'"
 - Typing an argument created with the .add_argument method by providing a "type=" parameter: i.e.: "type=int"
 - Making an  argument a boolean flag with the "action=" parameter: i.e.: "action='store_true'"
 - Combining Positional and Optional arguments
 - Using the "choice=[1, ..., n]" .add_argument option to limit the use of a flag: i.e. "choices=[0, 1, 2]"
 - Use fo the "count=" .add_argument parameter to allow for a flag to be used multiple times on the same instance of a command: i.e. "action="'count'"
 - Allowig conflicting parameters with the .add_mutually_exclusive_group() method. 
 - Supplying a program description for use by the -h/--help help function using the argparse.ArgumentParser() method: i.e. argparse.ArgumentParser(description="calculate X to the power of Y")
 
 

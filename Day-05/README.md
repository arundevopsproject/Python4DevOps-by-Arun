
# Command Line Arguments in Python

    Command line argument is a way of managing the script or program externally by providing the program name and the parameters that we pass when the program is under execution from the command line. These are used to customize the program’s behaviour without changing the source code.

# There are 3 important modules available in python to use command line arguments.
    1. Python sys module
    2. Python getopt module
    3. Python argparse module

# 1.Python sys module:

    • The sys module offers variables and functions for modifying many elements of the Python runtime environment.
    • This module gives users access to some variables that the interpreter uses or maintains as well as functions that have close relationships with the interpreter.
    • Sys module provides functions and variables used to manipulate the different parts of python run time environment.

# Variables in Sys Module:
    Python offers a number of ways to handle command-line parameters. The most popular approach is to use the sys.argv list, which is accessible via the sys module.
    One of the mostly used variables is sys.argv used to access the command line arguments given during run time.

# Sys.argv variables in Sys Module:
    • Sys.argv is a list structure to receive all the command line arguments passed during program execution from command line.
    • It’s a collection of command-line options. The quantity of command line arguments is provided by len(sys.argv).
    • The name of the running Python script is sys.argv[0].
    • To use sys.argv, we need to import the sys module.
    • In Python, the command-line arguments provided to the script are listed in the sys.argv list.
        o The first element is the name of the script itself (sys.argv[0]), and the subsequent elements are any additional arguments that were supplied after the script name.
        o The sys.argv list stores a string representation of each command-line argument.
    • Getting to Command-Line Arguments, we can access the sys.argv list by importing the sys module (import sys).
        o By referencing components of the sys.argv list, the command-line arguments can be accessed and handled.
    • Handling Command-Line Arguments, we can carry out a number of operations on the command-line arguments once we have access to the sys.argv list.

# Example 1: Print all arguments passed from command line

    # Command line arguments using sys.argv
    import sys
    
    # sys.argv is a list contains all arguments passed from command line
    py_list = sys.argv
    print('py_list: ', py_list)
    arguments = len(sys.argv)
    print('Number of arguments: ', arguments)
    
    # The first argument is file name
    print('py file name: ', py_list[0])
    print('Iteration over passed arguments:')
    for item in py_list:
    print(item)

# Explanation of the above code:
    This script is a simple Python program that shows how to use the sys.argv list to read command-line arguments supplied to a Python script.

    Let’s go over the dialogue line by line:
    1. import sys: This line imports the sys module, giving you access to a number of system-specific parameters and functions.
    2. py_list = sys.argv: In this case, the variable py_list is set to the sys.argv list. Python stores the command-line arguments given to the script in a list called sys.argv. The name of the script itself appears as the first member of this list (sys.argv[0]).
    3. print(‘py_list:’, py_list): This statement publishes the information contained in the py_list variable, which shows all of the command-line parameters supplied to the script.
    4. arguments = len(sys.argv): The variable arguments is given the length of the sys.argv list in this line. It provides us with the overall number of command-line arguments the script received.
    5. print(‘Number of arguments:’, arguments): This line outputs the total number of arguments the script received on the command line.
    6. print(‘py file name:’, py_list[0]): This line displays the name of the Python script that is kept in sys.argv[0].
    7. print(“Iteration over passed arguments:”): This line produces a header indicating that the loop that comes next will iterate over the parameters that were passed.
    8. for each item in py_list: The py_list list’s elements are iterated over in this loop.
    Prepared by Arun Baidya
    9. print(item): This line prints each item in the py_list list, which is equivalent to each argument given as part of the script’s command-line.
    This script will display details about the arguments when you run it from the command line and supply them.


# Example 2: Print all passed arguments without file name

    # Command line arguments using sys.argv
    import sys
    
    # sys.argv is a list contains all arguments passed from command line
    py_list = sys.argv
    print('py_list: ', py_list)
    arguments = len(sys.argv)
    print('print all passed arguments without file name:')
    for i in range(1, arguments):
    print(py_list[i])


# 2.Python getopt module:
    Getopt is an inbuilt bash feature used to provide the options from command line. Getopt is used by shell procedure to pass the positional parameters of string contains the option characters to be recognized.
    Prepared by Arun Baidya
    Python getopt module is a parser, used for analysing command line options, given in command line arguments in sys.argv. Parsing means dividing the commands into smaller parts and trying to understand.
    To use this module, we need to import it, using the command import getopt
    The main function provided by this module is getopt() function. The purpose of this getopt() function is to parse command line options and parameter list.

# Syntax: getopt.getopt(args,options,[long options])

# Where:
    • Args: this is the arguments passed to the function. It is the classification of the arguments to be analyzed and derived from sys.argv[1:] i.e. arguments from first position to all command line arguments. \
    • Options: These are also known as short options. This is the second parameter passed in the function. The options are the characters followed by colon; the script need to recognize. option is expected to have an argument which should be separated by white space. Short option should have prefix with ‘-‘.
    • Long options: This is the third parameter passed to the python getopt function. It is the sequence of the strings with the long names known as long options alternative to the short options. Long option names can be consisting of more than one single character, and its name should have prefix with ‘- -’
    If any long option needs an argument, then it should be followed by an equal to ‘=’ sign.
    • Return value: Return value consisting of two elements: the first is a list of (option, value) pairs and second element is a list of arguments that are left when the options list was stripped.

# Example: Python getopt Module

    # Script: getopt_example.py
    import sys
    import getopt
    # Get command-line arguments (excluding script name)
    args = sys.argv[1:]
    Prepared by Arun Baidya
    # Define short and long options
    # -h : help
    # -n : name
    # -a : age
    opts, vals = getopt.getopt(args, "hn:a:", ["help", "name=", "age="])
    for opt, val in opts:
    if opt in ("-h", "--help"):
    print("Usage: python getopt_example.py -n <name> -a <age>")
    sys.exit()
    elif opt in ("-n", "--name"):
    name = val
    elif opt in ("-a", "--age"):
    age = val
    print("Name:", name)
    print("Age:", age)


# How to Run?
    $ python getopt_example.py -n Alice -a 25

# 3.Python argparse module:
Argparse is a widely used in-built command line parser module to parse the input entered through the command line interface. To use this, we need to import argparse module.
This module was released with python 3.2. Python argparse module allows to

    1.Parse command- line arguments and options.
    2.Take a variable number of parameters in a single option.
    3.Provide subcommands in CLI.

    # Creating parser object:
    import argparse
    parser=argparse.ArgumentParser()
    
    # Syntax for creating ArgumentParser Objects:
    argparse.ArgumentParser(
        prog=None,
        usage=None,
        description=None,
        epilog=None,
        parents=[],
        formatter_class=argparse.HelpFormatter,
        prefix_chars='-',
        fromfile_prefix_chars=None,
        argument_default=None,
        conflict_handler='error',
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True
    )


# Brief Explanation of Common Parameters
    • prog → Program name (default: script name)
    • usage → Usage message shown on help
    • description → Description of what the program does
    • epilog → Text shown after help message
    • parents → Parent parsers whose arguments are inherited
    • formatter_class → Controls help message formatting
    • prefix_chars → Characters used for optional arguments (default -)
    • fromfile_prefix_chars → Read arguments from a file
    • argument_default → Default value for arguments
    • conflict_handler → Action on conflicting arguments (error or resolve)
    • add_help → Automatically add -h/--help
    • allow_abbrev → Allow abbreviated long options
    • exit_on_error → Exit on parsing errors (Python 3.9+)


# Example: Python argparse Module

    # Script: argparse_example.py
    
    import argparse
    
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Example program using argparse"
    )
    
    # Add arguments
    parser.add_argument(
        "-n", "--name",
        help="Enter your name",
        required=True
    )
    parser.add_argument(
        "-a", "--age",
        type=int,
        help="Enter your age",
        required=True
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Use arguments
    print("Name:", args.name)
    print("Age:", args.age)


======================================================================================================================


# Environment-Based Deployment Script:

    # Use case: Deploy to dev / staging / prod using variables
        environment = "production"
        app_name = "web_app"
        version = "v1.2.3"
        print(f"Deploying {app_name} version {version} to {environment} environment")
    
    
# Server Health Check Script:
    
    # Use case: Check server status in monitoring. In this example, Variables store dynamic monitoring values.
        server_name = "web-server-01"
        cpu_usage = 68
        memory_usage = 72
        if cpu_usage > 80 or memory_usage > 80:
            print(f"ALERT: High usage on {server_name}")
        else:
            print(f"{server_name} is healthy")


# CI/CD Build Information Script:
    # Use case: Used in Jenkins/GitLab pipelines. In this example, Variables track pipeline metadata.
        build_id = 102
        branch = "main"
        status = "SUCCESS"
        print("Build ID:", build_id)
        print("Branch:", branch)
        print("Build Status:", status)
    

# Package Installation Automation:
    # Use case: OS provisioning / configuration management. Here, Variables help automate repetitive configuration tasks.
        package_name = "nginx"
        state = "installed"
        print(f"Package {package_name} is {state}")
    

# Log File Rotation Script:
    # Use case: Managing application logs. Here, Variables store paths and thresholds.
        log_file = "/var/log/app.log"
        max_size_mb = 100
        current_size_mb = 120
        if current_size_mb > max_size_mb:
            print(f"Rotating log file: {log_file}")
    
    
# Docker Container Management:
    # Use case: Container automation. Here, Variables define container properties.
        container_name = "nginx_container"
        image_version = "nginx:latest"
        status = "running"
        print(f"Container {container_name} using {image_version} is {status}")
    

# Cloud Resource Configuration:
    # Use case: AWS/Azure automation scripts. Here, Variables make scripts cloud-agnostic and scalable.
        instance_type = "t2.micro"
        region = "us-east-1"
        instance_count = 3
        print(f"Launching {instance_count} instances of type {instance_type} in {region
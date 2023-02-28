import logging
import configparser
import sys

if __name__ == '__main__':

    # Create a config parser and read the config file
    config = configparser.ConfigParser()
    config.read('3461-Project1.conf')

    # Create the logger file
    logging.basicConfig(filename='3461-Project1.log', level=logging.INFO)
    logging.info("project1 starting")
    logging.info("Logging to 3461-Project1.log")
    logging.info("Log level set to INFO")

    # Split the config file into it's subsequent sections
    configSections = config.sections()

    # Print configuration options
    print("Configuration File Contents: ")
    logging.info("Configuration File Contents:")
    for section in configSections:

        # Print section name
        print("\tSection: " + section)
        logging.info("\tSection: " + section)

        # Print options
        options = dict(config.items(section))
        for key in options:
            print("\t\toption " + key + " = " + options[key])
            logging.info("\t\toption " + key + " = " + options[key])

    numInputs = 0

    # Main loop with user input
    while True:

        numInputs += 1

        # Collect user input and print to both console and logger file
        userString = input("project1 " + str(numInputs) + " > ")
        print("Entered String   = " + userString)
        logging.info(userString)

        # Make the first word uppercase
        tokens = userString.split(" ")
        tokens[0] = tokens[0].upper()

        # Rebuild the string
        returnString = ""
        for token in tokens:
            returnString += token
            returnString += " "

        # Print the processed string to the console and the logger
        print("Processed String = " + returnString)
        logging.info(returnString)

        # Quit if the first token was quit
        if tokens[0] == "QUIT":
            break

    # Once we quit, print shutting down and exit
    print("Shutting down ...")
    logging.info("Shutting down ...")
    sys.exit(0)

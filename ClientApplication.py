import json
import logging
import configparser
import socket
import sys

if __name__ == '__main__':

    # Create a config parser and read the config file
    config = configparser.ConfigParser()
    config.read('clientConfig.conf')

    # Split the config file into it's subsequent sections
    configSections = config.sections()

    for section in configSections:

        # Check for 'logger' section
        if section == "logger":

            # Split logger section into components
            loggerOptions = dict(config.items(section))

            # Store relevant variables
            fileName = loggerOptions["logfile"]
            fileLevel = loggerOptions["loglevel"]
            logHost = loggerOptions["loghost"]

            logging.basicConfig(filename=fileName, level=logging.INFO)
            logging.info("Project2 starting")
            logging.info("Logging to " + fileName)
            logging.info("Log level set to " + fileLevel)

        # Check for 'project2' section
        if section == "project2":

            # Split project2 section into components
            projectOptions = dict(config.items(section))

            # Store relevant variables
            serverHost = projectOptions["serverhost"]
            serverPort = projectOptions["serverport"]

    numInputs = 0

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverHost, int(serverPort)))

    # Main loop with user input
    while True:

        numInputs += 1

        # Collect user input and print to both console and logger file
        userString = input("project2-client " + str(numInputs) + " > ")
        logging.info(userString)

        # Make the first word uppercase
        tokens = userString.split(" ")
        tokens[0] = tokens[0].upper()

        request = tokens[0]
        parameters = tokens[1:]

        # Rebuild the string
        parameter = ""
        for token in parameters:
            parameter += token
            parameter += " "

        # Print the processed string to the console and the logger
        logging.info(parameter)

        package = {"request":request, "parameter": parameter}
        data = json.dumps(package)

        clientSocket.send(bytes(data,encoding="utf-8"))

        response = json.loads(clientSocket.recv(1024).decode())
        print("Response Recieved: " + response["parameter"])

        # Quit if the first token was quit
        if tokens[0] == "QUIT":
            break


    # Once we quit, print shutting down and exit
    print("Shutting down ...")
    logging.info("Shutting down ...")
    sys.exit(0)

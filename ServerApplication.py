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

    # Create a socket connection and bind it
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((serverHost, int(serverPort)))
        s.listen()
        conn, addr = s.accept()

        # Print out the server starting
        print(f"Server starting on {serverHost}")
        with conn:
            while True:
                data = conn.recv(1024).decode('utf-8')    # this returns a JSON-formatted String
                if not data:
                    break

                # Send the data
                parsed_data = json.loads(data)
                conn.send(data.encode())

        # Shut down the server
        print("Server shutting down...")
        logging.info("Server shutting down...")
        conn.send("Server shutting down...".encode())

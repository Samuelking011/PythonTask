#command to import an open source library called OS.
import os

#conditional statement to check if directory config already exist.
#if the directory already exist, a user friendly message display to notify users
#if such directory does not exisit a new directory is created
if os.path.exists("Config"):
    print("This directory already exist")
else:
    os.mkdir("Config")
    print("The directory config created successfully")

#conditional statement to check if file db.config already exisit in directory config.
#if the file  already exist, a user friendly message display to notify users
#if such file does not exisit a new directory is created
if os.path.exists("Config/db.config"):
    print("file with name db.config already exist")
else:
    file = open("Config/db.config", "w")
    print("File db.config successfully created inside the config directory.")

#conditional statement to check if file webserver.config already exisit in directory config.
#if the file  already exist, a user friendly message display to notify users
#if such file does not exisit a new directory is created
if os.path.exists("Config/webserver.config"):
    print("file with name webserver.config already exist")
else:
    file = open("Config/webserver.config", "w")
    print("File webserver.config successfully created inside the config directory.")


#command to open and read file db.config inside directory Config.
file = open("Config/db.config", "r")
print(file.read())
#command to close the file.
file.close()

#command to open and write into file webserver.config inside directory Config.
file = open("Config/webserver.config", "w")
file.write("Prof Dotun is an amazing instructor. He is really calm, resourceful, and eager to teach. He wants all his student to be successful.")
#command to open and read file webserver.config inside directory Config.
file = open("config/webserver.config", "r")
print(file.read())
#command to close the file.
file.close()



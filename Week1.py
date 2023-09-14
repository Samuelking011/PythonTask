import os

#if os.path.exists("config"):
#    print("This directory already exist")
#else:
#    os.mkdir("config")
#    print("The directory config created successfully")


#if os.path.exists("config/db.config"):
#    print("file with name db.config already exist")
#else:
#    file = open("config/db.config", "w")
#    print("File db.config successfully created inside the config directory.")


#if os.path.exists("config/webserver.config"):
#    print("file with name webserver.config already exist")
#else:
#    file = open("config/webserver.config", "w")
#    print("File webserver.config successfully created inside the config directory.")

file = open("config/webserver.config")
print(file.read())



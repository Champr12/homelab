# Import modules to interact with the OS
import os
import subprocess

# Define the directories as a list
directories = [
    "/home/localusr/docker/plex/media/Movies",
    "/home/localusr/docker/plex/media/Shows"
]

# Function to check if the directories are empty
def is_directory_empty(directory):
    # os.listdir lists the content in the specified directory
    return len(os.listdir(directory)) == 0

# Loops over the directories list and check if the directories are empty, run the mount commands if the directories are empty
# the mount commands are "rclone mount whatbox:/home/champr12/Movies /home/localusr/docker/plex/media/Movies --allow-other --daemon" 
# and "rclone mount whatbox:/home/champr12/Shows /home/localusr/docker/plex/media/Shows --allow-other --daemon" 
for directory in directories:
    if is_directory_empty(directory) and directory == "/home/localusr/docker/plex/media/Movies":
        subprocess.run(["rclone", "mount", "whatbox:/home/champr12/Movies", "/home/localusr/docker/plex/media/Movies", "--allow-other", "--daemon"])
    elif is_directory_empty(directory) and directory == "/home/localusr/docker/plex/media/Shows":
        subprocess.run(["rclone", "mount", "whatbox:/home/champr12/Shows", "/home/localusr/docker/plex/media/Shows", "--allow-other", "--daemon"])       

# Restart the Plex Docker container
subprocess.run(["sudo","docker", "restart", "plex"])

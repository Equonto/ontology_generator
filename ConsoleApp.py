

import colorama
from colorama import Fore
from FileIo import folder_exists
from CreateOntology import CreateOntology

# Initialize Colorama
colorama.init(autoreset=True)

# Prompt the user for input
config_folder_name = input(Fore.GREEN + "Enter the name of config folder for this ontology: ")

# Print the user's response
print("You entered:", config_folder_name)
print("Creating ontologies...")

if (folder_exists("config/"+config_folder_name) == False):
    print(Fore.RED + "The folder does not exist. Please check the name and try again.")
    exit(1)

creator = CreateOntology(config_folder_name)
creator.create_ontologies()

print(Fore.GREEN + "Process complete. Please check the config/<ontology>/output folder.")
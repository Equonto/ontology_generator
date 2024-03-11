
import os
import glob
import shutil
import json

def clear_output_directory(folder_location):
    files = glob.glob(folder_location+"/*")
    for f in files:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

def move_files(src_folder, dst_folder):
    files = glob.glob(src_folder+"/*")
    for f in files:
        shutil.copy(f, dst_folder)

def read_json_file(file_path):
    with open(file_path, "r") as file:
        json_str = file.read()
    return json.loads(json_str)

def folder_exists(folder_location):
    return os.path.exists(folder_location)

def delete_file(file_path):
    os.remove(file_path)

def list_files_in_directory(directory):
    return os.listdir(directory)

def get_ontology_filename(ontology_json, extension="ttl"):
    version_number = ontology_json['ontology_version'].replace(".", "_")
    filename = ontology_json['ontology_filename']
    return f"{filename}_v{version_number}.{extension}"

def get_ontology_shortname(ontology_json):
    return ontology_json['ontology_shortname']

def get_ontology_settings(location):
    settings = read_json_file("config/"+location+"/settings.json")
    return settings

def directory_exists(directory):
    return os.path.exists(directory)
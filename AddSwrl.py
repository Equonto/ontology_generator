
from FileIo import read_json_file, get_ontology_filename, get_ontology_settings, directory_exists, append_file_to_file

def get_filename_that_matches_shortname(location, shortname):
    settings = get_ontology_settings(location)
    for setting in settings:
        if setting["ontology_shortname"] == shortname:
            return get_ontology_filename(setting)

def create_swrl(location):
    if (directory_exists("config/"+location+"/swrl") == False):
        return
    swrl_settings = read_json_file("config/"+location+"/swrl/settings.json")
    for setting in swrl_settings:
        ontology_filename = get_filename_that_matches_shortname(location, setting["ontology_shortname"])
        swrl_filename = setting["rules_filename"]
        append_file_to_file("config/"+location+"/swrl/"+swrl_filename, "config/"+location+"/output/"+ontology_filename)
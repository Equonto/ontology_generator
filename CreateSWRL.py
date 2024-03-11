# add swrl rules

from FileIo import read_json_file, get_ontology_filename, get_ontology_settings, directory_exists
from owlready2 import *
import json

def add_swrl(location):
    if (directory_exists("config/"+location+"/swrl") == False):
        return
    rules = read_json_file("config/"+location+"/swrl/swrl_rules.json")
    for rule in rules:
        ontology = load_ontology(location, get_filename_that_matches_shortname(location, rule["ontology_shortname"]), rule["imports"])
        ontology = add_swrl_rule(rule, ontology)
        save_ontology(ontology)
        cleanup(ontology)

def read_json_file(file_path):
    with open(file_path, "r") as file:
        json_str = file.read()
    return json.loads(json_str)

def load_ontology(location, ontology_filename, imports=[]):
    onto_path.append("config/"+location+"/output")
    for i in imports:
        owlready2.get_ontology("file://config/"+location+"/output/"+i).load()
    ontology = owlready2.get_ontology("file://config/"+location+"/output/"+ontology_filename).load()
    return ontology

def add_swrl_rule(rule, ontology):
    with ontology:
        print(list(ontology.object_properties()))
        r = Imp()
        r.set_as_rule(rule["value"])
        return ontology

def save_ontology(ontology):
    ontology.save()

def cleanup(ontology):
    ontology.destroy()

def get_filename_that_matches_shortname(location, shortname):
    settings = get_ontology_settings(location)
    for setting in settings:
        if setting["ontology_shortname"] == shortname:
            return get_ontology_filename(setting, "xml")
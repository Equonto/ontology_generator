from FileIo import *
from RunLutra import run_lutra_process, run_docttr
from RunWidoco import run_widoco
from AddSwrl import create_swrl

class CreateOntology:

    def __init__(self, location) -> None:
        self.location = location
        self.ontologies = []
        for onto in get_ontology_settings(location):
            self.ontologies.append({
                "ontology_filename": get_ontology_filename(onto),
                "ontology_shortname": get_ontology_shortname(onto)
            })

    def prepare_output_directory(self):
        clear_output_directory("config/"+self.location+"/output")
        move_files("config/"+self.location+"/imports", "config/"+self.location+"/output")

    def generate_ontologies(self):
        for ontology in self.ontologies:
            run_lutra_process(ontology["ontology_filename"], ontology["ontology_shortname"], self.location)
        create_swrl(self.location)

    def generate_documentation(self):
        run_docttr(self.location)

    def generate_linked_data(self):
        for ontology in self.ontologies:
            run_widoco(ontology["ontology_filename"], ontology["ontology_shortname"], self.location)

    def create_ontologies(self):
        print("Preparing output directory")
        self.prepare_output_directory()
        print("Generating ontologies")
        self.generate_ontologies()
        print("Generating template documentation")
        self.generate_documentation()
        print("Generating ontology documentation")
        self.generate_linked_data()
        print("Process complete. Please check the config/output folder.")
        input("Press Any Key to Exit...")
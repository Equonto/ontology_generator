from FileIo import clear_output_directory, move_files, read_json_file
from RunLutra import run_lutra_process, run_docttr
from RunWidoco import run_widoco

def get_ontology_filename(ontology_json):
    version_number = ontology_json['ontology_version'].replace(".", "_")
    filename = ontology_json['ontology_filename']
    return f"{filename}_v{version_number}.ttl"

def get_ontology_shortname(ontology_json):
    return ontology_json['ontology_shortname']

def get_ontology_settings():
    settings = read_json_file("generator/config/settings.json")
    return settings

def prepare_output_directory():
    clear_output_directory("generator/config/output")
    move_files("generator/config/imports", "generator/config/output")

def generate_ontologies():
    for ontology in get_ontology_settings():
        run_lutra_process(get_ontology_filename(ontology), get_ontology_shortname(ontology))

def generate_documentation():
    run_docttr()

def generate_linked_data():
    run_widoco("StaticProcedureOntology_v0_0_1.ttl", "spo")
    run_widoco("ConditionalMaintenanceTaskOntology_v0_0_1.ttl", "cmto")

if __name__ == "__main__":

    ontologies = ["spo", "cmto"]

    print("Preparing output directory")
    prepare_output_directory()
    print("Gennerating ontologies")
    generate_ontologies()
    print("Generating template documentation")
    generate_documentation()
    print("Generating ontology documentation")
    generate_linked_data()
    print("Process complete. Please check the config/output folder.")
    input("Press Any Key to Exit...")
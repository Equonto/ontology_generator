import rdflib
from FileIo import list_files_in_directory, delete_file

def convert_ontology_filetypes(location):
    location = "config/"+location
    ontology_filenames = list_files_in_directory(location+"/output")
    for ontology_filename in ontology_filenames:
        g = rdflib.Graph()
        if (len(ontology_filename.split(".")) == 2):
            format = ontology_filename.split(".")[1]
            if format == "owl" or format == "rdf":
                format = "xml"
            if ((format == "ttl" or format == "xml") and ontology_filename != "catalog-v001.xml"):
                g.parse(location+"/output/"+ontology_filename, format=format)
                #delete_file(location+"/output/"+ontology_filename)
                ontology_filename = ontology_filename.replace(format, "xml")
                g.serialize(destination=location+"/output/"+ontology_filename, format="xml")
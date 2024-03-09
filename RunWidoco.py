import subprocess
import os

def run_widoco(ontology_filename, ontology_shortname, location):

    command = """
        java -jar widoco-1.4.20-jar-with-dependencies_JDK-17.jar \\
        -ontFile output/"""+ontology_filename+"""\\
        -outFolder output/widoco/"""+ontology_shortname+""" \\
        -confFile widoco_conf/"""+ontology_shortname+"""\\
        -rewriteAll \\
        -saveConfig output/widoco/"""+ontology_shortname+"""/config \\
        -htaccess \\
        -oops \\
        -ignoreIndividuals \\
        -includeAnnotationProperties \\
        -displayDirectImportsOnly \\
        -excludeIntroduction \\
        -uniteSections \\
        -noPlaceHolderText"""

    print(command)


    result = subprocess.run(command
        , stdout=subprocess.PIPE
        , stderr=subprocess.PIPE
        , shell=True
        , cwd="config/"+location)
        
    print(result.stderr.decode("utf-8"))
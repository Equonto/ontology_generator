# Ontology Generator

This repository contains the necessary code to generate an Ontology, OTTR Documentationa and Widoco Documentation.

## Getting Started

### Prerequisites

Before you begin, ensure you have a Python virtual environment (venv) set up and that you're familiar with activating venvs in your Integrated Development Environment (IDE). This project requires Python 3 and `pip`.

### Installation

1. **Set Up Virtual Environment**

   If you haven't already created a virtual environment for Python projects, you can set one up by navigating to your project directory in the terminal and running: ```python3 -m venv venv```


1. **Activate Virtual Environment**

    Activate your virtual environment to ensure that all dependencies are installed within this isolated environment. Activation commands vary depending on your operating system:

- **Linux/MacOS:**

  ```source venv/bin/activate```

- **Windows:**
 ``` .\venv\Scripts\activate```

3. **Install Dependencies**

With your virtual environment activated, install the project dependencies using: ```pip install -r requirements.txt```

o update your requirements.txt with the latest packages, you can create a snapshot of the installed packages using: ```pip3 freeze > requirements.txt```

### Generating an Ontology

1. Prepare Configuration

    To generate a new ontology, first prepare the necessary configuration folders within the config directory of this project. The structure and content of these folders will depend on the specifics of the ontology you wish to generate.

2. Run the Application

    With your configurations set and dependencies installed, you're ready to generate the ontology. Run the following command from the root of your project directory: ```python3 ConsoleApp.py```

<!-- README content provided by OpenAI's ChatGPT -->

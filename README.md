# AirBnB Clone Project

Welcome to the AirBnB clone project! This project involves building a simplified version of the AirBnB web application, focusing on creating a command interpreter and setting up a storage system.

## Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Storage Abstraction](#storage-abstraction)
- [Command Interpreter](#command-interpreter)
- [Data Model](#data-model)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project involves building a command-line interface to manage AirBnB objects, including users, states, cities, and places. The first step is to create a command interpreter and implement a storage system that allows objects to be serialized and persisted to a file in JSON format. The aim is to establish a solid foundation for future development, including HTML/CSS templating, database storage, API integration, and front-end integration.

Please read the AirBnB concept page to understand the core concepts and objectives of this project.

## Project Structure

The project is structured to achieve the following key goals:
- Implement a parent class (`BaseModel`) for initialization, serialization, and deserialization of future instances.
- Establish a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes for AirBnB objects (e.g., User, State, City, Place) that inherit from `BaseModel`.
- Develop the first abstracted storage engine using file storage.
- Create unit tests to validate classes and the storage engine.
- Implement a command interpreter for managing objects.
- Enable storing and persisting objects to a JSON file.

## Storage Abstraction

The storage engine in this project serves as an abstraction between the objects and their storage/persistence. It ensures that the console code and future components like the front-end and RestAPI are decoupled from the storage implementation. This abstraction allows for easy switching between storage types without modifying the entire codebase.

## Command Interpreter

The command interpreter is a vital tool in this project, allowing users to interact with and manage AirBnB objects. It facilitates the creation, updating, and deletion of objects via a console interface. Additionally, it provides the ability to store and persist objects to a JSON file using the established storage abstraction.

## Data Model

The data model comprises various classes representing AirBnB objects. These classes inherit from the `BaseModel` and define the structure and behavior of the corresponding objects, ensuring consistency and organization within the application.

## Usage

### Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB-Clone-Project
   ```

3. Ensure you have Python installed. This project is compatible with Python 3.x.

### Authors

Contributors to this project:
- [Phindulo Mulaudzi](https://github.com/your_github_profile)
- [Another Contributor](https://github.com/another_contributor)

### Starting the Command Interpreter

To start the command interpreter, run the `console.py` script:
```bash
./console.py
```

### Interactive Mode

In interactive mode, you can directly enter commands and see the output:
```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
```

### Non-Interactive Mode

You can also use the command interpreter in non-interactive mode by passing commands via standard input (pipe):
```bash
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

Or you can use a file to input commands:
```bash
cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

In non-interactive mode, the commands are read from standard input or a file, and the output is displayed accordingly.

### Examples

Here are some examples of commands you can use in the interactive mode:
- `help`: Displays the list of available commands and their descriptions.
- `create <class_name>`: Creates an instance of the specified class.
- `show <class_name> <id>`: Displays information about an instance based on the class name and ID.
- `all <class_name>`: Displays all instances of a specific class or all instances if no class is provided.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Updates the specified attribute of an instance.
- `destroy <class_name> <id>`: Deletes an instance based on the class name and ID.

Feel free to explore and use these commands to manage AirBnB objects efficiently.

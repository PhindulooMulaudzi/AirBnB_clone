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

Follow the instructions in the AirBnB concept page to set up and run the project. Use the command interpreter to manage AirBnB objects efficiently. Refer to the unittests to validate the functionality of the classes and storage engine.

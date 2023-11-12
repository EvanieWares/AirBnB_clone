# AirBnB clone - The console
Welcome to the AirBnB clone project! This project is the first step towards building a full web application: the AirBnB clone. The primary goal of this project is to create a command interpreter that manages AirBnB objects, such as User, State, City, and Place. This command interpreter is crucial for the subsequent projects involving HTML/CSS templating, database storage, API, and front-end integration.

## Commands
The command interpreter allows you to interact with and manage AirBnB objects. It operates in interactive mode, providing a shell-like experience. The following commands are supported:

* **EOF**: Ends the command interpreter.
* **quit**: Exits the program.
* **create <class>**: Creates a new instance of the specified class (e.g., BaseModel), saves it to the JSON file, and prints the **id**.
  + Example: `create BaseModel`
* **show <class> <id>**: Prints the string representation of an instance based on the class name and **id**.
  + Example: `show BaseModel 1234-1234-1234`
* **destroy <class> <id>**: Deletes an instance based on the class name and id, saving the change into the JSON file.
  + Example: `destroy BaseModel 1234-1234-1234`
* **all <class>**: Prints all string representations of instances based on the class name.
  + Example: `all BaseModel` or `all`
* **update <class> <id> <attribute> <value>**: Updates an instance based on the class name and id by adding or updating attributes, saving the change into the JSON file.
  + Example: `update BaseModel 1234-1234-1234 email "aibnb@mail.com"`

## How to start
To start the AirBnB clone command interpreter, run the following command in your terminal:
``` bash
$ ./console.py
```
When you run this command the following prompt will appear:
``` bash
(hbnb) 
```
This prompt designates you are in the "HBnB" console

## How to use
Once the command interpreter is running, you can interact with it by entering commands. Use the `help` command to see the list of available commands and their descriptions.
``` bash
(hbnb) help
```

### Examples

```
$ ./console.py
(hbnb) create BaseModel
1234-1234-1234
(hbnb) show BaseModel 1234-1234-1234
[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323323), 'updated_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323326)}
(hbnb) update BaseModel 1234-1234-1234 first_name "person"
(hbnb) all BaseModel
["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323323), 'updated_at': datetime.datetime(2023, 11, 12, 13, 48, 04, 919499), 'first_name': 'person'}"]
(hbnb) quit
$
```

Feel free to explore and manage your AirBnB objects using the provided command interpreter!

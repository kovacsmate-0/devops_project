# Junior DevOps Engineer test project

## Overview
This application handles POST requests with a parameter named 'string' and a string-type value. Upon receiving a valid 'string' parameter, the application returns the same string with swapped case ('abcDEF' becomes 'ABCdef') as the response. Errors are properly handled by the application. The test script implemented by pytest and the app served by gunicorn.

## Requirements
- `Python 3.8` or later
- `pytest` (for testing)
- `Flask`
- `requests` (for running the test script)
- `Docker` (for containerization)
- `docker-compose`
- `Vagrant` and `Virtualbox` (for the virtual environment) [Optional]

## Installation
### 0. [Optional]
If you are working on a Windows machine, you will need a virtual Linux environtment to run this application.
To setup this virtual environment make sure you have Virtualbox and Vagrantfile installed on your computer, then follow these steps:

1. Start the VM using Vagrant. You have to be inside that folder where the Vagrantfile is.

        vagrant up

2. To login to the machine, you need to use SSH:

        vagrant ssh

3. You are now inside the VM, if you want to shut down  or remove the machine completely:

        vagrant halt          # shut down
        vagrant destroy       # remove


### 1. Clone the projects repository to your local computer:
        git clone https://github.com/kovacsmate-0/devops_project.git

        cd devops_project

### 2. Install the required dependencies:
        pip install -r requirements.txt


        

## Running the Application
There are 2 ways to run the case swapper app:
- Running locally
- Using Docker

### Running locally
1. To start the app locally, use the following command:

        python app.py
   
3. Now the application listening for POST requests at: `http://127.0.0.0:8000`
4. To test the app you can use **curl** from another machine:

        curl -X POST -H "Content-Type: application/json" -d '{"string": "abcDEF"}' http://127.0.0.1:8000/
5. Output should be:

        {"swapped_string": "ABCdef"}
6. To stop the app, use CTRL + C.


### Using Docker
1. To start the app you have to make sure that Docker and docker-compose are installed on your computer.

2. You also need a Dockerfile and a docker-compose.yaml file.
Dockerfile:



        # docker-compose.yaml
   
        version: '3'
        
        services:
          web:
            build:
              context: .
              dockerfile: Dockerfile
            ports:
              - "8000:8000"

4. 
  

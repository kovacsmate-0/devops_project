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
- Using Docker, docker-compose, gunicorn

### Running locally
1. To start the app locally, use the following command:

        python app.py
   
3. Now the application listening for POST requests at: `http://127.0.0.0:8000`
4. To test the app you can use **curl** from another machine:

        curl -X POST -H "Content-Type: application/json" -d '{"string": "abcDEF"}' http://127.0.0.1:8000/
5. Output should be:

        {"swapped_string": "ABCdef"}
6. To stop the app, use CTRL + C.

### Deploy application using `gunicorn`

To run the app with gunicorn you will need a server entrypoint script [wsgi_server.py]

        from app import app
        
        if __name__ == "__main__":
            app.run()
        
In order to test the app deployment with gunicorn use the following command:

        gunicorn wsgi_server:app -b 0.0.0.0:8000


For windows users there is an alternative (pip install waitress)

        waitress-serve --listen=0.0.0.0:8000 wsgi-server:app


### Packaging with Docker

For the packaging you can use a set of Shell scripts.
1. Build Docker image 

        #!/bin/bash
        
        docker build -t devops_project_app .
   You can use the following command in cmd to run the script:
   `./build_docker_image.sh`

2. Start Docker instance

        #!/bin/bash
        
        docker run -d -p 8000:8000 --name devops_project_instance devops_project_app
   You can use the following command in cmd to run the script:
   `./start_docker_instance.sh`
   The application is now running on `http://127.0.0.0:8000` and listening for POST requests.
   
4. Stop and Remove instance

        #!/bin/bash
        
        docker stop devops_project_instance
        docker rm devops_project_instance
   You can use the following command in cmd to run the script:
   `./stop_and_remove_instance.sh`
   
### Using docker-compose
1. To start the app you have to make sure that Docker and docker-compose are installed on your computer.

2. You also need a Dockerfile and a docker-compose.yaml file.
   
   Dockerfile:
        
                FROM python:3.8
                
                WORKDIR /app
                
                COPY requirements.txt /app/
                RUN pip install --no-cache-dir -r requirements.txt
                
                COPY . /app
                
                CMD ["gunicorn", "wsgi_server:app", "-b", "0.0.0.0:8000"]
        
   docker-compose.yaml
           
                version: '3'
                
                services:
                  web:
                    build:
                      context: .
                      dockerfile: Dockerfile
                    ports:
                      - "8000:8000"

3. Build and run Docker containers:

        docker-compose build      
        docker-compose up -d       # -d: means run the app in the background

4. The app is now accessible on: `http://127.0.0.0:8000`
5. If your want to stop and delete Docker container, then:

        docker-compose down

## Testing
You can use `pytest` and `requests` to test the swapcase app.

1. Make sure that the application is running via `docker-compose` or `gunicorn`.
2. Then run the tests:

        pytest test_app.py
The test script covers both success and failure cases.
  

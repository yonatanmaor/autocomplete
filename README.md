# autocomplete API

To run, first create a docker image using the provided Dockerfile:

`cd <path-to-project-root-folder>`

`docker build -t autocomplete_service .`


Then run the docker image: 

`docker run -p 2222:1188 autocomplete_service`


Now test the availability of the rest service using http://localhost:2222/is_alive



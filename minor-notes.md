## Auto Answered Doubts
-First to implement the tests, I was trying to use a creation and deletion of a testing database but seeing that nothing is ever written to the database there is no point in creating another one for testing, that will just increase the tester workload with something they were not expecting. 

## Comment structure
- Comments that are obvious after the first read of the code should not be kept in the code augmenting the cognitive load and the time spent reading the code of the developers.
    They can be kept in this file.
  
## Investigating the docker image

- I used to use an ubuntu image but ubuntu has been declining for a few years although serverwise keeps been a nice option I think now is the time to change to a python image based on debian.
- The version of the base image is 3.8 and not 3.11 to take advantange of the longer release/debugging time passed in the community.

## Building rest-service image / [Dockerfile](./flask-jwt-auth/Dockerfile)
- Python 3.8 is currently being improved (https://devguide.python.org/#status-of-python-branches) and have a longer possible life (https://endoflife.date/python) whitout being too new.
    `RUN apt-get -y install python3.8`

- The BASE_DIR is configured from the docker-compose to make the image creation more flexible.
    `ARG BASE_DIR`

-  The directory of the project it's defined as the default directory of vagrant; from the source (/) so;
        `(ENV BASE_DIR=/hproperty)`
    - Even if the Operating System changes the structure of the project is kept.
    - Also is not directed to home(~) to make paths shorter and not dependant on a particular user

## Using the image / docker-compose

- The code is shared, not copied, to the container to:
    - speed the build of the image for development(now the code is small and is not a problem look at assumptions)
    - Being able to use the IDE of your choice in the host Operating System.

## Choosed names
- hproperty is choosed as a project name to slighly protect the anonymity of the project and that it's not easily copied.

## Documentation
- The style is chosen from pep 257 https://www.python.org/dev/peps/pep-0257#multi-line-docstrings

## Formating / Style
- flake8 is used to make sure pep8 is being respected

### Deployment in aws
* The deploy of the nginx inside an AWS machine makes me investigate and learn a lot more about nginx. The template that I always follow had a server block that was just to serve static content althought it worked different in other projects.

## Debug

### Debug commands of the manage.py
You need to run Visual Studio Code with the remote extension (https://code.visualstudio.com/docs/remote/remote-overview) in the ldloans_rest-service container, in the /ldloans directory. Make sure you have put your breakpoints (https://code.visualstudio.com/docs/editor/debugging). Then run inside the container the command:

    `$ python -m debugpy --wait-for-client --listen 0.0.0.0:5678 ./manage.py`
And start the debugger from the menu that Visual Studio Code provides.

### Debug a single test
Is basically the same as " Debug commands of the manage.py" with the remote visual studio code but run the individual test

    `$ python -m debugpy --wait-for-client --listen 0.0.0.0:5678  project/tests/test_user_model.py`
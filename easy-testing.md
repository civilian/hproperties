## Requirements

* `Postman` https://www.postman.com/downloads/
    — Install Postman for different operating system.
  
## Test in postman
* Click [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/20133860-18a61172-c285-4bf5-a479-27f30b2b8447?action=collection%2Ffork&collection-url=entityId%3D20133860-18a61172-c285-4bf5-a479-27f30b2b8447%26entityType%3Dcollection%26workspaceId%3Df735ffb6-febe-4ea6-8f6d-7e49d20691b1#?env%5Bhabi_rest%5D=W3sia2V5Ijoic2VydmVyIiwidmFsdWUiOiI0NC4yMDMuMTI3LjE5MiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0Iiwic2Vzc2lvblZhbHVlIjoiNDQuMjAzLjEyNy4xOTIiLCJzZXNzaW9uSW5kZXgiOjB9XQ==)
and get it to run in postman

### Api Rest running the tests
* If you connect to the server with the command, and the key provided in the mail, you can also review the 
tests. First go to the ldloans directory (`cd ~/hproperties`) and then you can run the tests with with:
  `sudo docker-compose run rest-service python -m pytest`
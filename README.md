Objective: Create a DynamoDB table and load data into it using Python
Prerequisites: 
Access to AWS Cloud9
Rudimentary Python knowledge 
Rudimentary JSON knowledge
An AWS account 

Disclaimer: I performed this project on my root account for the sake of completing the task. However, in a production environment, you will want to assign an IAM role with the appropriate permissions. 
Steps
Log into your AWS console 
Go to the Cloud9 service 
You will need to create the table, in this case we will use Python to create the table. I used the "createtable.py" in this repository and then ran the file in Cloud9
You will also need a separate python script and JSON file to load the data into the newly created table 
Please see the "load table" and "sneaker data" files for the code. 
Run the new python script in your Cloud9 environment. The data will be displayed in the terminal with the word "adding" next to it. 
That is it!

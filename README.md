# Social-Media-Hashtag-Trend-Analyzer-Application

## Project Overview
This project aims to analyze hashtags from text uploaded by users. It uses AWS DynamoDB to store the data and AWS Lambda for processing.

step1:first create the IAM USER with  for the boto3 session which connect the local to AWS

session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',     # Replace with your actual access key
    aws_secret_access_key='YOUR_SECRET_KEY', # Replace with your actual secret key
    region_name='YOUR_REGION'                 # Replace with your desired region
)


step2:Create the IAM roles with 
  -awslambda full access
  -awsdynamodb full access

step3: Create the table in Dynamodb with payload through code or by Create table option

step4: Create the lambda function type the code in AWS lambda code console 

step5: Create the two lambda function one for post the hashtags into the Dynamodb table and another one for fetching the top 3 trending hashtags

step6: Create streamlit app with two lambda function invoke  through  api endpoint or response function



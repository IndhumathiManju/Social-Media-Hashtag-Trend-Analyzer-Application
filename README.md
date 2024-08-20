# Social-Media-Hashtag-Trend-Analyzer-Application
first create the IAM USER with  for the boto3 session which connect the local to AWS

session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',     # Replace with your actual access key
    aws_secret_access_key='YOUR_SECRET_KEY', # Replace with your actual secret key
    region_name='YOUR_REGION'                 # Replace with your desired region
)


Create the IAM role with 
  -awslambda full access
  -awsdynamodb full access

create the table in Dynamodb with payload through code or by Create table option

create the lambda function type the code in AWS lambda code console 

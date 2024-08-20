import streamlit as st
import boto3
import json
import uuid
from datetime import datetime

# Initialize Boto3 client for Lambda
session = boto3.Session(region_name='eu-north-1')
lambda_client = boto3.client('lambda')

# Streamlit UI
st.title("Social Media Post and Trending Hashtags")

# Section for creating a new post
st.header("Create a Post")
post_text = st.text_area("Enter your post text:", "")
post_hashtags = st.text_input("Enter your hashtags (comma separated):", "")

post_id = str(uuid.uuid4())
timestamp = datetime.utcnow().isoformat()

if st.button("Submit Post"):
    # Prepare the payload for the PostFunction
    post_payload = {
        "PostID": post_id,
        "post_text": post_text,
        "post_hashtags": [tag.strip() for tag in post_hashtags.split(',')],
        "timestamp": timestamp
    }

    # Invoke the PostFunction Lambda
    response = lambda_client.invoke(
        FunctionName='social_post',
        InvocationType='RequestResponse',
        Payload=json.dumps(post_payload)
    )

    # Process the response
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))
    if response_payload['statusCode'] == 200:
        st.success("Post successfully stored!")
    else:
        st.error(f"Failed to store post: {response_payload['body']}")

# Section for displaying trending hashtags
st.header("Trending Hashtags")

if st.button("Show Trending Hashtags"):
    # Prepare the payload for the TrendingFunction
    trending_payload = []

    # Invoke the TrendingFunction Lambda
    response = lambda_client.invoke(
        FunctionName='hastaga',
        InvocationType='RequestResponse',
        Payload=json.dumps(trending_payload)
    )

    # Process the response
    response_payload = json.loads(response['Payload'].read().decode('utf-8'))

    if response_payload['statusCode'] == 200:
        # Convert JSON string to Python dict/list
        trending_hashtags = (response_payload['body'])

        st.write("Trending Hashtags:")
        if isinstance(trending_hashtags, list):
            for item in trending_hashtags:
                if isinstance(item, list) and len(item) == 2:
                    hashtag, count = item
                    st.write(f'#{hashtag} - Top 3 Hashtags')
                else:
                    st.write('Unexpected data format:', item)
        else:
            st.write('Unexpected response format:', trending_hashtags)
    else:
        st.error(f"Failed to fetch trending hashtags: {response_payload['body']}")



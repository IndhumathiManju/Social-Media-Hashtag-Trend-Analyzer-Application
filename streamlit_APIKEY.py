import streamlit as st
import requests
import json
import uuid
import datetime

# Replace with your actual Lambda function endpoints
post_lambda_endpoint = "YOUR_POST_LAMBDA_ENDPIONT"
trending_lambda_endpoint = "YOUR_TRENDING_LAMBDA_ENDPIONT"

def main():
    st.title("Social Media Post Creator")

    # Input fields for post text and hashtags
    post_text = st.text_area("Compose your post", placeholder="Write something...")
    post_hashtags = st.text_input("Add hashtags (comma-separated)", placeholder="#example")

    # Button to submit the post
    if st.button("Post"):
        if post_text:
            # Generate a unique PostID using UUID
            post_id = str(uuid.uuid4())

            # Get the current timestamp in UTC
            timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

            # Prepare the data payload
            post_data = {
                'PostID': post_id,
                'post_text': post_text,
                'post_hashtags': [tag.strip() for tag in post_hashtags.split(',')],
                'timestamp': timestamp
            }

            # Send the data to the Lambda function
            response = requests.post(post_lambda_endpoint, json=post_data)
            
            if response.status_code == 200:
                st.success("Your post was successfully stored!")
            else:
                st.error(f"Error storing post: {response.text}")
        else:
            st.error("Post text cannot be empty")

    st.header("Trending Hashtags")
    
    # Button to fetch and display trending hashtags
    if st.button("Show Trending Hashtags"):
        response = requests.get(trending_lambda_endpoint)
        
        if response.status_code == 200:
            trending_hashtags = response.json()
            if trending_hashtags:
                st.write("Trending Hashtags:")
                for hashtag, count in trending_hashtags:
                    st.write(f"{hashtag}: {count} times")
            else:
                st.write("No trending hashtags available.")
        else:
            st.error(f"Error fetching trending hashtags: {response.text}")

if __name__ == "__main__":
    main()

import streamlit as st
from dotenv import load_dotenv
import os
import re
from src.retrieval_generation import generation
from src.ingest import ingestdata

# Load environment variables
load_dotenv()

# Ingest data and create the retrieval-augmented generation chain
# vstore = ingestdata("done")
# chain = generation(vstore)
if "chain" not in st.session_state:
    st.session_state.vstore = ingestdata("done")  # Store vstore in session state
    st.session_state.chain = generation(st.session_state.vstore)  # Store the chain in session state
# Streamlit UI
st.title("Course Recommendation System")

# User input text box
user_input = st.text_input("Enter your query:")

# Submit button
if st.button("Submit"):
    if user_input:
        result = st.session_state.chain.invoke(user_input)
        # Regex to extract course details
        pattern = r"Course:\s*(.*?)\s*Price:\s*(\$\d+)\s*URL:\s*(https?://\S+)"

        # Extract matches
        matches = re.findall(pattern, result)

        # Convert to structured format
        courses = [{"name": name, "price": price, "url": url} for name, price, url in matches]
        l1="https://www.genaicourses.com/blog/post/what-are-the-basic-building-blocks-of-ai-algorithms/opengraph-image.png?b01b4d4524590d02"
        l2="https://preview.redd.it/lithium-continuing-my-chatgpt-equation-to-bing-dalle-v0-kii5h6jndkpa1.jpg?width=1024&format=pjpg&auto=webp&s=67c1051b79d7892846cb6f2264270e15562a52e3"
        l3="https://img.freepik.com/premium-photo/hi-tech-digital-square-blocks-generate-ai_98402-102455.jpg"
        l=[l1,l2,l3]
        # Creating three columns
        col1, col2, col3 = st.columns(3)

        # Display each course in a separate column
        for col, course,img in zip([col1, col2, col3], courses,l):
            with col:
                st.image(img, use_container_width=True)
                st.subheader(course["name"])
                st.write(f"**Price:** {course['price']}")
                st.link_button("Go to Course", course["url"])
    else:
        st.warning("Please enter a query to get recommendations.")
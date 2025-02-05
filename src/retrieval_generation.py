import logging
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI  # ✅ Corrected Import
import os
from src.ingest import ingestdata

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("generation.log"), logging.StreamHandler()]
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def generation(vstore):
    try:
        logging.info("Starting generation process.")
        
        retriever = vstore.as_retriever(search_kwargs={"k": 3})
        logging.info("Retriever created successfully.")
        
        PRODUCT_BOT_TEMPLATE = """
        You are an expert course recommendation system that helps users find the perfect educational content.
        Analyze the course descriptions and skills to match the user's requirements.

        For each recommended course, you must provide:
        1. Course Name
        2. Course Price
        3. Course URL

        CONTEXT:
        {context}

        USER QUERY: {question}

        RECOMMENDATIONS:
        Please format each recommendation as follows:
        
        Course: [Course Name]
        Price: [Course Price]
        URL: [Course URL]
        """

        prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
        logging.info("Prompt template created successfully.")

        # ✅ Use LangChain's Gemini
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
        logging.info("Gemini LLM initialized successfully.")
        
        # ✅ Ensure context is correctly passed
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        logging.info("Chain created successfully.")
        
        return chain
    except Exception as e:
        logging.error("An error occurred during the generation process: %s", e, exc_info=True)
        raise

# if __name__ == '__main__':
#     try:
#         logging.info("Starting main execution.")
        
#         # Load VectorStore
#         vstore = ingestdata("done")
#         logging.info("VectorStore loaded successfully.")
        
#         # Generate recommendations
#         chain = generation(vstore)
#         logging.info("Chain invoked successfully.")
        
#         # Query for recommendations
#         query = "I need a course on web development with JavaScript and React"
#         logging.info(f"Performing recommendation query: {query}")
        
#         result = chain.invoke(query)
#         logging.info("Received result from chain.")
        
#         # Print the result
#         logging.info(f"Recommendation result: {result}")
#         print(result)
#     except Exception as e:
#         logging.error("An error occurred in the main execution: %s", e, exc_info=True)

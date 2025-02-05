import pandas as pd
import logging
from langchain_core.documents import Document

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("dataconverter.log"), logging.StreamHandler()]
)

def dataconveter():
    try:
        logging.info("Starting data conversion process.")
        
        # Load the data
        product_data = pd.read_csv("data\Coursera.csv")
        logging.info("Data loaded successfully from 'data\\Coursera.csv'.")
        
        # Select relevant columns
        columns = ['Course Name', 'Course URL', 'Course Description', 'Skills', 'Course Price']
        data = product_data[columns]
        logging.info("Selected relevant columns: %s", columns)
        
        # Add 'Tag' column
        data.loc[:, 'Tag'] = data['Course Description'] + data['Skills']
        logging.info("'Tag' column created by combining 'Course Description' and 'Skills'.")
        
        # Convert data to product_list
        product_list = []
        for index, row in data.iterrows():
            obj = {
                'course_name': row['Course Name'],
                'course_url': row['Course URL'],
                'course_price': row['Course Price'],
                'course_review': row['Tag']
            }
            product_list.append(obj)
        logging.info("Product list created with %d entries.", len(product_list))
        
        # Convert to Document objects
        docs = []
        for entry in product_list:
            metadata = {
                'course_name': entry['course_name'],
                'course_url': entry['course_url'],
                'course_price': entry['course_price']
            }
            doc = Document(page_content=entry['course_review'], metadata=metadata)
            docs.append(doc)
        logging.info("Document objects created successfully with %d entries.", len(docs))
        
        logging.info("Data conversion process completed successfully.")
        return docs

    except Exception as e:
        logging.error("An error occurred during the data conversion process: %s", e, exc_info=True)
        raise

# AI-Powered Course Recommendation System 🎓

An intelligent course recommendation system that leverages the power of Vector Embeddings, AstraDB, and Gemini Pro to provide personalized course suggestions based on user queries.

## 🌟 Demo

Here's how our system works in action:

### Blockchain Course Recommendations
![Screenshot 2025-02-05 230209](https://github.com/user-attachments/assets/96e7ef8b-52fd-427b-b4f5-94b1f166fb3d)
)
*Example of blockchain-related course recommendations*

### Machine Learning Course Recommendations
![Screenshot 2025-02-05 230103](https://github.com/user-attachments/assets/8118c76d-84f3-4e57-a7d1-f9a744e22d16)

*Example of machine learning course recommendations*

## 🏗️ Architecture
![Screenshot 2025-02-05 231054](https://github.com/user-attachments/assets/3fd34fe7-4270-4f97-9d27-d64799bb1a6f)


The system is built with a modern tech stack and follows a microservices architecture:
1. **Data Processing Layer**: Converts raw course data into embeddings
2. **Vector Store**: AstraDB for efficient similarity search
3. **LLM Integration**: Gemini Pro for natural language understanding
4. **User Interface**: Streamlit for an intuitive user experience

## 🚀 Features

- Natural language course search
- Real-time recommendations
- Price-aware suggestions
- Interactive user interface
- Visual course previews
- Direct course access links

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Vector Database**: AstraDB
- **LLM**: Google Gemini Pro
- **Embeddings**: HuggingFace (sentence-transformers/all-mpnet-base-v2)
- **Data Processing**: Pandas, LangChain

## 📋 Prerequisites

- Python 3.8+
- AstraDB Account
- Google AI Platform Account
- Required Python packages (see requirements.txt)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-powered-recommendation-system.git
cd ai-powered-recommendation-system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials:
# ASTRA_DB_API_ENDPOINT=your-endpoint
# ASTRA_DB_APPLICATION_TOKEN=your-token
# GOOGLE_API_KEY=your-google-api-key
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run app1.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your course query in the search box and click "Submit"

## 📁 Project Structure

```
.
├── src/
│   ├── data_converter.py   # Data processing and conversion
│   ├── ingest.py          # Vector store operations
│   └── retrieval_generation.py  # LLM integration
├── app1.py                # Streamlit application
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- LangChain for the awesome framework
- Anthropic for LLM capabilities
- AstraDB for vector storage
- Google for Gemini Pro API

## 📧 Contact

Your Name - amar_c@me.iitr.ac.in
Project Link: [https://github.com/yourusername/ai-powered-recommendation-system](https://github.com/yourusername/ai-powered-recommendation-system)

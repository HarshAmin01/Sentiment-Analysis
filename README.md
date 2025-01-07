# Sentiment Analysis Feedback/Reviews Analyzer

This project is a Python-based tool that analyzes the sentiment of customer feedback, reviews, or any text input. It uses a pre-trained natural language processing (NLP) model from Hugging Face's transformers library. The tool classifies text as positive or negative and provides a confidence score, making it ideal for businesses to gain insights from user feedback or reviews.

## Key Features:
- Batch Sentiment Analysis: Analyze multiple feedback entries or reviews in one go.
- Interactive Mode: Enter feedback interactively in the terminal for on-the-fly analysis.
- Model Reusability: Save and load pre-trained models and tokenizers to avoid redundant downloads.
- Customizable: Easily adapt to other NLP models or languages with Hugging Face.

## Example Use Cases
- Product Reviews: Analyze customer sentiments from product reviews to identify trends.
- Service Feedback: Gauge satisfaction from service-related feedback.
- Social Media Monitoring: Understand user sentiments in social media comments or tweets.

## Installation
### 1. Clone the Repository
### 2. Set Up a Virtual Environment (Optional but Recommended)
### 3. Install Dependencies
### 4. Install PyTorch (if not already installed)

#### For CPU-only systems:
- pip install torch torchvision torchaudio
- For detailed PyTorch installation (with GPU support), visit PyTorch's Get Started.

## Usage
 1. Run the Script
    - python main.py
 2. Analyze Default Examples
The script begins by analyzing a few predefined feedback examples:
Checking default examples
  i. Text: The customer service was excellent.
  - Sentiment: POSITIVE (Confidence: 0.9998)

ii. Text: I had a terrible experience with the product.
- Sentiment: NEGATIVE (Confidence: 0.9981)

3. Interactive Mode
You can enter feedback interactively for analysis:

i. Enter a sentence for sentiment analysis (or type 'exit' to quit): I love the new features!
- Sentiment: POSITIVE (Confidence: 0.9995)

ii. Enter a sentence for sentiment analysis (or type 'exit' to quit): The app crashes constantly.
- Sentiment: NEGATIVE (Confidence: 0.9974)

Type exit, quit, or thanks to leave the interactive mode.

## Project Structure

sentiment-analysis-feedback/
├── main.py               # Main script for running sentiment analysis
├── utils.py              # Utility functions (e.g., saving/loading models)
├── models/               # Directory for saved models and tokenizers
├── data/                 # Directory for sample input data (optional)
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation

## How It Works
- Pre-trained Model: The project uses Hugging Face's pre-trained model distilbert-base-uncased-finetuned-sst-2-english for sentiment analysis.
- Batch Processing: Analyze multiple feedback entries simultaneously to save time.
- Interactive Input: Analyze single feedback entries interactively, ideal for real-time use cases.

## Customization
- Use a Different Pre-trained Model
- You can replace the default model (distilbert-base-uncased-finetuned-sst-2-english) with another Hugging Face model. Update the model_name in main.py:


## Dependencies
The following Python libraries are required:

- transformers: For loading pre-trained models.
- torch: For running the PyTorch backend.
- Install them via:
   -  pip install transformers torch

## Example Output
Sample output from the tool:

- Checking default examples
i. Text: The customer service was excellent.
- Sentiment: POSITIVE (Confidence: 0.9998)

ii. Enter a sentence for sentiment analysis (or type 'exit' to quit): The app is too slow to load.
- Sentiment: NEGATIVE (Confidence: 0.9942)

## Known Issues
- Performance: The script may be slower on large datasets without GPU support.
- Model Selection: Ensure PyTorch is installed correctly to avoid compatibility issues.

## Contribution
Contributions are welcome! 

#### To contribute:

- Fork the repository.
- Create a feature branch: git checkout -b feature-name.
- Commit changes: git commit -m "Add feature-name".
- Push to the branch: git push origin feature-name.
- Open a pull request.

- Here is the code and it's output screenshot
  ![Screenshot 2025-01-07 101438](https://github.com/user-attachments/assets/1274a057-ca0c-4b88-beb5-11c90409cc29)


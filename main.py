from transformers import pipeline
from utils import save_model_and_tokenizer, analyze_texts
import os


def main():
    # Load the pre-trained sentiment analysis model
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    analyzer = pipeline("sentiment-analysis", model=model_name)

    # Define paths for saving the model and tokenizer
    model_save_path = "./models/sentiment_model"
    tokenizer_save_path = "./models/sentiment_tokenizer"

    # Save model and tokenizer
    save_model_and_tokenizer(analyzer, model_save_path, tokenizer_save_path)

    # Default examples
    print("\nChecking default examples")
    texts = [
        "The customer service was excellent.",
        "I had a terrible experience with the product.",
        "The restaurant is over there.",
    ]
    analyze_texts(analyzer, texts)

    # User input loop
    while True:
        user_text = input("\nEnter a sentence for sentiment analysis (or type 'exit' to quit): ")
        if user_text.lower() in ['exit', 'quit', 'thanks']:
            print("Thank you for visiting! Have a great day!")
            break
        if not user_text.strip():
            print("Please enter a valid sentence.")
            continue
        try:
            result = analyzer(user_text)
            print(f"Sentiment: {result[0]['label']} (Confidence: {result[0]['score']:.4f})")
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")


if __name__ == "__main__":
    main()

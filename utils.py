import os

def save_model_and_tokenizer(analyzer, model_path, tokenizer_path):
    """Save the model and tokenizer if not already saved."""
    if not os.path.exists(model_path):
        print("Saving the model and tokenizer...")
        os.makedirs(model_path, exist_ok=True)  # Create the models directory if it doesn't exist
        analyzer.model.save_pretrained(model_path)
        analyzer.tokenizer.save_pretrained(tokenizer_path)
        print("Model and tokenizer saved successfully!")
    else:
        print("Model and tokenizer already exist.")

def analyze_texts(analyzer, texts):
    """Analyze and display sentiments for a batch of texts."""
    results = analyzer(texts)
    for text, sentiment in zip(texts, results):
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment['label']} (Confidence: {sentiment['score']:.4f})\n")

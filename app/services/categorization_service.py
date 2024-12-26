import torch
import pickle
from app.services.database_service import get_uncategorized_articles, save_categorized_articles
from app.services.model_loader import load_model_and_tokenizer
from sklearn.preprocessing import LabelEncoder


def load_label_encoder():
    with open('./models/news_classifier_bert/label_classes.pkl', 'rb') as f:
        classes = pickle.load(f)

    # Initialize and fit the LabelEncoder
    label_encoder = LabelEncoder()
    label_encoder.classes_ = classes
    return label_encoder


def categorize_articles():
    # Load the model, tokenizer, and label encoder
    model, tokenizer = load_model_and_tokenizer()
    label_encoder = load_label_encoder()

    # Fetch uncategorized articles from the database
    uncategorized_articles = get_uncategorized_articles()
    categorized_articles = []

    for article in uncategorized_articles:
        # Skip articles with missing content
        if not article.get('content'):
            print(f"Skipping article with missing content: {article.get('id')}")
            continue

        try:
            # Tokenize the article content
            inputs = tokenizer(article['content'], truncation=True, padding=True, max_length=512, return_tensors="pt")
            outputs = model(**inputs)

            # Predict category
            predictions = torch.argmax(outputs.logits, dim=1).item()
            category = label_encoder.inverse_transform([predictions])[0]  # Decode the prediction

            # Assign the predicted category to the article
            article['category'] = category
            article['isCategorized'] = True
            categorized_articles.append(article)

        except Exception as e:
            print(f"Error processing article {article.get('id')}: {e}")
            continue

    # Save categorized articles back to the database
    save_categorized_articles(categorized_articles)

    # Return the count of successfully categorized articles
    return {
        'categorized_count': len(categorized_articles),
        'skipped_count': len(uncategorized_articles) - len(categorized_articles)
    }

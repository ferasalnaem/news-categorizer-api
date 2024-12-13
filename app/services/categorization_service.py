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
    model, tokenizer = load_model_and_tokenizer()
    label_encoder = load_label_encoder()

    uncategorized_articles = get_uncategorized_articles()

    categorized_articles = []

    for article in uncategorized_articles:
        if not article.get('content'):
            continue

        # Tokenize the article content
        inputs = tokenizer(article['content'], truncation=True, padding =True, return_tensors="pt")
        outputs = model(**inputs)

        # Predict category
        predictions = torch.argmax(outputs.logits, dim=1).item()
        category = label_encoder.inverse_transform([predictions])[0]  # Decode the prediction

        article['category'] = category
        article['isCategorised'] = True
        categorized_articles.append(article)

    save_categorized_articles(categorized_articles)
    return len(categorized_articles)
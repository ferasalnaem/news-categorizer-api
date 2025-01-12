# API Documentation

A RESTful API for categorizing news articles.

  Post &lt;baseUrl>/catgorize

# 🚀 How to Run the Project

## Prerequisites:


Copy the generated news_classfier_bert after training the model in https://github.com/ferasalnaem/news-categorizer-training to models directory as shown in the following project structure:

## ⚙️ Project Structure

```plaintext
news-categorizer-api/
├── app/
│   ├── routes/
│   │      ├── __init__.py/
│   │      └── categorize.py/
│   ├── services/
│   │      ├── categorization_service.py/
│   │      ├── database_service.py/
│   │      └── model_loader.py/
│   ├── __init__.py
│   ├── config.py
│   └── models.py
├── models/news_classfier_bert/
│   ├── config.json
│   ├── label_classes.pkl
│   └── model.safetensors
│   └── special_tokens_map.json
│   └── tokenizer_config.json
│   └── vocab.txt
├── venv/
├── app.py
└── requirements.txt

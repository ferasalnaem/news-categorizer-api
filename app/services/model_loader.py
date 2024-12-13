from transformers import BertTokenizer, BertForSequenceClassification
from app.config import Config


def load_model_and_tokenizer():
    tokenizer = BertTokenizer.from_pretrained(Config.MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(Config.MODEL_PATH)
    return model, tokenizer
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/newsAggregator")
    MODEL_PATH = os.getenv("MODEL_PATH", "./models/news_classifier_bert")
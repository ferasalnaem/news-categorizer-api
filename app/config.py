import os

class Config:
    # For local DB
    # MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/newsAggregator")
    # For Dockerized DB
    #MONGO_URI = os.getenv("MONGO_URI", "mongodb://fzaher:dev@mongo:27017/newsAggregator?authSource=admin")
    # For EC2 DB
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://fzaher:dev@3.73.84.1:27017/newsAggregator?authSource=admin")
    MODEL_PATH = os.getenv("MODEL_PATH", "./models/news_classifier_bert")
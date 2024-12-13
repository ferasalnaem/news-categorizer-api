from app import mongo_client
from app.models import Collections


def get_uncategorized_articles():
    dp = mongo_client.get_database()
    return list(dp[Collections.UNCATEGORIZED].find({"isCategorised": False}))


def save_categorized_articles(articles):
    db = mongo_client.get_database()
    categorized = db[Collections.CATEGORIZED]
    uncategorized = db[Collections.UNCATEGORIZED]

    # Insert categorized articles into categorized collection
    categorized.insert_many(articles)

    # Update uncategorized articles to mark them as categorized
    for article in articles:
        uncategorized.update_one({"_id": article['_id']}, {"$set": {"isCategorized": True}})
from flask import Blueprint, jsonify
from app.services.categorization_service import categorize_articles

categorize_bp = Blueprint('categorize', __name__)

@categorize_bp.route("", methods=["POST"])
def categorize():
    categorized_count = categorize_articles()
    return jsonify({"message": "Articles categorized", "count": categorized_count})

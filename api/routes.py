from flask import Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route("/")
def index(): 
    return "<h1> API WEB </h1>"
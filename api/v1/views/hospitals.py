#!/usr/bin/python3
"""This API Handles Registration of User."""
from api.v1.views import app_views
from flask_jwt_extended import create_access_token, set_access_cookies
from flask import request, jsonify, session
from flasgger.utils import swag_from
from models.hospital import Hospital
from models import storage
from sqlalchemy.exc import IntegrityError



@app_views.route("/auth/hospital/register", methods=["POST"])
def register():
    """Handle view for registration of user"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Bad Request"}), 400

    required_fields = [
        "name", "email","role",
        "password", "phone_number"
    ]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} Field Missing"}), 400
    try:
        hospital = Hospital(**data)
        storage.new(hospital)
        storage.save()
        return jsonify({"message": "Registration Successfully"}), 200
    except IntegrityError:
        return jsonify({"error": "User Exists Already"}), 409
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Internal Error Occured"}), 500
    finally:
        storage.close()

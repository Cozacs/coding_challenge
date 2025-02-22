from flask import Blueprint, request, jsonify
from app import db
from app.models import Person

main = Blueprint("main", __name__)

@main.route("/person-info", methods=["POST"])
def add_person():
    data = request.get_json()

    if not data.get("name") or not data.get("current_role"):
        return jsonify({"error": "Name and Current_role are necessary"}), 400

    new_person = Person(
        name=data["name"],
        current_role=data["current_role"],
        company=data.get("company"),
        location=data.get("location"),
        linkedin_url=data.get("linkedin_url"),
    )

    db.session.add(new_person)
    db.session.commit()

    return jsonify({"message": "Person add to Database!"}), 201


@main.route("/person-info", methods=["GET"])
def get_person():
    name = request.args.get("name")
    company = request.args.get("company")

    if not name:
        return jsonify({"error": "Name are necessary for research"}), 400

    query = Person.query.filter_by(name=name)

    if company:
        query = query.filter_by(company=company)

    person = query.first()

    if not person:
        return jsonify({"error": "Person not found"}), 404

    return jsonify({
        "name": person.name,
        "current_role": person.current_role,
        "company": person.company,
        "location": person.location,
        "linkedin_url": person.linkedin_url
    })

from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    current_role = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100))
    location = db.Column(db.String(100))
    linkedin_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Person {self.name} - {self.current_role}>"

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    full_name = db.Column(db.String(100))
    role = db.Column(db.String(20)) # 'Student' or 'Professor'
    
    # Student Profile Fields
    qualification = db.Column(db.String(100))
    college = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    resume_file = db.Column(db.String(100)) # Stores filename like 'resume_1.pdf'

# In models.py
class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    domain = db.Column(db.String(100))
    description = db.Column(db.String(500))
    type = db.Column(db.String(50)) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # --- ADD THIS NEW LINE ---
    pdf_link = db.Column(db.String(500))
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))
    status = db.Column(db.String(20), default="Pending")
    
    # Relationships to access data easily
    student = db.relationship('User', backref='applications')
    internship = db.relationship('Internship', backref='applications')
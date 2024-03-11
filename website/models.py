from . import db
from flask_login import UserMixin


# User model for both students and faculty members

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_student = db.Column(db.Boolean, nullable=False)
    is_faculty_member = db.Column(db.Boolean, nullable=False)


# Student model inheriting from User
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academic_program = db.Column(db.String(100), nullable=False)
    areas_of_expertise = db.Column(db.String(255))
    availability = db.Column(db.String(100), nullable=True)
    experience = db.Column(db.String(100), nullable=True)


# Faculty member model inheriting from User
class FacultyMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship('Department', backref=db.backref('faculty_members', lazy=True))


# Department model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


# Job listing model
class JobListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    responsibilities = db.Column(db.Text, nullable=False)
    qualifications = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text)
    hours = db.Column(db.Integer(), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship('Department', backref=db.backref('job_listings', lazy=True))


# Application model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('applications', lazy=True))
    job_listing_id = db.Column(db.Integer, db.ForeignKey('job_listing.id'), nullable=False)
    job_listing = db.relationship('JobListing', backref=db.backref('applications', lazy=True))
    resume = db.Column(db.String(255))
    cover_letter = db.Column(db.Text)
    transcripts = db.Column(db.String(255))
    letters_of_recommendation = db.Column(db.String(255))


# Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('appointments', lazy=True))
    faculty_member_id = db.Column(db.Integer, db.ForeignKey('faculty_member.id'), nullable=False)
    faculty_member = db.relationship('FacultyMember', backref=db.backref('appointments', lazy=True))
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)


# Document model for document management
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    application = db.relationship('Application', backref=db.backref('documents', lazy=True))
    document_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(255))


# Feedback model for feedback mechanism
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_type = db.Column(db.String(10), nullable=False)  # Student or FacultyMember
    feedback_text = db.Column(db.Text, nullable=False)


class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('tutor', uselist=False), lazy=True)
    hourly_rate = db.Column(db.Float, nullable=False, default=100.0)

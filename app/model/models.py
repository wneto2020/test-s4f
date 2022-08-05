from app import db


class RentalCompanie(db.Model):

    companie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fantasy_name = db.Column(db.String(100), nullable=False)
    corporate_name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(13), nullable=False)
    zip = db.Column(db.String(9), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)


class AutoMaker(db.Model):

    automaker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Model(db.Model):

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    automaker = db.Column(db.String(255), nullable=False, unique=True)


class Vehicle(db.Model):

    vehicle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ports_number = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(255), nullable=False)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_year = db.Column(db.Integer, nullable=False)
    manufacturer_year = db.Column(db.Integer, nullable=False)
    board = db.Column(db.String(8), nullable=False, unique=True)
    chassi = db.Column(db.String(17), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)


class Log(db.Model):

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    finish_at = db.Column(db.DateTime, nullable=False)

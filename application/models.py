from application import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime as dt
import shortuuid as su

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)







class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    emailAddress = db.Column(db.String(100), index = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    licenseID = db.Column(db.Integer, db.ForeignKey('licenses.id'), nullable = False)
    sessions = db.relationship('Sessions', backref = db.backref("sessionOwner"), uselist = True)

    def __init__(self, username, password, emailAddress):
        self.username = username
        self.password = generate_password_hash(password)
        self.emailAddress = emailAddress
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def check_licenseID(self, licenseKey):
        targetLicense = Licenses.query.filter_by(code = licenseKey)
        if targetLicense is None or targetLicense.status == 'CLAIMED':
            return False
        else:
            targetLicense.status = 'CLAIMED'
            self.licenseID = targetLicense.id
            db.session.commit()
            return True
    



class Licenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20), nullable = False, unique = True)
    status = db.Column(db.String(7), nullable = False) # CLAIMED OR VALID
    user = db.relationship('Users', backref = db.backref('licenseCode'), uselist = False, nullable = True)
    creation_date = db.Column(db.DateTime, nullable = False)
    claimDate = db.Column(db.DateTime, nullable = True)

    def __init__(self, code):
        self.code = code
        self.creationDate = dt.datetime.now()
    
    def generateLicenseCode():
        newLicense = su.ShortUUID().random(9)
        if Licenses.query.filter_by(code = newLicense).first() is not None:
            newLicense = generateLicenseCode()
        return newLicense



class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(100), index = True, nullable = False)
    description = db.Column(db.Text, nullable = True)
    creationDate = db.Column(db.DateTime, index = True, nullable = False)

    def __init__(self, owner, name, description):
        self.name = name
        self.owner = owner
        self.description = description
        self.creationDate = dt.datetime.now()


class Coordsets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sessionID = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    obj1_x_pos = db.Column(db.Integer)
    obj1_y_pos = db.Column(db.Integer)
    obj1_width = db.Column(db.Integer)
    obj1_height = db.Column(db.Integer)
    obj1_color = db.Column(db.Integer)
    obj2_x_pos = db.Column(db.Integer)
    obj2_y_pos = db.Column(db.Integer)
    obj2_width = db.Column(db.Integer)
    obj2_height = db.Column(db.Integer)
    obj2_color = db.Column(db.Integer)
    obj1_color_B = db.Column(db.Integer)
    obj2_color_B = db.Column(db.Integer)
    obj1_color_C = db.Column(db.Integer)
    obj2_color_C = db.Column(db.Integer)

    def __init__(self, obj1_x_pos, obj1_y_pos, obj1_width, obj1_height, obj1_color, obj2_x_pos, obj2_y_pos, obj2_width, obj2_height, obj2_color, obj1_color_B, obj2_color_B, obj1_color_C, obj2_color_C):
        self.obj1_x_pos = obj1_x_pos
        self.obj1_y_pos = obj1_y_pos
        self.obj1_width = obj1_width
        self.obj1_height = obj1_height
        self.obj1_color = obj1_color
        self.obj2_x_pos = obj2_x_pos
        self.obj2_y_pos = obj2_y_pos
        self.obj2_width = obj2_width
        self.obj2_height = obj2_height
        self.obj2_color = obj2_color
        self.obj1_color_B = obj1_color_B
        self.obj2_color_B = obj2_color_B
        self.obj1_color_C = obj1_color_C
        self.obj2_color_C = obj2_color_C

import bcrypt
from app.const_vars import PEPPER
from app.database.models import Users
from app import db

class Security:
    
    @classmethod
    def hash_password(cls, password: str):
        """Secures the password

        Args:
            password (str): Given password from the user

        Returns:
            str: Hashed password
            str: salt
        """
        salt = bcrypt.gensalt()
        password += PEPPER
        return bcrypt.hashpw(password.encode('utf-8'), salt), salt
    
    @classmethod
    def check_password(cls, email: str, password: str) -> bool:
        """Check if given password is valid with hashed from db

        Args:
            login (int): Users login
            password (str): Password given by user

        Returns:
            bool: True if passwords mach, False if not
        """
        with db.session as session:
            user = session.query(Users).filter(Users.email == email).first()
        password += PEPPER
        new_hashed_password = bcrypt.hashpw(password.encode('utf-8'), user.salt)
        return new_hashed_password == user.password

      
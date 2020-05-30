import os


class Config:
    DB_CONNECTION = os.getenv('DB_CONNECTION', 'db.sqlite')
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret').encode()
    UPLOAD_FOLDER = os.path.join(
        os.getcwd(),
        os.getenv('UPLOAD_FOLDER', 'upload')
    )

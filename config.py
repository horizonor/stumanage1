import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config,
    'MYSQL_PASSWORD': 'xb#mysql#1112',
    'DATABASE_NAME': 'studenttrainPlan'
}

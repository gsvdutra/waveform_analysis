from email.mime import application
from application.main import Main

if __name__ == '__main__':
    application = Main('resources/example_data.csv')
    application.run_app()
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:aljozu99@localhost:5432/proyectodbp"

#QLALCHEMY_DATABASE_URI = "postgresql://sec01group01:utec2021@204.2.195.90:30794/CS2901sec01"
TESTING = True
SECRET_KEY = "FDsarfewaifhq34985ty3hfg043y2th43wef"
USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
USER_ENABLE_EMAIL = True        # Enable email authentication
USER_ENABLE_USERNAME = False    # Disable username authentication
USER_EMAIL_SENDER_NAME = USER_APP_NAME
USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
RBAC_USE_WHITE = True
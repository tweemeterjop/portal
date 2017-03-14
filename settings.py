import os

# Run the portal in debug mode?
DEBUG = True

# Database connection URI, PostgreSQL or MySQL is suggested.
# Examples, see documentation for more:
# postgresql://foo:bar@localhost:5432/portal
# mysql://foo:bar@localhost/portal
SQLALCHEMY_DATABASE_URI = "postgresql://cuckoo:cuckoo@localhost/portal"

# If set to True, Flask-SQLAlchemy will track modifications of objects and emit
# signals.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key used by Flask to generate sessions etc. (This feature is not
# actually used at the moment as we have no user accounts etc).
SECRET_KEY = os.urandom(32)

# IP address of the Cuckoo API.
CUCKOO_API = "http://127.0.0.1:8090"

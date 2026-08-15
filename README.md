# kinetic-plex-api

Libraries

pip install Flask
pip install Flask-SQLAlchemy
pip install pymysql
pip install Flask-Migrate
pip install python-dotenv

Configure .env

DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_NAME=kinetic_plex_db

Migrations

flask --app run.py db init
flask --app run.py db migrate -m "<migration-name>"
flask --app run.py db upgrade
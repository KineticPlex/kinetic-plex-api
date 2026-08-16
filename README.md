# KineticPlex API

## Project Description
The **KineticPlex API** is the core backend service for the KineticPlex 3D Sign Language Translation platform. Built with Python and Flask, it acts as the bridge between natural language text and 3D avatar animations. 

Its primary responsibilities include:
* **Natural Language Processing (NLP):** Utilizes `spaCy` to analyze Spanish text, perform lemmatization, filter stop-words, and reorder sentences into a proper Sign Language grammatical structure (Gloss).
* **Sequence Management:** Maps processed words to specific 3D animation keys stored in a MySQL database.
* **Client Integration:** Serves structured JSON responses containing animation sequences and durations, ready to be consumed and rendered by the Godot Game Engine frontend.

##  Installation & Setup

```bash
# Web framework and ORM for database management
pip install Flask
pip install Flask-SQLAlchemy

# MySQL driver for Python
pip install pymysql

# Database migration handling
pip install Flask-Migrate

# Environment variable management
pip install python-dotenv

# Natural Language Processing library
pip install spacy

# Small model (Fastest, low memory footprint, good for development)
python -m spacy download es_core_news_sm

# Medium model (Better accuracy, includes word vectors)
python -m spacy download es_core_news_md

# Large model (Highest accuracy for production environments)
python -m spacy download es_core_news_lg
```

## Environment Variables

Create a `.env` file in the root directory of the project to configure your MySQL database connection. Replace the values with your local or server credentials:

```env
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=<your_database_host>
DB_NAME=<your_database_name>
```

## Database Migrations

We use `Flask-Migrate` (Alembic) to handle database schema changes. Whenever you create or modify a model in your code, you must run migrations to update the MySQL database.

**Initialize the migration environment:**
*(Run this only once when setting up the project for the first time)*
```bash
flask --app run.py db init
```
> **What it does:** Creates a `migrations/` folder in your project directory to track all database changes.

**Generate a new migration script:**
*(Run this every time you modify, add, or delete a table column in your models)*
```bash
flask --app run.py db migrate -m "<migration-name>"
```
> **What it does:** Compares your current SQLAlchemy models with the existing database schema and generates a Python script with the necessary SQL instructions to update it. Example: `-m "Added category_id to animations"`.

**Apply migrations to the database:**
*(Run this after creating a migration script to actually apply the changes)*
```bash
flask --app run.py db upgrade
```
> **What it does:** Executes the generated migration scripts, applying the physical changes (creating tables, altering columns) to your MySQL database.
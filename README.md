# KineticPlex API

## Project Description
The **KineticPlex API** is the core backend service for the KineticPlex 3D Sign Language Translation platform. Built with Python and Flask, it acts as the bridge between natural language text and 3D avatar animations. 

Its primary responsibilities include:
* **Natural Language Processing (NLP):** Utilizes `spaCy` to analyze Spanish text, perform lemmatization, filter stop-words, and reorder sentences into a proper Sign Language grammatical structure (Gloss).
* **Sequence Management:** Maps processed words to specific 3D animation keys stored in a MySQL database.
* **Client Integration:** Serves structured JSON responses containing animation sequences and durations, ready to be consumed and rendered by the Godot Game Engine frontend.

## Installation & Setup (Local)

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
FLASK_DEBUG=0

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

## Running with Docker

You can easily run the application in an isolated environment using Docker. Ensure your `.env` file is properly configured before starting the container, as it will be loaded at runtime.

**1. Build the Docker image:**
Run this command in the root of your project to create the image:
```bash
docker build -t kinetic-plex-api .
```

**2. Run the container (Standard):**
This command starts the application in the background (`-d`), names the container `kinetic-plex-api-container` for easier management, maps port 9001, and loads your environment variables:
```bash
docker run -d --name kinetic-plex-api-container -p 9001:9001 --env-file .env kinetic-plex-api
```

**2.1. Run the container in Development Mode (Live Reloading):**
If you are actively developing, mount your local directory as a volume so changes reflect instantly without rebuilding the image. (Ensure `FLASK_DEBUG=1` is active in your `.env`).

*   **For Ubuntu (Linux) and Windows PowerShell:**
    ```bash
    docker run -d --name kinetic-plex-api-container -p 9001:9001 -v "${PWD}:/app" --env-file .env kinetic-plex-api
    ```
*   **For Windows CMD (Command Prompt):**
    ```cmd
    docker run -d --name kinetic-plex-api-container -p 9001:9001 -v "%cd%:/app" --env-file .env kinetic-plex-api
    ```

**3. Stop the container:**
When you need to stop the application:
```bash
docker stop kinetic-plex-api-container
```

**4. Remove the container:**
To delete a stopped container so you can create a new one with the same name:
```bash
docker rm kinetic-plex-api-container
```

**5. View container logs (Troubleshooting):**
To check the output and trace errors if a container fails to start:
```bash
docker logs kinetic-plex-api-container
```

**6. View all containers:**
To see a list of all your running and stopped containers:
```bash
docker ps -a
```

**7. View available images:**
To see a list of all Docker images downloaded or built on your system:
```bash
docker images
```

**8. Access the container shell (Navigate inside):**
To open an interactive terminal inside your running container and navigate its directories:
```bash
docker exec -it kinetic-plex-api-container /bin/bash
```

> **Tip:** Once inside, you can use standard Linux commands like `ls` (to list files) and `cd` (to change directories). Type `exit` when you are done to leave the container's terminal.

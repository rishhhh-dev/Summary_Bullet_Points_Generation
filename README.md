# Summary_Bullet_Points_Generation
This repo creates a summary and bullet points based on the user's input as a message using Groq API. 

# Prerequisites
1. Python (>=3.x)
2. pip (Python Package Installer)
3. Virtualenv
4. Postman

# Clone Repo
> git clone https://github.com/rishhhh-dev/Summary_Bullet_Points_Generation.git

# Create a virtual environment and install dependencies
```
python -m venv env_name
source env_name/bin/activate

pip install -r requirements.txt
```

# Create a .env file and add variables
```
GROQ_API_KEY=your_api_key_here
POSTGRES_DATABASE_NAME=your_db_name_here
POSTGRES_DATABASE_USER=your_db_user_here
POSTGRES_DATABASE_PASSWORD=your_db_password_here
POSTGRES_DATABASE_HOST=your_db_host_here
POSTGRES_DATABASE_PORT=your_db_port_here
```
# Export the env variables
```
export GROQ_API_KEY=your_api_key_here
export POSTGRES_DATABASE_NAME=your_db_name_here
export POSTGRES_DATABASE_USER=your_db_user_here
export POSTGRES_DATABASE_PASSWORD=your_db_password_here
export POSTGRES_DATABASE_HOST=your_db_host_here
export POSTGRES_DATABASE_PORT=your_db_port_here
```

# Migrate database tables
```
python manage.py makemigrations
python manage.py migrate
```

# Start local server
```
python manage.py runserver
```

# Execute API endpoints via CURL or Postman
> To generate a JWT token
```
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

> To generate the summary
```
curl -X POST http://127.0.0.1:8000/generate-summary/ -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{"message": "Your input text here"}'
```

> To generate bullet points
```
curl -X POST http://127.0.0.1:8000/generate-bullet-points/ -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{"message": "Your input text here"}'
```

# Run test cases command
```
pytest
```

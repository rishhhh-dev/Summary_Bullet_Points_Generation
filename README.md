# Summary_Bullet_Points_Generation
This repo creates a summary and bullet points based on the user's input as a message using Groq API. 

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

# Run test cases command
> pytest

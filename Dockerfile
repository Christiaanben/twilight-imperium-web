FROM python:3.10

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

# Add all the files to docker under project folder
COPY ./src ./

# Run the server with gunicorn when the server starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
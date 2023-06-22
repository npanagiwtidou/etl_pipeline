# Deriving the python image
FROM python:3.8-buster

#Creating the working directory in Docker
WORKDIR /app

# Copy all the source code into our directory to the Docker image
COPY . /app

#install all the libraries we will need to execute the code
RUN pip install -r requirements.txt

# tell the Docker the command to run inside the container
CMD ["python","./main.py"]


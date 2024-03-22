# Use a lightweight Python image
FROM python:3.8.10

# Set the working directory inside the container
WORKDIR /app

# Install any necessary dependencies
# If your script has additional dependencies, you can include them in requirements.txt and uncomment the following lines
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the api.py script to the container
COPY api.py .
COPY grabme.mp4 .

# Expose port 3000 for incoming connections
EXPOSE 3000

# Run the api.py script when the container starts
CMD [ "python", "api.py" ]
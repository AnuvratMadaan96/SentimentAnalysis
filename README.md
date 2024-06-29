# SentimentAnalysis

# Sentiment Analysis Application

This project is a simple web application that uses AWS Comprehend to perform sentiment analysis on user-provided text. The application is built using Django, Django REST framework, and AWS Comprehend.

## Project Structure

* sentiment_analysis/
  * api/
    * init.py
    * admin.py 
    * apps.py
    * migrations/
      * init.py
    * models.py
    * tests.py
    * views.py
    * urls.py
  * sentiment_analysis/
    * init.py
    * asgi.py
    * settings.py
    * urls.py
    * views.py
    * wsgi.py
  * templates/
    * index.html
  * manage.py
  * db.sqlite3

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- AWS account with access to Comprehend
- Boto3

### Installation
1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/sentiment_analysis.git    
    cd sentiment_analysis
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install django djangorestframework boto3
    ```

4. **Set up AWS credentials:**

    Configure your AWS credentials by running:

    ```bash
    aws configure
    ```

    Or set your credentials in the environment variables:

    ```bash
    export AWS_ACCESS_KEY_ID='your_access_key_id'
    export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
    export AWS_DEFAULT_REGION='your_aws_region'
    ```

### Database Migration

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### Running the Server
Start the Django development server:
```bash
python manage.py runserver
```
The application will be accessible at 'http://127.0.0.1:8000/'.

### Run the Server on EC2 instance
```bash
python manage.py runserver 0.0.0.0:8000
```
The application will be available at '**Public IP address on the EC2 instance**'

## Project Features
### Frontend
The frontend is a simple HTML page (index.html) that includes a form for the user to input text and a button to submit the text for sentiment analysis.

### Backend
The backend is built using Django REST framework and includes an API endpoint that processes the text input from the frontend and sends it to AWS Comprehend for sentiment analysis.

#### API Endpoint: /api/sentiment/ (POST request)
#### AWS Comprehend Integration
The backend uses the AWS SDK for Python (Boto3) to interact with AWS Comprehend. The SentimentAnalysisView in api/views.py handles the sentiment analysis request.

### Troubleshooting
#### Common Issues
##### Forbidden: /api/sentiment/

This error is usually due to missing CSRF tokens in your POST requests. Ensure that your AJAX request includes the CSRF token as shown in the index.html file.

#### AWS Comprehend Permission Issues

Make sure that your AWS credentials are correctly configured and have the necessary permissions to use AWS Comprehend.

```markdown
This `README.md` file provides a comprehensive guide to setting up and running the Sentiment Analysis application, including the project structure, setup instructions, features, and troubleshooting tips. Adjust the repository URL and other specific details as needed for your project.
```


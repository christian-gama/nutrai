# Diet App README

This project contains a Django web application that helps users manage their diet plans. The application is designed for nutritionists, who can create diet plans for their patients, and patients, who can view and follow the diet plans created for them.

[API Documentation](https://documenter.getpostman.com/view/16405037/2s93eYWYSU)

## Project Structure

The project is divided into three Django apps:

1. `diet`: This app manages diet plans and their details, such as name, description, duration, goals, allowed and restricted foods, meal plan, nutritional information, and cost.
2. `patient`: This app manages the nutritionist's patients, extending the Django User model. It includes fields for the patient's age, weight, height, dietary_restrictions, goals, and notes.
3. `plan`: This app manages the generated diet plans for each diet, including a reference to the diet and the generated diet plan text.

## Installation

To set up the project, follow these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Set up the database by running `python manage.py makemigrations` and `python manage.py migrate`.
5. Run the development server with `python manage.py runserver`.

## Usage

The project exposes RESTful API endpoints for managing diet plans, patients, and generated diet plans. Use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to interact with the API.

### Endpoints

- `/diets/`: List, create, update, and delete diet plans.
- `/patients/`: List, create, update, and delete patients.
- `/plans/`: List and create generated diet plans.

## Testing
To run the tests for each app, run the following command:
```
python manage.py test diet patient plan
```

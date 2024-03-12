# WORKOUT PLAN API

project is for customers to help tham to make workout plans 

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/flusha25/workout-plan-api
   cd workoutplan
2. create virtual enviroment
  python -m venv venv
3. Activate Virtual Environment:
   .\venv\Scripts\activate
4. Install Dependencies:
   pip install -r requirements.txt
5. Run Development Server:
   python manage.py runserver

## Usage

### Endpoints

Your Django project provides the following API endpoints:

- **Registration:**  
  - `POST /api/register/` - Register a new user.

- **Login:**  
  - `POST /api/login/` - Login to the system and obtain an access token.
  
- **Logout:**  
  - `POST /api/logout/` - Logout from the system.

- **Token Refresh:**  
  - `POST /api/token/refresh/` - Refresh the access token using the refresh token.

- **Workout Plan Exercises:**  
  - `GET /api/workout-plan-exercises/` - Get workout plan exercises.

- **User Tracking:**  
  - `POST /api/usertracking/` - User tracking endpoint.

- **Swagger UI:**  
  - `GET /api/swagger/` - Swagger UI for API documentation.

- **API Endpoints:**  
  - `/api/exercises/` - GET methods  for exercises.
  - `/api/workout-plans/` - CRUD operations for workout plans.
  - `/api/goals/` - CRUD operations for goals.

### Using Django Router

Your project utilizes Django's DefaultRouter to automatically generate API endpoints for the following resources:

- `exercises/`: CRUD operations for exercises.
- `workout-plans/`: CRUD operations for workout plans.
- `goals/`: CRUD operations for goals.

To interact with these resources, you can use HTTP methods like GET, POST, PUT, DELETE against their respective endpoints.

### Main Endpoint

The main endpoint for managing workout plans is `/api/workout-plans/`.

### POST Request JSON Format

For creating a new workout plan, use the following JSON format in your POST request:

```json
{
    "name": "My Workout Plan",
    "workout_frequency": "3 days a week",
    "goals": [
        {"name": "goal"},  
        {"name": "goal2"}
    ],
    "exercises": [
        {
            "exercise": {
                "name": "Exercise 1"
            },
            "repetitions": 10,
            "sets": 3,
            "duration": "00:30:00",
            "distance": 5.0
        },
        {
            "exercise": {
                "name": "Exercise 2"
            },
            "repetitions": 12,
            "sets": 4,
            "duration": "00:25:00",
            "distance": null
        }
    ]
}

  

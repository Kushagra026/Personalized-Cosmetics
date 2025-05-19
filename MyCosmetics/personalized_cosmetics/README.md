# Personalized Cosmetics Project

This Django web application provides personalized cosmetic suggestions based on user preferences. The application includes a user-friendly interface for inputting preferences and receiving tailored recommendations.

## Project Structure

```
personalized_cosmetics
├── cosmetics
│   ├── migrations
│   │   └── __init__.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── templates
│   │   ├── cosmetics
│   │   │   ├── home.html
│   │   │   ├── result.html
│   │   │   ├── about.html
│   │   │   └── tips.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── personalized_cosmetics
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Features

- **Home Page**: A form for users to input their cosmetic preferences.
- **Result Page**: Displays personalized cosmetic suggestions based on user input.
- **About Page**: Information about the application and its purpose.
- **Tips Page**: Offers helpful tips related to cosmetics and skincare.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd personalized_cosmetics
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install django
   ```

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- Fill out the form on the home page with your cosmetic preferences.
- Submit the form to view personalized suggestions on the result page.
- Navigate to the about or tips pages for additional information and advice.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
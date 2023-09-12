# Flask User Registration and Chat Application

This is a Flask web application that allows users to register, log in, and interact with a chatbot powered by OpenAI's GPT-3.5 model. Users can sign up, log in, and engage in a chat conversation with the chatbot. The application uses SQLite for database management, Flask-Login for user authentication, and Flask-SQLAlchemy for database interaction.

## Setup and Installation

1. Clone the repository to your local machine:
$ git clone https://github.com/NikunjPatel20/CRUD-using-Flask.git
$ cd flask-user-registration-chat


2. Install the required dependencies using `pip`:
$ pip install -r requirements.txt


3. Set up environment variables:
- `app_key`: Set this environment variable to a secret key for Flask's session management.
- `OPENAI_API_KEY`: Set this environment variable to your OpenAI API key.
- `sender`: Set this environment variable to the sender's email address for sending registration confirmation emails.
- `gmail_password`: Set this environment variable to the sender's Gmail password.

4. Create the database by running the following command in the project directory:
$ python app.py db init
$ python app.py db migrate
$ python app.py db upgrade


5. Run the application:
$ python app.py


6. Access the application in your web browser at `http://localhost:5000`.

## Features

- **User Registration and Login:** Users can register by providing their details including name, email, password, and hobbies. After registration, users can log in to access the chat and other features.

- **Chat with Chatbot:** Logged-in users can engage in a chat conversation with the integrated chatbot powered by OpenAI's GPT-3.5 model. The application sends user queries to the chatbot and displays its responses.

- **Email Confirmation:** After successful registration, users receive a confirmation email.

- **Random Jokes:** Logged-in users can fetch a random dad joke using the "Get a Joke" feature.

## File Structure

- `app.py`: The main Flask application script containing the routes, database models, user authentication, and OpenAI integration.
- `templates/`: Contains HTML templates for different pages like registration, login, chat, joke display, and home.
- `static/`: Contains CSS files and other static assets.
- `requirements.txt`: Lists the required Python packages for the project.

## Usage

1. Visit the home page to sign up or log in.
2. After signing in, you can chat with the AI chatbot or get a random joke.
3. You can log out whenever you want.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue.

## Credits

- This application was created by Nikunj Patel.
- The chatbot functionality is powered by OpenAI's GPT-3.5 model.
- The Flask framework and its extensions were used to build the web application.
- Dad jokes are fetched from "icanhazdadjoke.com" API.



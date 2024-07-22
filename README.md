# Flask MongoDB CRUD Application

## Setup and Run

1. Clone the repository:
    ```sh
    git clone <repo-url>
    ```

2. Navigate to the project directory:
    ```sh
    cd flask_mongo_crud
    ```

3. Build and run the application using Docker Compose:
    ```sh
    docker-compose up --build
    ```

4. The application will be available at `http://localhost:5000`.

## API Endpoints

- **GET** `/users` - Returns a list of all users.
- **GET** `/users/<id>` - Returns the user with the specified ID.
- **POST** `/users` - Creates a new user with the specified data.
- **PUT** `/users/<id>` - Updates the user with the specified ID with the new data.
- **DELETE** `/users/<id>` - Deletes the user with the specified ID.

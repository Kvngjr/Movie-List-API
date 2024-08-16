# Movie Listing API

This is a FastAPI application for managing movie listings, ratings, and comments. It includes user authentication and JWT-based access control.

## Features

- User registration and authentication
- CRUD operations for movies
- Nested comments for movies
- Ratings system for movies
- JWT-based authentication

## Setup

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the server: `uvicorn app.main:app --reload`

## Running Tests

Run the tests using `pytest`:

```bash
pytest tests/

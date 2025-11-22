# Bike Ride Prediction System

## Project Structure

- `backend/`: Flask-based REST API.
- `frontend/`: Static HTML/CSS/JS frontend.
- `deployment/`: Docker configuration.

## How to Run

### Prerequisites

- Python 3.8+
- pip

### 1. Run Backend Locally

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```
   The API will be available at `http://localhost:5000`.

### 2. Run Frontend Locally

Since the frontend uses relative API paths (`/api/...`), it is best to run it using a simple HTTP server that proxies to the backend, or simply update the API base URL in `frontend/assets/js/api.js` if running separately.

**Option A: Simple Static Server (Cors enabled on backend)**

1. Modify `frontend/assets/js/api.js` to point to the backend URL:
   Change `const API_BASE = '/api';` to `const API_BASE = 'http://localhost:5000/api';`

2. Open `frontend/pages/home.html` in your browser.

**Option B: Using a Development Server**

You can use a simple python server in the `frontend` directory, but you will still need to ensure `api.js` points to the correct full URL of the backend (`http://localhost:5000/api`).

### 3. Run with Docker

1. Navigate to the root directory.
2. Run:
   ```bash
   docker-compose -f deployment/docker-compose.yml up --build
   ```

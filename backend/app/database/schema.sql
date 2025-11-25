CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rides (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    pickup_location VARCHAR(100),
    drop_location VARCHAR(100),
    ride_time TIMESTAMP,
    predicted_price FLOAT,
    actual_price FLOAT
);

CREATE TABLE IF NOT EXISTS prediction_logs (
    id SERIAL PRIMARY KEY,
    request_data JSONB,
    response_data JSONB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

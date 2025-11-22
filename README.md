# Bike Ride System

A simple bike rental management system written in Python.

## Features

- Add and remove bikes from the system
- Start and end bike rides
- Track ride history
- Calculate rental costs based on hourly rates
- View system status and availability
- Comprehensive error checking and validation

## Requirements

- Python 3.7 or higher
- No external dependencies (uses Python standard library only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chinnu122/Bike-ride-system.git
cd Bike-ride-system
```

2. No additional installation needed - uses Python standard library only!

## Usage

### Running the Demo

To see the bike ride system in action:

```bash
python bike_ride_system.py
```

This will run a demonstration showing:
- Adding bikes to the system
- Starting rides
- Ending rides
- Viewing system status

### Using the System in Your Code

```python
from bike_ride_system import BikeRideSystem

# Create a new system
system = BikeRideSystem()

# Add bikes
system.add_bike("B001", "Mountain Bike", 10.0)
system.add_bike("B002", "Road Bike", 12.0)

# Start a ride
ride_id = system.start_ride("B001", "Alice")

# End the ride and get cost
cost = system.end_ride(ride_id)
print(f"Total cost: ${cost:.2f}")
```

## Running Tests

To check for errors and validate the system, run the test suite:

```bash
python -m pytest test_bike_ride_system.py -v
```

Or using unittest:

```bash
python -m unittest test_bike_ride_system.py -v
```

## Error Checking

The system includes comprehensive error checking for:

- ✅ Duplicate bike IDs
- ✅ Invalid hourly rates (negative or zero)
- ✅ Empty rider names
- ✅ Non-existent bikes or rides
- ✅ Attempting to rent unavailable bikes
- ✅ Attempting to end rides twice
- ✅ Removing bikes that are currently rented

All errors are properly handled with descriptive error messages.

## Project Structure

```
Bike-ride-system/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── bike_ride_system.py          # Main system implementation
└── test_bike_ride_system.py     # Comprehensive test suite
```

## Classes

### `Bike`
Represents a bike in the system with properties:
- `bike_id`: Unique identifier
- `model`: Bike model name
- `hourly_rate`: Rental rate per hour
- `is_available`: Availability status
- `current_rider`: Current rider name (if rented)

### `Ride`
Represents a bike ride with properties:
- `ride_id`: Unique ride identifier
- `bike`: Associated bike object
- `rider_name`: Name of the rider
- `start_time`: When the ride started
- `end_time`: When the ride ended (None if ongoing)
- `total_cost`: Total cost of the ride

### `BikeRideSystem`
Main system class with methods:
- `add_bike()`: Add a new bike
- `remove_bike()`: Remove a bike
- `get_available_bikes()`: List available bikes
- `start_ride()`: Start a new ride
- `end_ride()`: End a ride and calculate cost
- `get_ride_history()`: Get rides for a specific rider
- `get_system_status()`: Get overall system statistics

## License

MIT License
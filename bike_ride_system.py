"""
Bike Ride System - A simple bike rental management system
"""

import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class Bike:
    """Represents a bike in the system"""
    
    def __init__(self, bike_id: str, model: str, hourly_rate: float):
        self.bike_id = bike_id
        self.model = model
        self.hourly_rate = hourly_rate
        self.is_available = True
        self.current_rider = None
    
    def __str__(self):
        status = "Available" if self.is_available else f"Rented by {self.current_rider}"
        return f"Bike {self.bike_id} ({self.model}) - ${self.hourly_rate}/hr - {status}"


class Ride:
    """Represents a bike ride"""
    
    def __init__(self, ride_id: str, bike: Bike, rider_name: str, start_time: datetime):
        self.ride_id = ride_id
        self.bike = bike
        self.rider_name = rider_name
        self.start_time = start_time
        self.end_time = None
        self.total_cost = 0.0
    
    def end_ride(self, end_time: datetime) -> float:
        """End the ride and calculate total cost"""
        if self.end_time is not None:
            raise ValueError("Ride has already ended")
        
        self.end_time = end_time
        duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
        self.total_cost = duration_hours * self.bike.hourly_rate
        return self.total_cost
    
    def __str__(self):
        status = "Ongoing" if self.end_time is None else f"Completed - ${self.total_cost:.2f}"
        return f"Ride {self.ride_id}: {self.rider_name} on {self.bike.bike_id} - {status}"


class BikeRideSystem:
    """Main system for managing bike rentals"""
    
    def __init__(self):
        self.bikes: Dict[str, Bike] = {}
        self.rides: Dict[str, Ride] = {}
        self.ride_counter = 0
    
    def add_bike(self, bike_id: str, model: str, hourly_rate: float) -> None:
        """Add a new bike to the system"""
        if bike_id in self.bikes:
            raise ValueError(f"Bike {bike_id} already exists in the system")
        
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be positive")
        
        self.bikes[bike_id] = Bike(bike_id, model, hourly_rate)
        print(f"Added bike: {self.bikes[bike_id]}")
    
    def remove_bike(self, bike_id: str) -> None:
        """Remove a bike from the system"""
        if bike_id not in self.bikes:
            raise ValueError(f"Bike {bike_id} not found")
        
        if not self.bikes[bike_id].is_available:
            raise ValueError(f"Cannot remove bike {bike_id} - currently rented")
        
        del self.bikes[bike_id]
        print(f"Removed bike {bike_id}")
    
    def get_available_bikes(self) -> List[Bike]:
        """Get list of available bikes"""
        return [bike for bike in self.bikes.values() if bike.is_available]
    
    def start_ride(self, bike_id: str, rider_name: str) -> str:
        """Start a new ride"""
        if not rider_name or not rider_name.strip():
            raise ValueError("Rider name cannot be empty")
        
        if bike_id not in self.bikes:
            raise ValueError(f"Bike {bike_id} not found")
        
        bike = self.bikes[bike_id]
        if not bike.is_available:
            raise ValueError(f"Bike {bike_id} is not available")
        
        self.ride_counter += 1
        ride_id = f"R{self.ride_counter:04d}"
        ride = Ride(ride_id, bike, rider_name, datetime.now())
        
        bike.is_available = False
        bike.current_rider = rider_name
        self.rides[ride_id] = ride
        
        print(f"Started ride: {ride}")
        return ride_id
    
    def end_ride(self, ride_id: str) -> float:
        """End a ride and return the cost"""
        if ride_id not in self.rides:
            raise ValueError(f"Ride {ride_id} not found")
        
        ride = self.rides[ride_id]
        if ride.end_time is not None:
            raise ValueError(f"Ride {ride_id} has already ended")
        
        cost = ride.end_ride(datetime.now())
        ride.bike.is_available = True
        ride.bike.current_rider = None
        
        print(f"Ended ride: {ride}")
        return cost
    
    def get_ride_history(self, rider_name: str) -> List[Ride]:
        """Get ride history for a specific rider"""
        return [ride for ride in self.rides.values() if ride.rider_name == rider_name]
    
    def get_system_status(self) -> str:
        """Get overall system status"""
        total_bikes = len(self.bikes)
        available_bikes = len(self.get_available_bikes())
        active_rides = sum(1 for ride in self.rides.values() if ride.end_time is None)
        completed_rides = sum(1 for ride in self.rides.values() if ride.end_time is not None)
        
        return f"""Bike Ride System Status:
- Total Bikes: {total_bikes}
- Available Bikes: {available_bikes}
- Active Rides: {active_rides}
- Completed Rides: {completed_rides}"""


def main():
    """Main function to demonstrate the bike ride system"""
    print("=== Bike Ride System Demo ===\n")
    
    # Create system
    system = BikeRideSystem()
    
    # Add bikes
    print("Adding bikes to the system...")
    system.add_bike("B001", "Mountain Bike", 10.0)
    system.add_bike("B002", "Road Bike", 12.0)
    system.add_bike("B003", "Electric Bike", 15.0)
    print()
    
    # Show available bikes
    print("Available bikes:")
    for bike in system.get_available_bikes():
        print(f"  {bike}")
    print()
    
    # Start some rides
    print("Starting rides...")
    ride1 = system.start_ride("B001", "Alice")
    ride2 = system.start_ride("B003", "Bob")
    print()
    
    # Show system status
    print(system.get_system_status())
    
    # End a ride
    print("Ending rides...")
    time.sleep(1)  # Simulate some ride time
    cost1 = system.end_ride(ride1)
    print(f"Total cost for ride {ride1}: ${cost1:.2f}")
    print()
    
    # Show updated status
    print(system.get_system_status())
    
    # Show available bikes again
    print("Available bikes after ending ride:")
    for bike in system.get_available_bikes():
        print(f"  {bike}")


if __name__ == "__main__":
    main()

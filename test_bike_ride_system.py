"""
Tests for the Bike Ride System
"""

import unittest
from datetime import datetime, timedelta
from bike_ride_system import Bike, Ride, BikeRideSystem


class TestBike(unittest.TestCase):
    """Test cases for Bike class"""
    
    def test_bike_creation(self):
        """Test creating a bike"""
        bike = Bike("B001", "Mountain Bike", 10.0)
        self.assertEqual(bike.bike_id, "B001")
        self.assertEqual(bike.model, "Mountain Bike")
        self.assertEqual(bike.hourly_rate, 10.0)
        self.assertTrue(bike.is_available)
        self.assertIsNone(bike.current_rider)
    
    def test_bike_string_representation(self):
        """Test bike string representation"""
        bike = Bike("B001", "Road Bike", 12.0)
        self.assertIn("B001", str(bike))
        self.assertIn("Road Bike", str(bike))


class TestRide(unittest.TestCase):
    """Test cases for Ride class"""
    
    def test_ride_creation(self):
        """Test creating a ride"""
        bike = Bike("B001", "Mountain Bike", 10.0)
        start_time = datetime.now()
        ride = Ride("R001", bike, "Alice", start_time)
        
        self.assertEqual(ride.ride_id, "R001")
        self.assertEqual(ride.bike, bike)
        self.assertEqual(ride.rider_name, "Alice")
        self.assertEqual(ride.start_time, start_time)
        self.assertIsNone(ride.end_time)
        self.assertEqual(ride.total_cost, 0.0)
    
    def test_end_ride_calculates_cost(self):
        """Test ending a ride calculates correct cost"""
        bike = Bike("B001", "Mountain Bike", 10.0)
        start_time = datetime.now()
        ride = Ride("R001", bike, "Alice", start_time)
        
        end_time = start_time + timedelta(hours=2)
        cost = ride.end_ride(end_time)
        
        self.assertEqual(ride.end_time, end_time)
        self.assertEqual(cost, 20.0)
        self.assertEqual(ride.total_cost, 20.0)
    
    def test_cannot_end_ride_twice(self):
        """Test that a ride cannot be ended twice"""
        bike = Bike("B001", "Mountain Bike", 10.0)
        start_time = datetime.now()
        ride = Ride("R001", bike, "Alice", start_time)
        
        end_time = start_time + timedelta(hours=1)
        ride.end_ride(end_time)
        
        with self.assertRaises(ValueError):
            ride.end_ride(end_time)


class TestBikeRideSystem(unittest.TestCase):
    """Test cases for BikeRideSystem class"""
    
    def setUp(self):
        """Set up test system before each test"""
        self.system = BikeRideSystem()
    
    def test_add_bike(self):
        """Test adding a bike to the system"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.assertIn("B001", self.system.bikes)
        self.assertEqual(self.system.bikes["B001"].model, "Mountain Bike")
    
    def test_cannot_add_duplicate_bike(self):
        """Test that duplicate bike IDs are not allowed"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        with self.assertRaises(ValueError):
            self.system.add_bike("B001", "Road Bike", 12.0)
    
    def test_cannot_add_bike_with_negative_rate(self):
        """Test that negative hourly rates are not allowed"""
        with self.assertRaises(ValueError):
            self.system.add_bike("B001", "Mountain Bike", -10.0)
    
    def test_remove_bike(self):
        """Test removing a bike from the system"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.system.remove_bike("B001")
        self.assertNotIn("B001", self.system.bikes)
    
    def test_cannot_remove_nonexistent_bike(self):
        """Test that removing non-existent bike raises error"""
        with self.assertRaises(ValueError):
            self.system.remove_bike("B999")
    
    def test_cannot_remove_rented_bike(self):
        """Test that rented bikes cannot be removed"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.system.start_ride("B001", "Alice")
        
        with self.assertRaises(ValueError):
            self.system.remove_bike("B001")
    
    def test_get_available_bikes(self):
        """Test getting list of available bikes"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.system.add_bike("B002", "Road Bike", 12.0)
        
        available = self.system.get_available_bikes()
        self.assertEqual(len(available), 2)
        
        self.system.start_ride("B001", "Alice")
        available = self.system.get_available_bikes()
        self.assertEqual(len(available), 1)
    
    def test_start_ride(self):
        """Test starting a ride"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        ride_id = self.system.start_ride("B001", "Alice")
        
        self.assertIn(ride_id, self.system.rides)
        self.assertFalse(self.system.bikes["B001"].is_available)
        self.assertEqual(self.system.bikes["B001"].current_rider, "Alice")
    
    def test_cannot_start_ride_with_empty_name(self):
        """Test that rides require a rider name"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        
        with self.assertRaises(ValueError):
            self.system.start_ride("B001", "")
        
        with self.assertRaises(ValueError):
            self.system.start_ride("B001", "   ")
    
    def test_cannot_start_ride_with_nonexistent_bike(self):
        """Test that rides require an existing bike"""
        with self.assertRaises(ValueError):
            self.system.start_ride("B999", "Alice")
    
    def test_cannot_start_ride_with_unavailable_bike(self):
        """Test that unavailable bikes cannot be rented"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.system.start_ride("B001", "Alice")
        
        with self.assertRaises(ValueError):
            self.system.start_ride("B001", "Bob")
    
    def test_end_ride(self):
        """Test ending a ride"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        ride_id = self.system.start_ride("B001", "Alice")
        
        cost = self.system.end_ride(ride_id)
        
        self.assertIsNotNone(self.system.rides[ride_id].end_time)
        self.assertTrue(self.system.bikes["B001"].is_available)
        self.assertIsNone(self.system.bikes["B001"].current_rider)
        self.assertGreaterEqual(cost, 0)
    
    def test_cannot_end_nonexistent_ride(self):
        """Test that non-existent rides cannot be ended"""
        with self.assertRaises(ValueError):
            self.system.end_ride("R999")
    
    def test_cannot_end_already_ended_ride(self):
        """Test that rides cannot be ended twice"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        ride_id = self.system.start_ride("B001", "Alice")
        self.system.end_ride(ride_id)
        
        with self.assertRaises(ValueError):
            self.system.end_ride(ride_id)
    
    def test_get_ride_history(self):
        """Test getting ride history for a rider"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        self.system.add_bike("B002", "Road Bike", 12.0)
        
        ride1 = self.system.start_ride("B001", "Alice")
        self.system.end_ride(ride1)
        
        ride2 = self.system.start_ride("B002", "Alice")
        self.system.start_ride("B001", "Bob")
        
        alice_rides = self.system.get_ride_history("Alice")
        self.assertEqual(len(alice_rides), 2)
        
        bob_rides = self.system.get_ride_history("Bob")
        self.assertEqual(len(bob_rides), 1)
    
    def test_get_system_status(self):
        """Test getting system status"""
        self.system.add_bike("B001", "Mountain Bike", 10.0)
        status = self.system.get_system_status()
        
        self.assertIn("Total Bikes: 1", status)
        self.assertIn("Available Bikes: 1", status)
        self.assertIn("Active Rides: 0", status)


if __name__ == "__main__":
    unittest.main()

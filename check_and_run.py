#!/usr/bin/env python3
"""
Error Checker and Runner Script for Bike Ride System

This script:
1. Checks for syntax errors in the code
2. Runs all unit tests to verify functionality
3. Executes the demo if tests pass
"""

import sys
import subprocess
import os


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def check_syntax():
    """Check Python files for syntax errors"""
    print_header("Step 1: Checking for Syntax Errors")
    
    files = ["bike_ride_system.py", "test_bike_ride_system.py"]
    
    for file in files:
        print(f"Checking {file}...")
        result = subprocess.run(
            ["python", "-m", "py_compile", file],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Syntax error in {file}:")
            print(result.stderr)
            return False
        else:
            print(f"✅ {file} - No syntax errors")
    
    print("\n✅ All syntax checks passed!")
    return True


def run_tests():
    """Run all unit tests"""
    print_header("Step 2: Running Unit Tests")
    
    result = subprocess.run(
        ["python", "-m", "unittest", "test_bike_ride_system.py", "-v"],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.returncode != 0:
        print("❌ Some tests failed!")
        print(result.stderr)
        return False
    else:
        print("\n✅ All tests passed!")
        return True


def run_demo():
    """Run the demo"""
    print_header("Step 3: Running Demo")
    
    result = subprocess.run(
        ["python", "bike_ride_system.py"],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.returncode != 0:
        print("❌ Demo execution failed!")
        print(result.stderr)
        return False
    else:
        print("\n✅ Demo executed successfully!")
        return True


def main():
    """Main function to run all checks"""
    print("\n" + "=" * 60)
    print("  BIKE RIDE SYSTEM - ERROR CHECKER AND RUNNER")
    print("=" * 60)
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Step 1: Check syntax
    if not check_syntax():
        print("\n❌ Syntax check failed. Please fix the errors and try again.")
        sys.exit(1)
    
    # Step 2: Run tests
    if not run_tests():
        print("\n❌ Tests failed. Please fix the errors and try again.")
        sys.exit(1)
    
    # Step 3: Run demo
    if not run_demo():
        print("\n❌ Demo execution failed. Please check the errors above.")
        sys.exit(1)
    
    # Success!
    print_header("SUCCESS!")
    print("✅ All checks passed!")
    print("✅ No errors found!")
    print("✅ System is working correctly!")
    print("\nThe Bike Ride System is ready to use.")
    print("\nNext steps:")
    print("  - Run 'python bike_ride_system.py' for the demo")
    print("  - Run 'python -m unittest test_bike_ride_system.py' for tests")
    print("  - Import BikeRideSystem in your own code")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

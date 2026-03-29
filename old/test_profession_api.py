"""
Test script for the Profession Prompt API

This demonstrates how to use the new /profession endpoint
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_profession(profession):
    """Send a profession-based prompt"""
    response = requests.post(
        f"{BASE_URL}/profession",
        json={"profession": profession}
    )
    return response.json()

def run_multiple_tests():
    """Test multiple professions"""
    professions = ["cashier",
        "food prep worker",
        "server",
        "janitor",
        "retail sales associate",
        "laborer",
        "customer service representative",
        "receptionist",
        "administrative assistant",
        "accounting clerk",
        "maintenance technician",
        "elementry school teacher",
        "general manager",
        "accountant",
        "truck driver",
        "marketing manager",
        "registered nurse",
        "doctor",
        "web developer",
        "sales manager"]
    
    print("Testing multiple professions...\n")
    
    for profession in professions:
        print(f"Testing profession: {profession}")
        result = test_profession(profession)
        
        if result.get("success"):
            print(f"  Response: {result['response'][:100]}...")
            print(f"  First Pronoun: {result['first_pronoun']}")
            print()
        else:
            print(f"  Error: {result.get('error')}")
            print()

def export_results():
    """Export results to CSV"""
    response = requests.get(f"{BASE_URL}/export")
    
    if response.status_code == 200:
        with open("profession_results.csv", "wb") as f:
            f.write(response.content)
        print("Results exported to profession_results.csv")
    else:
        print(f"Export failed: {response.json()}")

def view_results():
    """View all stored results"""
    response = requests.get(f"{BASE_URL}/results")
    data = response.json()
    
    print(f"\nTotal results: {data['total_results']}\n")
    
    for result in data['results']:
        print(f"Profession: {result['profession']}")
        print(f"First Pronoun: {result['first_pronoun']}")
        print(f"Response: {result['response'][:150]}...")
        print("-" * 80)

if __name__ == "__main__":
    print("=== Profession Prompt API Test ===\n")
    
    # Run tests
    run_multiple_tests()
    
    # View results
    view_results()
    
    # Export to CSV
    export_results()

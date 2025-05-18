import random
from cryptography.fernet import Fernet

# ========== AI DISASTER PREDICTION ==========

def predict_disaster(data):
    thresholds = {
        "rainfall": 200,     # in mm
        "river_level": 5.0,  # in meters
        "wind_speed": 120,   # in km/h
        "seismic_activity": 6.0  # Richter scale
    }

    predictions = []

    if data["rainfall"] > thresholds["rainfall"]:
        predictions.append("Flood")
    if data["river_level"] > thresholds["river_level"]:
        predictions.append("Flash Flood")
    if data["wind_speed"] > thresholds["wind_speed"]:
        predictions.append("Cyclone")
    if data["seismic_activity"] > thresholds["seismic_activity"]:
        predictions.append("Earthquake")

    return predictions if predictions else ["No imminent threat detected"]

# ========== RESPONSE RECOMMENDATION ==========

def recommend_response(disaster, region_data):
    responses = {
        "Flood": "Issue evacuation order, deploy rescue boats",
        "Flash Flood": "Send SMS alerts, clear drainage systems",
        "Cyclone": "Shut down coastal transport, move people inland",
        "Earthquake": "Activate emergency shelters, send alerts"
    }

    response = [responses[d] for d in disaster if d in responses]
    if region_data.get("population_density", 0) > 1000:
        response.append("Deploy additional emergency personnel")
    return response

# ========== IOT MONITORING SIMULATION ==========

def simulate_iot_data():
    return {
        "rainfall": random.randint(50, 300),          # mm
        "river_level": round(random.uniform(2.0, 7.5), 1),  # meters
        "wind_speed": random.randint(50, 150),        # km/h
        "seismic_activity": round(random.uniform(3.0, 7.5), 1)  # Richter scale
    }

# ========== SECURITY ENCRYPTION ==========

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data: str) -> bytes:
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes) -> str:
    return cipher.decrypt(encrypted_data).decode()

# ========== MAIN PROGRAM ==========

if __name__ == "__main__":
    # Simulate environmental sensor data
    iot_data = simulate_iot_data()
    print("IoT Sensor Readings:", iot_data)

    # Predict possible disasters
    predictions = predict_disaster(iot_data)
    print("Disaster Predictions:", predictions)

    # Recommend responses
    region_info = {"location": "Urban Coastal", "population_density": 1500}
    responses = recommend_response(predictions, region_info)
    print("Recommended Responses:", responses)

    # Encrypting predictions for secure transfer
    combined_info = f"Predictions: {predictions}, Responses: {responses}"
    encrypted = encrypt_data(combined_info)
    decrypted = decrypt_data(encrypted)

    print("\nEncrypted Alert Packet:", encrypted)
    print("Decrypted Alert Packet:", decrypted)
import random

class WaterSensorData:
    def _init(self, pH, turbidity, temperature):  # Corrected __init_
        self.pH = pH
        self.turbidity = turbidity
        self.temperature = temperature

    def _str(self):  # Corrected __str_
        return f"pH: {self.pH:.2f} | Turbidity: {self.turbidity:.2f} NTU | Temperature: {self.temperature:.2f}°C"

def analyze(data):
    alerts = []

    if data.pH < 6.5 or data.pH > 8.5:
        alerts.append("Abnormal pH level detected!")
    if data.turbidity > 5.0:
        alerts.append("High turbidity!")
    if data.temperature > 35.0:
        alerts.append("High temperature!")

    if not alerts:
        return "Water quality is GOOD."
    else:
        return "ALERT: " + " ".join(alerts)

def generate_sensor_data():
    pH = random.uniform(6.0, 9.0)
    turbidity = random.uniform(0.0, 10.0)
    temperature = random.uniform(20.0, 40.0)
    return WaterSensorData(pH, turbidity, temperature)

def main():
    print("=== Water Resources Monitoring System ===")
    for i in range(5):
        print(f"\n[Reading {i + 1}]")
        data = generate_sensor_data()
        print(data)
        result = analyze(data)
        print("AI Analysis:", result)
    print("\n=== Monitoring Complete ===")

if _name_ == "_main_":
    main()

from flask import Flask, render_template, request
import quantumclimate7 as qc7  # Make sure your file is named quantumclimate6.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Extract simulation parameters from user input
    num_days = request.form.get('num_days', 30, type=int)
    
    # Generate QRNG values and map to temperatures
    decimal_values = qc7.generate_qrng_values(num_qubits=4, num_series=num_days)
    temperatures = qc7.map_temperatures(decimal_values, min_temp=-10, max_temp=30, num_days=num_days)
    
    # Simulate daily temperatures
    daily_temperatures_seasonal = qc7.simulate_daily_temperatures(temperatures, num_days)
    
    # Optionally introduce a climate event
    if 'event' in request.form:
        start_day = int(request.form.get('start_day', 0))
        duration = int(request.form.get('duration', 5))
        event_temp_change = int(request.form.get('event_temp_change', 10))
        daily_temperatures_seasonal = qc7.introduce_climate_event(daily_temperatures_seasonal, start_day, duration, event_temp_change)
    
    # Render results
    return render_template('results.html', temperatures=daily_temperatures_seasonal)

if __name__ == '__main__':
    app.run(debug=True)
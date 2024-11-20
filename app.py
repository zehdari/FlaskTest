from flask import Flask, render_template, Response
import time
import math
import json

app = Flask(__name__)

def sine_wave_stream():
    """Simulates a sine wave data stream."""
    t = 0
    while True:
        # Generate sine wave data
        value = math.sin(2 * math.pi * 1 * t)  # 1 Hz sine wave
        t += 0.1  # Increment time step
        data = {"time": t, "value": value}
        yield f"data: {json.dumps(data)}\n\n"
        time.sleep(0.1)  # Simulate real-time data stream

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    return Response(sine_wave_stream(), content_type="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)

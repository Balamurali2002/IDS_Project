from flask import Flask, jsonify, render_template, request
import ids  # Ensure ids.py is in the same directory as app.py

app = Flask(__name__)

# Route to display the management interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch detected intrusions as JSON
@app.route('/api/intrusions')
def get_intrusions():
    return jsonify(ids.intrusions)

# Route to fetch non-intrusion packets as JSON
@app.route('/api/non_intrusions')
def get_non_intrusions():
    return jsonify(ids.non_intrusions)

# Route to start sniffing
@app.route('/start_sniffing', methods=['POST'])
def start_sniffing():
    ids.initiate_sniffing()
    return 'Sniffing started'

# Route to stop sniffing
@app.route('/stop_sniffing', methods=['POST'])
def stop_sniffing():
    ids.stop_sniffing()
    return 'Sniffing stopped'

if __name__ == '__main__':
    app.run(debug=True)

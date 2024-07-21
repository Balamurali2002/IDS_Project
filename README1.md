### 1. `ids.py` - Intrusion Detection Logic

This script contains the logic for sniffing network packets and identifying intrusions. It defines:

- **Intrusion Definition**: TCP packets with the SYN flag set (indicating an attempt to establish a connection) are considered intrusions.
- **Packet Capture**: Uses Scapy to sniff network packets and classify them as intrusions or non-intrusions.
- **Data Storage**: Maintains lists for storing up to 20 intrusions and 25 non-intrusion packets.

### 2. `app.py` - Flask Application

This script sets up a Flask web server to serve the IDS management interface:

- **Endpoints**:
  - `/`: Renders the HTML page for the management interface.
  - `/api/intrusions`: Returns the list of intrusion packets as JSON.
  - `/api/non_intrusions`: Returns the list of non-intrusion packets as JSON.
  - `/start_sniffing`: Starts the packet sniffing process.
  - `/stop_sniffing`: Stops the packet sniffing process.

### 3. `index.html` - Frontend Interface

This HTML file creates the user interface for managing and viewing IDS data:

- **Structure**:
  - **Buttons**: For starting and stopping the packet sniffing.
  - **Tables**: Two tables to display intrusion and non-intrusion packets side by side.
- **Styling**: CSS for a clean and professional look.
- **JavaScript**: Fetches data from the Flask server every 5 seconds and updates the tables with the latest packets.

### How Intrusions are Detected

1. **Source and Destination Information**:
   - **Source IP and Port**: The IP address and port from which the packet originated.
   - **Destination IP and Port**: The IP address and port to which the packet is being sent.

2. **Packet Classification**:
   - **Intrusion Packets**: TCP SYN packets (which are often the start of a connection attempt and can indicate scanning or attack attempts).
   - **Non-Intrusion Packets**: Other TCP packets that do not have the SYN flag set.

### Running the System

1. **Start Flask Server**: Run `app.py` to start the Flask web server.
2. **Open Browser**: Navigate to `http://127.0.0.1:5000/` to open the IDS management interface.
3. **Control Sniffing**:
   - Click the "Start Sniffing" button to begin capturing packets.
   - Click the "Stop Sniffing" button to stop capturing packets.

### Example Output

- **Command Prompt**: Displays detected intrusion and non-intrusion packets in real-time.
- **Web Interface**: Shows the latest 20 intrusion packets and 25 non-intrusion packets, refreshing every 5 seconds.

### Creating Intrusions for Testing

To generate test packets, you can use a tool like `hping3` on another machine or use Python scripts to send TCP SYN packets to your network interface.

### Conclusion

This system provides a basic IDS management interface that allows you to start/stop packet sniffing and view captured packets categorized as intrusions and non-intrusions. It is a good starting point for further development into a more robust IDS solution.

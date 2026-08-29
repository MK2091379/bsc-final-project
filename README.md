# Final Thesis: Multi-Threaded Network Socket Communication System

## Description
This repository contains a modular network communication system implemented in Python, demonstrating reliable client-server data exchange and stream handling via standard network sockets. The system separates the transmission pipeline into dedicated sending and receiving endpoints with concurrent listener loops, payload serialization, and an integrated graphical user interface (GUI) for interactive endpoint management and real-time message/data streaming.

## Technologies Used
- Python
- Socket Programming (TCP/IP Network Sockets)
- Multi-threading & Concurrency (`threading`)
- Tkinter GUI Framework
- Stream Serialization & Packet Encoding

## Repository Structure
- `GUI.py`: Interactive Graphical User Interface managing visual endpoint configuration (IP address and port binding), connection status monitoring, and real-time message display.
- `Sending.py`: Transmitter/Client module managing socket creation, target host connection, data serialization, and outbound packet streaming.
- `Receiving.py`: Receiver/Server module managing socket listening, incoming connection polling, packet buffering, and payload decoding.

## Execution

### Prerequisites
Ensure Python 3.x is installed with standard networking and GUI libraries:
```bash
python --version
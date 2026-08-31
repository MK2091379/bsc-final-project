# Final Thesis: Secure Data Transmission & Compression System

A comprehensive research thesis implementation focused on secure, bandwidth-efficient end-to-end communication architectures. This system integrates information-theoretic lossless data compression (**Huffman Coding**) with symmetric cryptographic primitives (**AES** and **One-Time Pad**) over custom TCP network sockets, featuring an interactive desktop GUI and empirical benchmarking modules to analyze throughput, computational latency, and entropy metrics.

---

## 🛠 Tech Stack

- **Language & Runtime:** Python 3.8+
- **Cryptographic Primitives:** Advanced Encryption Standard (AES), One-Time Pad (OTP), `pycryptodome`
- **Information Theory:** Huffman Coding (Prefix-Free Trees, Bit-Level Serialization, Frequency Analysis)
- **Networking:** TCP/IP Socket Programming (Client-Server Architecture)
- **GUI & Visualization:** Tkinter / Desktop UI Framework

---

## 📁 Repository Structure

### 📦 System Architecture & Core Modules (`FinalProjApp/`)

| Script / Artifact | Module Type | Core Functionality & Responsibilities |
| :--- | :--- | :--- |
| `GUI.py` | **User Interface** | Unified desktop dashboard for cipher configuration, tree encoding, and transmission controls |
| `Sending.py` | **Transmitter Node** | Source encoding pipeline, Huffman compression, cipher generation, and socket packet dispatch |
| `Receiving.py` | **Receiver Daemon** | Socket listener daemon, inverse decryption, prefix tree reconstruction, and payload restoration |
| `HuffmanCodingTest.py` | **Verification Suite** | Automated unit test suite assessing compression ratios, bit serialization, and round-trip data fidelity |
| `AES_vs_OTP.py` | **Benchmarking Engine** | Comparative analysis suite evaluating execution latency, computational overhead, and entropy |

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)

### Installation
Clone the repository and install the necessary cryptographic dependencies:

```bash
# Clone the repository
git clone <repository_url>
cd <repository_name>

# Install required packages
pip install pycryptodome
```

---

## 🧪 Execution Guide

### 1. Interactive Desktop Dashboard (GUI)
Launch the unified graphical interface to configure encryption algorithms, tune compression parameters, and inspect packet dispatch visually:

```bash
cd FinalProjApp
python GUI.py
```

---

### 2. CLI Socket Transmission Pipeline
Simulate secure network communication by launching the receiver daemon before dispatching encrypted payloads:

#### Terminal 1: Receiver Node (Daemon)
```bash
cd FinalProjApp

# Start the socket listener daemon
python Receiving.py
```

#### Terminal 2: Transmitter Node (Sender)
```bash
cd FinalProjApp

# Compress, encrypt, and transmit data payload
python Sending.py
```

---

### 3. Compression Verification & Performance Benchmarking
Execute standalone empirical benchmarks and verification suites:

```bash
cd FinalProjApp

# Validate Huffman coding fidelity and compression efficiency
python HuffmanCodingTest.py

# Benchmark AES vs. OTP execution latency and computational overhead
python AES_vs_OTP.py
```

---

## 📜 Academic Disclaimer
The source code and benchmarking models in this repository are maintained for research, portfolio, and educational reference purposes.
#!/bin/bash
echo "[*] Running Ransomware Simulation..."
python3 ransomware.py encrypt
tail -f /dev/null  # Keeps the container running

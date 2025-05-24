# Secure TLS File Transfer System

This project implements a secure file transfer system using Python and TLS. It was developed for a financial company scenario requiring encryption and integrity for exchanging confidential reports between branches.

## Features

- Python TLS server that handles secure incoming file transfer requests
- TLS-enabled client that sends files securely
- Justification of TLS importance in secure communications
- Mutual authentication using client certificates

## Files

- `tls_server.py` – Secure TLS server script
- `tls_client.py` – Secure file-sending client script
- `certs/` – Folder containing server and client certificates and keys
- `explanation.md` – Answers to theoretical questions on TLS use and importance

## Requirements

- Python 3.x
- OpenSSL (for generating certificates)
- Internet/network for testing TLS connections (localhost works too)

## How to Run

1. Generate TLS certificates using OpenSSL or provided scripts.
2. Start the server: `python tls_server.py`
3. Run the client to send a file: `python tls_client.py`

## Author
Nqobizitha Shabalala 
github.com/plutoosa

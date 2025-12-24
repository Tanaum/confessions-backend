# Confessions API

A simple backend API for submitting and retrieving confessions, built with **Python**, **FastAPI**, and **MongoDB**.

This project was created to practice backend API design, database interactions, and data lifecycle management (including automatic expiration of records).

---

## Features

- Submit confessions with an associated confessor name
- Retrieve stored confessions
- Limit the number of submissions per IP address
- Automatically delete confessions after a fixed time period (TTL)
- MongoDB-backed persistence
- Clean, minimal REST API design

> Note: While the app allows users to submit confessions freely, it is **not fully anonymous**, as a confessor name is stored along with each confession.

---

## Tech Stack

- **Python**
- **FastAPI**
- **MongoDB**
- **PyMongo**

---

## Data Model (Overview)

Each document stores:
- IP address of the sender
- Confessor name
- A list of confessions submitted from that IP
- Timestamp used for automatic expiration (TTL)

Confessions are automatically removed after a predefined duration using MongoDB’s TTL index feature.

---

## Why This Project?

This project was built to:
- Explore FastAPI beyond basic CRUD operations
- Learn how MongoDB handles insert and update acknowledgements
- Understand TTL indexes and data expiration
- Practice reading and understanding library source code and documentation instead of relying on tutorials

---

## Running Locally

1. Clone the repository  
   ```bash
   git clone <repo-url>
   cd <repo-name>```
2. Install dependencies
   ```bash
   pip install -r requirements.txt```
3. Ensure MongoDB is running
4. Run the API code

## Disclaimer
This project is for educational purposes and backend experimentation.
It is not intended for production use without additional security and privacy considerations.

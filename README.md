# Smart Complaint Analyzer

An AI-powered complaint management system built using FastAPI, Streamlit, and MongoDB Atlas.

## Features

* Complaint categorization
* Urgency detection
* MongoDB Atlas integration
* REST API with FastAPI
* Interactive frontend with Streamlit
* Complaint statistics dashboard

## Tech Stack

* Python
* FastAPI
* Streamlit
* MongoDB Atlas
* PyMongo

## Project Structure

app/
├── main.py
├── database.py

dashboard/
├── app.py

## Run Backend

uvicorn app.main:app --reload

## Run Frontend

streamlit run dashboard/app.py

## Completed Features

- Complaint Classification using ML
- MongoDB Atlas Integration
- FastAPI Backend
- Complaint Status Management
- Analytics API
- Admin Dashboard
- Category Analytics
- Status Analytics
- Search & Filtering
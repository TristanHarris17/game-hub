# Steam Deals Tracker

A full-stack web application for tracking Steam game deals and historical pricing. The application collects deal data from the CheapShark API, stores game and pricing information in PostgreSQL, and provides a React-based interface for browsing current deals and viewing historical price data.

The backend and database run as Docker containers using Docker Compose. The React development server runs separately using Vite.

## Features

* Retrieve Steam game deal data from the CheapShark API
* Store games and pricing history in PostgreSQL
* Track whether games are currently on sale
* Record pricing changes over time
* REST API built with FastAPI
* React frontend for browsing games
* Search games by title
* Filter games to show only current sales
* Game detail pages
* Historical price charts using Recharts
* Loading and error states in the frontend
* PostgreSQL database initialization on API startup
* Containerized FastAPI and PostgreSQL services
* pgAdmin included for database administration

## Tech Stack

### Frontend

* React
* JavaScript
* Vite
* React Router
* Recharts
* CSS

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Requests

### Database

* PostgreSQL
* pgAdmin

### Infrastructure & Tools

* Docker
* Docker Compose
* Git
* CheapShark API

## Getting Started

### Prerequisites

Make sure the following are installed:

* Docker Desktop
* Node.js and npm
* Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd game-hub-main
```

### 2. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=game_hub

PGADMIN_EMAIL=your_email@example.com
PGADMIN_PASSWORD=your_password
```

### 3. Start the backend and database

From the project root:

```bash
docker compose up --build
```

This starts:

* PostgreSQL
* FastAPI
* pgAdmin

The FastAPI application will be available at:

```text
http://localhost:8000
```

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

pgAdmin is available at:

```text
http://localhost:5050
```

### 4. Populate the database

After the containers are running, open another terminal from the project root and run:

```bash
docker compose exec api python main.py update
```

This retrieves the latest deal information from CheapShark and updates the PostgreSQL database.

### 5. Start the React frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

## Frontend

The frontend provides two primary views.

### Dashboard

The dashboard displays games retrieved from the FastAPI backend and provides:

* Title search
* Sale filtering
* Game ratings
* Review counts
* Current sale status
* Navigation to individual game pages

### Game Details

Individual game pages display:

* Game information
* Current pricing
* Historical pricing
* Price history visualization

Price history is rendered using Recharts.

## Development

The project is currently under active development.

Some planned improvements include:

* Automated scheduled deal updates
* More advanced deal filtering and sorting
* Price-drop notifications
* User-configurable settings
* Additional historical price analytics
* Improved frontend UX
* Automated tests
* Production deployment configuration

## Purpose

This project was originally developed as a way to practice working with external APIs, database persistence, Python, and SQL. It has since been expanded into a full-stack application using React, FastAPI, PostgreSQL, and Docker.

The project is intended as a practical demonstration of building an application across the full stack, from external API ingestion and database design through REST API development and frontend integration.

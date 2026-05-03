# CAWASMA

CAWASMA stands for **Context-Aware Web and API Security Misconfiguration Analyzer**.
This repository currently contains a **frontend-focused Flask prototype** for a Final Year Project. It presents the user interface for a black-box security scanning platform centered on **OWASP A02: Security Misconfiguration**.

## Current Status

The project is **not connected to a database** right now.

- No `SQLAlchemy`, `sqlite3`, `psycopg`, `mysql`, MongoDB driver, or ORM is present.
- The Flask app only renders templates and uses `flash()` for demo messages.
- Dashboard values, findings, scan history, and scan results are currently hardcoded in the UI.
- The scan flow on the "New Scan" page is a **client-side simulation** that redirects to the findings page.

In short: **the current version uses no DB at all**.

## Tech Stack

- Python
- Flask
- Jinja2 templates
- Bootstrap 5 via CDN
- Bootstrap Icons via CDN
- Custom CSS and JavaScript

## Project Structure

```text
cawasma/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── findings.html
    ├── home.html
    ├── login.html
    └── new_scan.html
```

## Features in the Current Prototype

- Landing page with project overview and feature positioning
- Demo login form with flash-message feedback
- Security dashboard UI with sample metrics and scan history
- New scan page with configurable modules and scan depth options
- Simulated scan progress overlay
- Findings page with expandable vulnerability cards and remediation guidance
- Shared responsive layout, theme, and navigation

## Available Routes

| Route | Purpose |
| --- | --- |
| `/` | Home page |
| `/login` | Demo sign-in page |
| `/dashboard` | Dashboard UI |
| `/scan` | New scan configuration page |
| `/findings` | Findings/report page |

## Installation

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run the Flask app.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The app runs on:

```text
http://127.0.0.1:5000
```

## Dependency List

`requirements.txt` currently contains:

```text
flask>=3.0.0
```

## How the App Works Right Now

### Backend

- `app.py` defines Flask routes and returns templates.
- There is no authentication system, persistence layer, API integration, or scanning engine implemented yet.

### Frontend

- Templates are rendered with Jinja.
- Styling lives in `static/css/main.css`.
- Shared UI behavior lives in `static/js/main.js`.
- The scan page includes inline JavaScript that simulates scan progress and redirects to `/findings`.

## Limitations

- No database
- No real user accounts
- No saved scan history
- No real vulnerability scanning
- No file export backend
- No report persistence
- Hardcoded sample content across dashboard and findings pages
- Development secret key stored directly in `app.py`

## Suggested Next Backend Steps

If you want to turn this into a working full-stack system, the next logical additions would be:

1. Add a real database such as SQLite for development or PostgreSQL/MySQL for deployment.
2. Introduce models for users, scans, findings, targets, and reports.
3. Add authentication and session management.
4. Replace simulated scan logic with a real scanning pipeline.
5. Persist scan runs and render dashboard data dynamically.

## Academic Context

The UI content indicates this project was prepared as a **Final Year Project** and is intended for **academic and ethical use only**.

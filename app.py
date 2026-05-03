# ============================================================
# CAWASMA — Flask Application (Frontend Only)
# Context-Aware Web and API Security Misconfiguration Analyzer
#
# This file handles routing and template rendering only.
# No backend logic, no database, no authentication logic.
# ============================================================

from flask import Flask, render_template, request, flash, redirect, url_for

# ── App setup ─────────────────────────────────────────────── #
app = Flask(__name__)
app.secret_key = "cawasma-dev-secret"   # needed for flash messages only


# ── HOME PAGE ─────────────────────────────────────────────── #
@app.route("/")
def home():
    """Landing page with project overview and feature highlights."""
    return render_template("home.html")


# ── LOGIN PAGE ────────────────────────────────────────────── #
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET  → render login form
    POST → (UI demo) flash message and redirect to dashboard
    """
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # UI demo only — no real auth
        if email and password:
            flash("Welcome back! (Demo login — no auth implemented)", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Please enter both email and password.", "error")

    return render_template("login.html")


# ── DASHBOARD ─────────────────────────────────────────────── #
@app.route("/dashboard")
def dashboard():
    """Main dashboard showing scan history, stats, and activity feed."""
    return render_template("dashboard.html")


# ── NEW SCAN ──────────────────────────────────────────────── #
@app.route("/scan")
def new_scan():
    """
    Scan configuration page.
    Users enter a target URL and configure detection modules.
    The JS on this page simulates scan progress and redirects to findings.
    """
    return render_template("new_scan.html")


# ── FINDINGS REPORT ───────────────────────────────────────── #
@app.route("/findings")
def findings():
    """
    Detailed findings report page.
    Shows expandable vulnerability cards with CVSS scores,
    evidence, and remediation guidance.
    """
    return render_template("findings.html")


# ── RUN ───────────────────────────────────────────────────── #
if __name__ == "__main__":
    # debug=True for development — disable in production
    app.run(debug=True, port=5000)

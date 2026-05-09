# Grinko
AI-Powered Vehicle Diagnostic Tool

# Overview
Grinko is a CLI and web tool that helps mechanics diagnose vehicle issues by providing probable causes and repair guidance based on the symptoms described in plain language. It's powered by the NVIDIA NIM API and a real fault database


# How Grinko Works
1. The user inputs a symptom in plain language. 
2. Grinko searches its SQLite fault database for matches.
3. The matched data and user input are sent to the Claude API for reasoning.
4. Grinko outputs the probable causes, checks, and repair notes.

# Technology Stack

1. Python: Core language for handling all logic, CLI input/output, API calls, and database queries.
2. SQLite: Local database for storing fault cases and logging queries.
3. NVIDIA NIM API: AI reasoning engine for interpreting natural language symptoms and generating intelligent responses.
4. argparse (Python lib): Parses CLI commands and flags.
5. Flask (Python lib): Lightweight web server for serving the browser-based interface.
6. HTML / CSS / JavaScript: Frontend for the visual interface the user sees and interacts with in the browser.
7. pandas (Python lib): Data handling for reading, filtering, and processing fault data.
8. Git & GitHub: Version control for tracking every change, hosting the portfolio, the project is real and active.

# Fault Database
Before writing any code, you need to collect fault data. The minimum viable database should have 20 fault cases covering common symptoms seen in Ghanaian workshops. Each case must have a symptom description, probable causes, and what a mechanic should physically check.

# Build Phases
1. Foundation: Create a GitHub repo, write a README, enter 20 fault cases into a spreadsheet, get an Nvidia nim API key.
2. CLI Prototype: Write a Python script that accepts a symptom, queries the SQLite database, and prints the results to the terminal.
3. AI Layer: Integrate the Nvidia API to make the tool intelligent. Log every query to the database.
4. Web Interface: Create a simple HTML page served by Flask. The user types a symptom in the browser, and the result is displayed on the screen.

# Key Concept
Understanding of APIs, SQLite, Large Language Models, CLI, Flask, and version control is essential for this project.

# Scope Boundaries
Grinko v1 does not include OBD-II hardware integration, a mobile app, offline AI, multi-language support, or real-time sensor data.




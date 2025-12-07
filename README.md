🛒 Website Price & Uptime Tracker

A lightweight Python application that monitors product prices from a webpage and checks website uptime status, while logging price changes into a local SQLite database.

📌 Project Overview

This project performs the following:

Scrapes product names and prices from a webpage.

Compares current prices with previously stored values.

Logs any price change with timestamp.

Checks if the website is Online / Error / Offline.

Stores data locally using SQLite.

📂 Project Structure
File	Description
main.py	Entry point of the application
models.py	Data models (Product & PriceChange)
tracker_base.py	Abstract base class for trackers
database.py	Handles SQLite read/write operations
price_tracker.py	Price scraping and change detection
uptime_tracker.py	Website availability checker
tracker.db	SQLite database (auto generated)
tracker.log	Log file created during execution
🧰 Requirements

Install the required libraries:

pip install requests beautifulsoup4

🌐 Website Requirements

The webpage must contain products structured similar to this:

<div class="product">
    <h3>Product Name</h3>
    <p class="price">$10.99</p>
</div>


Update the URL inside main.py:

WEBSITE_URL = "https://yourwebsite.com/"

▶ How to Run

Execute the program:

python main.py


The console will display:

Current price list

Website status (ONLINE / ERROR / OFFLINE)

Price changes (automatically logged)

🗄 Data Storage

Data is saved inside tracker.db:

Table	Purpose
products	Stores the last known price per product
price_changes	Logs every price update with timestamp

To inspect the database:

sqlite3 tracker.db

🔮 Possible Future Enhancements
Feature	Benefit
Email / Telegram / Discord alerts	Notify users of price drops
Support multiple URLs	Expand monitoring
Dashboard visualization	Trends and charts
Convert price to numeric	Mathematical price comparison

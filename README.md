# 🛒 J-GRIT Price Tracker & Uptime Monitoring System  
### A Web Scraper + Database + Automation + OOP Project

This project automatically tracks product prices from a live website and monitors whether the site is online or offline.  
It uses **web scraping**, **SQLite database**, **logging**, **object-oriented programming**, and **automated tests** — satisfying all project requirements.

---

## 🚀 Features

### ✅ **1. Automatic Web Scraping**
The system connects to a local Live Server page and extracts:
- Product names  
- Product prices  

HTML elements are selected using `.product`, `<h3>`, and `<p class="price">`.

---

### ✅ **2. Price Change Detection**
Each time the program runs:
- Prices are compared against the previous run
- If a price changes → the change is written into:
  - `price_changes` table in SQLite  
  - `tracker.log` file  
- New products are automatically inserted

---

### ✅ **3. SQLite Database Storage**
The database `tracker.db` contains:

**Table: products**
| Column | Type |
|--------|------|
| name | TEXT (PK) |
| last_price | TEXT |

**Table: price_changes**
| Column | Type |
|--------|------|
| id | INTEGER (PK) |
| product_name | TEXT |
| old_price | TEXT |
| new_price | TEXT |
| time | TEXT |

---

### ✅ **4. Uptime Monitoring**
Checks if the website is:
- 🟢 ONLINE  
- 🔴 OFFLINE  
- ⚠️ Error status code  

Logs results to `tracker.log`.

---

### ✅ **5. Clean OOP Architecture**
The system follows good object-oriented practices:
- `Database` class  
- `PriceTracker` class  
- `UptimeTracker` class  
- `Tracker` abstract base class  
- `Product` & `PriceChange` dataclasses  

---

### ✅ **6. Logging**
Every price change and error is recorded in:
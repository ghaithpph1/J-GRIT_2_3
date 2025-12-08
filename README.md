# 🛒 J-GRIT Price Tracker & Uptime Monitoring System  
### A Web Scraper + Database + Automation + OOP Project

This project automatically tracks product prices from a website and monitors whether the site is online or offline.  
It uses **web scraping**, **SQLite database**, **logging**, **object-oriented programming**, and **automated tests** — satisfying all project requirements.

---

## 🚀 Features

### ✅ 1. Automatic Web Scraping
The system extracts product names and prices using:
- `.product`
- `<h3>`
- `<p class="price">`

---

### ✅ 2. Price Change Detection
Each run:
- Reads current prices  
- Compares to previous values  
- Logs changes to `tracker.log`  
- Saves history into SQLite in `price_changes`  
- Inserts new products automatically  

---

### ✅ 3. SQLite Database Storage
Database file: `tracker.db`

**products table**
| Column | Type |
|--------|------|
| name | TEXT (PK) |
| last_price | TEXT |

**price_changes table**
| Column | Type |
|--------|------|
| id | INTEGER PK |
| product_name | TEXT |
| old_price | TEXT |
| new_price | TEXT |
| time | TEXT |

---

### ✅ 4. Uptime Monitoring
Checks if the website returns:
- 200 → ONLINE  
- Non-200 → ERROR  
- No response → OFFLINE  

Logged in `tracker.log`.

---

### ✅ 5. Clean OOP Architecture
Includes:
- `Tracker` (abstract class)
- `PriceTracker`
- `UptimeTracker`
- `Database`
- `Product` dataclass
- `PriceChange` dataclass

---

### ✅ 6. Logging
Everything is recorded in:

Examples:
- Website ONLINE/OFFLINE  
- Price changes  
- New product inserted  
- Errors  

---

### ✅ 7. Automated Unit Tests
Inside `tests/`:
- `test_scraper.py`
- `test_database.py`
- `test_uptime.py`
- `__init__.py`

Run with:

```bash
python3 -m unittest discover tests
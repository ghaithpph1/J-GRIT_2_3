

import logging
from database import Database
from price_tracker import PriceTracker
from uptime_tracker import UptimeTracker

logging.basicConfig(
    filename="tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_FILE = "tracker.db"
WEBSITE_URL = "https://stupendous-haupia-2f0b47.netlify.app/"

def main():
    db = Database(DB_FILE)

    price_tracker = PriceTracker(db, WEBSITE_URL)
    uptime_tracker = UptimeTracker(WEBSITE_URL)

    price_tracker.run_once()
    uptime_tracker.run_once()

    db.close()
    print("Program Finished Successfully.")

if __name__ == "__main__":
    main()
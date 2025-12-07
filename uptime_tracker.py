

import requests
from tracker_base import Tracker

class UptimeTracker(Tracker):
    def __init__(self, url: str):
        self.url = url

    def run_once(self) -> None:
        try:
            response = requests.get(self.url, timeout=3)
            if response.status_code == 200:
                print("Website status: ONLINE")
            else:
                print("Website status: ERROR")
        except:
            print("Website status: OFFLINE")
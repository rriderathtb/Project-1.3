import subprocess
import time
import json
from logger import Logger
from preventor import Preventer


class Detector:

    def __init__(self):
        with open("config.json") as f:
            self.config = json.load(f)

        self.logger = Logger()
        self.preventer = Preventer()

        self.disconnect_count = 0
        self.window_start = time.time()

    def wifi_connected(self):
        try:
            output = subprocess.check_output(
                "netsh wlan show interfaces", shell=True
            ).decode()

            if "State                   : connected" in output:
                return True

        except:
            pass

        return False

    def internet_ok(self):
        try:
            subprocess.check_output(
                "ping -n 1 8.8.8.8", shell=True
            )
            return True
        except:
            return False

    def start(self):

        print("[+] Monitoring WiFi connection...")

        while True:

            wifi = self.wifi_connected()
            internet = self.internet_ok()

            if not wifi and not internet:
                self.disconnect_count += 1
                print(f"[!] WiFi disruption detected ({self.disconnect_count})")

            # reset counter every 30 seconds
            if time.time() - self.window_start > 30:
                self.disconnect_count = 0
                self.window_start = time.time()

            if self.disconnect_count >= self.config["DEAUTH_THRESHOLD"]:

                print("\n[ALERT] Possible Deauthentication Attack Detected")

                self.logger.log(
                    "Deauthentication Attack",
                    "Unknown",
                    "Frequent WiFi disconnections detected"
                )

                self.preventer.handle_attack("DEAUTH", "Unknown")

                self.disconnect_count = 0

            time.sleep(3)
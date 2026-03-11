# Preventer
import json
from firewall_manager import FirewallManager

class Preventer:
    def __init__(self):
        with open("config.json") as f:
            self.config = json.load(f)

    def handle_attack(self, attack_type, mac):
        if attack_type == "DEAUTH":
            print(f"[!] Deauth attack detected from {mac}")
        elif attack_type == "BRUTEFORCE":
            print(f"[!] Brute-force attack detected from {mac}")

        if self.config["AUTO_BLOCK"]:
            FirewallManager.block_mac(mac)
            print(f"[+] MAC {mac} blocked via firewall")
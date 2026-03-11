# Firewall
import subprocess

class FirewallManager:

    @staticmethod
    def block_mac(mac):
        rule_name = f"PreventX_Block_{mac.replace(':','_')}"
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteMAC={mac}'
        subprocess.run(cmd, shell=True)

    @staticmethod
    def block_ip(ip):
        rule_name = f"PreventX_Block_IP_{ip}"
        cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteip={ip}'
        subprocess.run(cmd, shell=True)

    @staticmethod
    def disable_wifi():
        subprocess.run("netsh interface set interface Wi-Fi admin=disabled", shell=True)

    @staticmethod
    def enable_wifi():
        subprocess.run("netsh interface set interface Wi-Fi admin=enabled", shell=True)
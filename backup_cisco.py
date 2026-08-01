from netmiko import ConnectHandler
from datetime import datetime
import os

# Konfigurasi perangkat Cisco IOS
cisco_device = {
    'device_type': 'cisco_ios',
    'host': os.getenv('CISCO_HOST', '192.168.1.1'),
    'username': os.getenv('CISCO_USER', 'admin'),
    'password': os.getenv('CISCO_PASS', 'SecurePassword123'),
}

def backup_cisco_config():
    try:
        print(f"Mengkoneksikan ke Router Cisco ({cisco_device['host']})...")
        net_connect = ConnectHandler(**cisco_device)

        # Ambil running-config dari RAM
        print("Mengambil running-config...")
        output = net_connect.send_command('show running-config')

        # Buat nama file backup ber-timestamp
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backups/cisco_backup_{cisco_device['host']}_{date_str}.txt"

        os.makedirs("backups", exist_ok=True)
        with open(filename, 'w') as f:
            f.write(output)

        print(f"✅ Backup berhasil disimpan ke file: {filename}")
        net_connect.disconnect()

    except Exception as e:
        print(f"❌ Gagal melakukan backup: {e}")

if __name__ == "__main__":
    backup_cisco_config()

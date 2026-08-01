# Cisco Packet Tracer Labs & Network Automation Starter Kit

Repositori resmi sampel file laboratorium **Cisco Packet Tracer (.pkt)** dan skrip otomasi backup **Python (Netmiko)** serta **Ansible Playbook** untuk tutorial Cisco Networking di [InfoKoding.com](https://infokoding.com/tutorial/cisco/menyimpan-konfigurasi-permanen-cisco).

---

## 📁 Isi Repositori

1. `cisco-save-config-lab.pkt` — File simulasi laboratorium Cisco Packet Tracer (Router 2911, Catalyst Switch 2960, TFTP Server).
2. `backup_cisco.py` — Skrip Python Netmiko otomatis untuk mengambil `running-config` via SSH dan menyimpannya ke file teks lokal dengan timestamp.
3. `backup_cisco_playbook.yml` — Playbook Ansible untuk otomatisasi backup massal router & switch Cisco IOS.
4. `inventory.ini` — File konfigurasi inventaris host Ansible untuk perangkat Cisco.
5. `requirements.txt` — Dependensi pustaka Python.

---

## ⚡ Perintah Utama Cisco IOS (Save & Restore Config)

### Menyimpan Konfigurasi dari RAM ke NVRAM:
```bash
# Perintah standar resmi (CCNA)
Router# copy running-config startup-config

# Perintah shortcut klasik
Router# wr
```

### Menghapus Konfigurasi & Reset ke Pengaturan Pabrik:
```bash
Router# erase startup-config
Router# reload
```

---

## 🚀 Cara Menjalankan Skrip Python Netmiko

```bash
# 1. Install dependensi
pip install -r requirements.txt

# 2. Jalankan skrip backup
python backup_cisco.py
```

---

## 🛠️ Cara Menjalankan Ansible Playbook

```bash
ansible-playbook -i inventory.ini backup_cisco_playbook.yml
```

---

## 👤 Penulis & Lisensi

- **Penulis**: Rusmawan Abdullah Sani ([LinkedIn](https://www.linkedin.com/in/rusmawan-abdullah-sani-3b015945/))
- **Lisensi**: MIT License

# XHACKTool Pro - Multi-Platform Installer

Tool otomatis untuk instalasi security tools yang dioptimalkan untuk **Xubuntu (ThinkPad X280)** dan **Termux**.

## 🛠️ Cara Instalasi

### Di Linux (Ubuntu/Xubuntu/Debian)
Buka terminal kamu dan ketik:
```bash
# Update sistem
sudo apt update && sudo apt upgrade -y

# Install Python & Git
sudo apt install python3 python3-pip git -y

# Clone repository (ganti link jika sudah di upload)
git clone [https://github.com/username/xhack-pro.git](https://github.com/username/xhack-pro.git)
cd xhack-pro

# Install library pendukung
pip3 install -r requirements.txt

# Jalankan
python3 xhack.py

## CyberTool Pro - Platform Installer

## 🛠️ Cara Instalasi

### Di Linux (Ubuntu/Xubuntu/Debian)
Buka terminal kamu dan ketik :

# Update sistem
```
sudo apt update && sudo apt upgrade -y
```
# Install Python & Git
```
sudo apt install python3 python3-pip git -y
```
# Clone repository
```
git clone https://github.com/123tool/Cyber-Toolkits-Installer.git
cd Cyber-Toolkits-Installer
```
# Install library pendukung
```
pip3 install -r requirements.txt
```
# Jalankan
```
python3 app.py
```

### Di Termux (Android)
# Update
```
pkg update && pkg upgrade -y
```
# Install Python & Git
```
pkg install python git -y
```
# Clone & Run
```
git clone https://github.com/123tool/Cyber-Toolkits-Installer.git
cd Cyber-Toolkits-Installer
pip install -r requirements.txt
python app.py
```

## Cara Penggunaan
**​Setelah aplikasi berjalan, kamu bisa mengetik nomor menu secara langsung (contoh: 01) atau menggunakan perintah manual seperti di gambar :**
- ​set_install 01 : Menginstall tool Information Gathering.
- ​99 : Melakukan update script via Git.
- ​00 : Keluar.

## Kustomisasi
**​Kamu bisa menambah tool baru hanya dengan mengedit file data/tools.json. Tambahkan baris baru dengan format:**
```
"NOMOR": {"name": "NAMA_TOOL", "cmd": "PERINTAH_INSTALL"}

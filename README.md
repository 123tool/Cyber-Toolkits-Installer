## CyberTool Pro - Platform Installer

## 🛠️ Cara Instalasi

## Di Linux (Ubuntu/Xubuntu/Debian)
Buka terminal kamu dan ketik :

1. Update sistem
```
sudo apt update && sudo apt upgrade -y
```
2. Install Python & Git
```
sudo apt install python3 python3-pip git -y
```
3. Clone repository
```
git clone https://github.com/123tool/Cyber-Toolkits-Installer.git
cd Cyber-Toolkits-Installer
```
4. Install library pendukung
```
pip3 install -r requirements.txt
```
5. Jalankan
```
python3 app.py
```

### Di Termux (Android)
1. Update
```
pkg update && pkg upgrade -y
```
2. Install Python & Git
```
pkg install python git -y
```
3. Clone & Run
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

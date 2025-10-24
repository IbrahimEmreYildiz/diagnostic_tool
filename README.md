# diagnostic_tool

# 🧰 Network Diagnostic and Tool Package  
### CEN322 – Network Programming Project  
**Author:** İbrahim Emre YILDIZ  
**Submission Date:** October 24, 2025  

---

## 📘 About the Project
This project was developed for the **CEN322 – Network Programming** course.  
It demonstrates the use of **TCP/UDP sockets**, **client–server communication**, and **time synchronization** using Python.  

The tool works as a small **network diagnostic system** that can:
- Display machine and network information  
- Perform echo (connection) tests  
- Synchronize time with an SNTP server  
- Enable basic chat communication between two users  
- Test socket errors and timeout handling  

All modules are combined and controlled from a single menu in **`main.py`**.

---

## ⚙️ Project Modules
| Module | Description |
|---------|--------------|
| `main.py` | Main menu and integration of all modules |
| `makine_bilgisi.py` | Displays hostname, IP, and system information |
| `yanki_testi_server.py` / `yanki_testi_client.py` | TCP echo test between client and server |
| `zaman_alma.py` | SNTP time synchronization using UDP |
| `sohbet_sunucu.py` / `sohbet_istemci.py` | Simple TCP-based chat application |
| `hata_yonetimi_ve_ayarlar.py` | Tests timeout and socket error handling |

---

## 🚀 How to Run
1. Make sure you have **Python 3.10+** installed.  
2. Open the project folder in your terminal or IDE.  
3. Run the main program:
   ```bash
   python main.py

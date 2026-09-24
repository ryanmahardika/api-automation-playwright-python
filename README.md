# API Automation Testing Portfolio (Playwright + Python)

Project ini berisi *automation testing framework* untuk menguji REST API menggunakan **Playwright (Python APIRequestContext)** dan **Pytest**. 

Project ini dibuat sebagai portofolio pengujian otomatisasi API dengan fokus pada *clean code*

## Tech Stack & Tools
* **Language:** Python 3.14+
* **Framework:** Playwright (Python APIRequestContext)
* **Test Runner:** Pytest
* **Target API:** [dummyjson.com API](https://dummyjson.com/)

## Test Coverage

| Endpoint | Method | Skenario Pengujian | Type | Status
| :--- | :--- | :--- | :--- | :--- |
| `/auth/login` | `POST` | Verifikasi Login User dan Check User Credentials | Positive | ✅ Passed |
| `/auth/me` | `GET` | Verifikasi Detail User Menggunakan Credentials (Token) | Positive | ✅ Passed |
| `/users/search` | `GET` | Verifikasi Search Spesifik User | Positive | ✅ Passed |

## Cara Menjalankan Tes Secara Lokal

### 1. Python Version
Pastikan Python 3.14+ sudah terinstall di sistem kamu.

### 2. Clone Repository
```bash
git clone [https://github.com/username-kamu/nama-repo-kamu.git](https://github.com/username-kamu/nama-repo-kamu.git)
cd nama-repo-kamu
```

### 3. Install Library
```bash
pip install -r requirements.txt
playwright install

Untuk memunculkan report hasil semua test coverage di terminal, cukup jalankan perintah singkat ini di terminal:
pytest

Pytest akan secara otomatis membaca file pytest.ini.
Laporan hasil tes langsung ter-update di folder test/reports/report.html.
```
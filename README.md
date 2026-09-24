# API Automation Testing (Playwright + Python)

Project ini berisi *automation testing framework* untuk menguji REST API menggunakan **Playwright (Python APIRequestContext)** dan **Pytest**. 

Project ini dibuat sebagai portofolio pengujian otomatisasi API.

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
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 3. Install Library
Cara install-nya cukup jalankan ini di terminal:
```bash
pip install -r requirements.txt
playwright install
```

### 4. Generate Report Tests
Untuk memunculkan report hasil semua test coverage, cukup jalankan perintah singkat ini di terminal:
```bash
pytest
```
Pytest akan secara otomatis membaca file pytest.ini.
Laporan hasil tes langsung ter-update di folder tests/reports/report.html.

## Hasil Test (Test Report)

Berikut adalah laporan hasil pengujian otomatis menggunakan Pytest HTML Reporter:
![Execution Report](/tests/reports/report-screenshot1.png)
![Execution Report](/tests/reports/report-screenshot2.png)
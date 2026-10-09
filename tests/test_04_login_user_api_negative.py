import os
import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.parametrize("username, password, expected_status", [
    ("emilys", "emilyspass1", 400),     # Password salah
    ("emilys1", "emilyspass", 400),     # Username salah
    ("", "emilyspass", 400),            # Email kosong
    ("emilys", "", 400),                # Password kosong
])

def test_client_login_negative(api_request_context: APIRequestContext, username: str, password: str, expected_status: int):
    payload = {
        "username": username,
        "password": password
    }

    # Ambil URL endpoint dari env atau gunakan path relatif
    login_url = os.getenv("LOGIN_URL")
    response = api_request_context.post(login_url, data=payload)

    # 1. Ambil response body (Gunakan try-except agar aman jika response bukan JSON)
    try:
        response_body = response.json()
        error_message = response_body.get("message", "Message key tidak ditemukan di JSON")
    except Exception:
        response_body = response.text()
        error_message = response_body

    # 2. Cetak Log Untuk Setiap Parameter
    print(f"\n==========================================")
    print(f"Testing Scenario : username='{username}' | password='{password}'")
    print(f"HTTP Status Code : {response.status}")
    print(f"Response Message : {error_message}")
    print(f"Full Body JSON   : {response_body}")
    print(f"==========================================")

    # 3. Assertion Status Code & Response Message
    assert response.status == expected_status, (
        f"\nFAILED: Status code tidak sesuai untuk username='{username}'"
        f"\nExpected Status : {expected_status}"
        f"\nActual Status   : {response.status}"
        f"\nResponse Body   : {response_body}"
    )

    # 4. Memastikan message di response body tidak kosong
    assert error_message is not None and error_message != "", "Response error message kosong!"
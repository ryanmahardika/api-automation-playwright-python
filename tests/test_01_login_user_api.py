import os
from playwright.sync_api import APIRequestContext

def test_client_login_success(api_request_context: APIRequestContext):
    # Payload diambil langsung dari .env lewat os.getenv
    payload = {
        "username": os.getenv("USER_USERNAME"),
        "password": os.getenv("USER_PASSWORD")
    }

    # Cukup panggil endpoint (/v1/client/login)
    response = api_request_context.post(os.getenv("LOGIN_URL"), data=payload)

    # Assert status code harus 200
    # Assert ok untuk memastikan request sukses (status code di rentang 200-299)
    assert response.status == 200
    assert response.ok
    
    response_body = response.json()
    print("\nResponse Body Login:\n", response_body)

# Assertion adalah "inti" dari QA Automation.
# Tanpa assertion, Anda tidak sedang melakukan testing, melainkan hanya menjalankan perintah (automation script).
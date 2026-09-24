import os
from typing import Generator
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Playwright, APIRequestContext

# Memuat file .env ke dalam memori
load_dotenv()

# Ambil data variabel env
BASE_URL = os.getenv("BASE_URL")
LOGIN_URL = os.getenv("LOGIN_URL")
USERNAME = os.getenv("USER_USERNAME")
PASSWORD = os.getenv("USER_PASSWORD")

# Buka Playwright Instance sekali untuk seluruh Session (secara global)
@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as p:
        yield p

# Context Tanpa Auth (Menggunakan playwright_instance)
@pytest.fixture(scope="session")
def api_request_context(playwright_instance: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright_instance.request.new_context(
        base_url=BASE_URL,
        timeout=10000
    )
    yield request_context
    request_context.dispose()

# Get Auth Token
@pytest.fixture(scope="session")
def auth_token(api_request_context: APIRequestContext) -> str:
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    
    response = api_request_context.post(LOGIN_URL, data=login_payload)
    assert response.status == 200, f"Gagal login di config. Status: {response.status}"

    response_body = response.json()

    # Ekstraksi token dengan beberapa fallback
    data_dict = response_body.get("data", {})
    token = (
        data_dict.get("token") or 
        data_dict.get("accessToken") or 
        response_body.get("token") or 
        response_body.get("accessToken")
    )
    assert token is not None, "Token tidak ditemukan pada response login"
    return token

# Context Dengan Auth (Menggunakan playwright_instance secara aman, TANPA with sync_playwright lagi)
@pytest.fixture(scope="session")
def authenticated_context(playwright_instance: Playwright, auth_token: str) -> Generator[APIRequestContext, None, None]:
    authed_context = playwright_instance.request.new_context(
        base_url=BASE_URL,
        timeout=10000,
        extra_http_headers={
            "Authorization": f"Bearer {auth_token}"
        }
    )
    yield authed_context
    authed_context.dispose()
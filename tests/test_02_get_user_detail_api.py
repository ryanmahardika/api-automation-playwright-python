import os
from playwright.sync_api import APIRequestContext
from urllib.parse import urlencode

def test_get_user_detail(authenticated_context: APIRequestContext):
    # Kirim GET Request ke endpoint user detail
    # Token 'Bearer <token>' otomatis terikut dari fungsi 'authenticated_context' pada config file
    response = authenticated_context.get(
        os.getenv("GET_USER_DETAIL"),
    )

    # Assert Status Code (Harus 200 OK)
    assert response.status == 200, f"Gagal mengambil data agents. Status Code: {response.status}"
    assert response.ok, "Response status is not OK"

    # Ambil dan validasi Response Body
    response_body = response.json()
    print("\nResponse Body Agents:\n", response_body)

    # Assertion Lanjutan (Contoh pengetesan isi data)
    # Memastikan response mengembalikan data (sesuaikan dengan struktur JSON asli API Anda)
    # Pastikan response_body berbentuk dictionary (bukan list atau tipe lain di root level)
    assert isinstance(response_body, dict), f"Response JSON harus berupa Object/Dict, tetapi menerima: {type(response_body)}"
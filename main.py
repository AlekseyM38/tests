import requests
import unittest

YANDEX_DISK_TOKEN = 'your_yandex_disk_token'

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):

        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {
            "Authorization": f"OAuth {YANDEX_DISK_TOKEN}"
        }
        # Создаем тестовую папку на Яндекс.Диске
        self.test_folder_name = "test_folder"
        requests.put(f"{self.base_url}/resources", params={"path": self.test_folder_name}, headers=self.headers)

    def tearDown(self):
        # Удаляем тестовую папку после выполнения тестов
        requests.delete(f"{self.base_url}/resources", params={"path": self.test_folder_name}, headers=self.headers)

    def test_create_folder_success(self):
        folder_name = "new_folder"
        response = requests.put(f"{self.base_url}/resources", params={"path": folder_name}, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_create_folder_failure(self):
        # Проверяем обработку ошибки при создании папки с некорректным именем
        invalid_folder_name = "invalid/folder"
        response = requests.put(f"{self.base_url}/resources", params={"path": invalid_folder_name}, headers=self.headers)
        self.assertNotEqual(response.status_code, 201)
        self.assertEqual(response.status_code, 409)

    def test_update_nonexistent_file_failure(self):

        nonexistent_file_name = "nonexistent_file.txt"
        response = requests.put(f"{self.base_url}/resources/upload", params={"path": nonexistent_file_name},
                                headers=self.headers)
        self.assertEqual(response.status_code, 403)

    def test_get_files_in_invalid_folder_failure(self):

        invalid_folder_name = "nonexistent_folder"
        response = requests.get(f"{self.base_url}/resources", params={"path": invalid_folder_name},
                                headers=self.headers)
        self.assertEqual(response.status_code, 403)

class TestYandexDiskAPI_1(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://yandex.ru"
        self.headers = {
            "Authorization": f"OAuth {YANDEX_DISK_TOKEN}"
        }

    def test_yandex_disk_access(self):
        response = requests.get(self.base_url, headers=self.headers)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

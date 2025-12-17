import pytest
import requests
import logging
import json
import allure
from datetime import datetime


@pytest.fixture(scope="session")
def browser_config_base_url():
    return "https://petstore.swagger.io/v2"


def attach_to_allure(request_data, response_data):
    if request_data:
        allure.attach(
            json.dumps(request_data, indent=2, ensure_ascii=False),
            name=f"REQUEST: {request_data.get('method')} {request_data.get('endpoint')}",
            attachment_type=allure.attachment_type.JSON
        )

    if response_data:
        allure.attach(
            json.dumps(response_data, indent=2, ensure_ascii=False),
            name=f"RESPONSE: {response_data.get('status_code')}",
            attachment_type=allure.attachment_type.JSON
        )


@pytest.fixture
def api_client(browser_config_base_url):

    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
            self.session.headers.update({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })

        def request(self, method, endpoint, **kwargs):
            full_url = f"{self.base_url}{endpoint}"

            # Request data for logging
            request_body = kwargs.get('json')
            request_data = {
                "method": method,
                "endpoint": endpoint,
                "url": full_url,
                "body": request_body,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            # Console logging: level, date, time, URL
            logger.info(f"[REQUEST] {method} {full_url}")

            try:
                response = self.session.request(method, full_url, **kwargs)

                # Response data for logging
                try:
                    response_body = response.json()
                except:
                    response_body = response.text

                response_data = {
                    "status_code": response.status_code,
                    "url": str(response.url),
                    "body": response_body,
                    "time": f"{response.elapsed.total_seconds():.3f}s"
                }

                # Console logging: level, date, time, status code
                logger.info(
                    f"[RESPONSE] {method} {full_url} - Status: {response.status_code} ({response_data['time']})")

                # Allure logging (request + response)
                attach_to_allure(request_data, response_data)

                return response

            except requests.RequestException as e:
                logger.error(f"[ERROR] {method} {full_url} - {str(e)}")
                raise

    return APIClient(browser_config_base_url)


@pytest.fixture
def petstore(api_client):

    class PetStoreAPI:
        def __init__(self, client):
            self.client = client

        def find_pets_by_status(self, status="available"):
            return self.client.request('GET', f'/pet/findByStatus?status={status}')

        def get_pet_by_id(self, pet_id):
            return self.client.request('GET', f'/pet/{pet_id}')

        def create_pet(self, pet_data):
            return self.client.request('POST', '/pet', json=pet_data)

        def delete_pet(self, pet_id):
            return self.client.request('DELETE', f'/pet/{pet_id}')

        def create_order(self, order_data):
            return self.client.request('POST', '/store/order', json=order_data)

    return PetStoreAPI(api_client)


# Configure console logging
logger = logging.getLogger("api_tests")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',  # level, date, time
        datefmt='Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
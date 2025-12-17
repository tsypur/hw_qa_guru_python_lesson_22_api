import allure
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.schemas import Pet


@allure.feature("GET Tests")
class TestGetMethods:

    @allure.title("GET /pet/findByStatus - find available pets")
    def test_find_available_pets(self, petstore):
        response = petstore.find_pets_by_status("available")

        # 1. Status code check
        assert response.status_code == 200

        # 2. Response value check
        data = response.json()
        assert isinstance(data, list)

        # 3. Response schema validation (if data exists)
        if data:
            Pet.parse_obj(data[0])

    @allure.title("GET /pet/{id} - get pet by ID")
    def test_get_pet_by_id(self, petstore):
        # Create test pet with validated request data
        pet_data = Pet.create_request(
            name="TestPet",
            photo_urls=["https://example.com/photo.jpg"],
            status="available"
        )

        create_resp = petstore.create_pet(pet_data)
        pet_id = create_resp.json()["id"]

        try:
            response = petstore.get_pet_by_id(pet_id)

            # 1. Status code check
            assert response.status_code == 200

            # 2. Response value check
            data = response.json()
            assert data["id"] == pet_id
            assert data["name"] == "TestPet"

            # 3. Response schema validation
            Pet.parse_obj(data)

        finally:
            # Cleanup
            petstore.delete_pet(pet_id)
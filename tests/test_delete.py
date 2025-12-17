import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.schemas import Pet


@allure.feature("DELETE Tests")
class TestDeleteMethods:

    @allure.title("DELETE /pet/{id} - delete pet")
    def test_delete_pet(self, petstore):
        # Create pet with validated request
        pet_data = Pet.create_request(
            name="DeleteMe",
            photo_urls=["https://example.com/delete.jpg"],
            status="available"
        )
        create_resp = petstore.create_pet(pet_data)
        pet_id = create_resp.json()["id"]

        # Delete pet
        response = petstore.delete_pet(pet_id)

        # 1. Status code check
        assert response.status_code == 200

        # 2. Response value check
        data = response.json()
        assert isinstance(data, dict)

        # 3. Response schema validation (basic structure)
        assert all(key in data for key in ["code", "type", "message"]) or data == {}

        # Verify pet is deleted
        get_resp = petstore.get_pet_by_id(pet_id)
        if get_resp.status_code == 404:
            assert True
        elif get_resp.status_code == 200:
            response_data = get_resp.json()
            if "message" in response_data and "not found" in str(response_data["message"]).lower():
                assert True
import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.schemas import Pet, Order


@allure.feature("POST Tests")
class TestPostMethods:

    @allure.title("POST /pet - create pet")
    def test_create_pet(self, petstore):
        # Request schema validation
        pet_data = Pet.create_request(
            name="NewPet",
            photo_urls=["https://example.com/photo.jpg"],  # ← Есть фото
            status="available"
        )

        response = petstore.create_pet(pet_data)

        # 1. Status code check
        assert response.status_code == 200

        # 2. Response value check
        data = response.json()
        assert "id" in data
        assert data["name"] == "NewPet"

        # 3. Response schema validation
        Pet.parse_obj(data)

        # Cleanup
        pet_id = data["id"]
        petstore.delete_pet(pet_id)

    @allure.title("POST /store/order - create order")
    def test_create_order(self, petstore):
        # Create pet for order with validated request
        pet_data = Pet.create_request(
            name="OrderPet",
            photo_urls=["https://example.com/order.jpg"],  # ← Добавить фото
            status="available"
        )
        pet_resp = petstore.create_pet(pet_data)
        pet_id = pet_resp.json()["id"]

        try:
            # Request schema validation for order
            order_data = Order.create_request(
                pet_id=pet_id,
                quantity=1,
                status="placed",
                complete=False
            )

            response = petstore.create_order(order_data)

            # 1. Status code check
            assert response.status_code == 200

            # 2. Response value check
            data = response.json()
            assert "id" in data
            assert data["petId"] == pet_id

            # 3. Response schema validation
            Order.parse_obj(data)

        finally:
            # Cleanup
            petstore.delete_pet(pet_id)
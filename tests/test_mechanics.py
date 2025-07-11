from app.models import Customer, Inventory, Mechanics, ServiceTickets, db
from app.utils.util import encode_token

from test_customer import SuperTest


class TestMechanics(SuperTest):
    def init_objects(self):
        self.mechanics1 = {
            "name": "ed",
            "email": "ed@repairshop.com",
            "phone": "9719719711",
            "password": "test1",
            "salary": 199999.34,
        }

        self.updated_mechanics1 = {
            "name": "ed",  # changed to uppercase
            "email": "",
            "phone": "9289289280",  # changed phone number
            "password": "",
            "salary": 0,
        }

        self.mechanics2 = {
            "name": "edd",
            "email": "edd@repairshop.com",
            "phone": "5035035033",
            "password": "test2",
            "salary": 2.00,
        }

        self.customer1 = {
            "name": "kyle",
            "email": "kyle@gmail.com",
            "phone": "0123456789",
            "password": "test",
        }

        with self.app.app_context():
            # convert customer1 to Customer object to enter into database
            customer1_obj = Customer(**self.customer1)
            mechanics1_obj = Mechanics(**self.mechanics1)
            db.session.add(customer1_obj)
            db.session.add(mechanics1_obj)
            db.session.commit()
        self.token1 = encode_token(1)
        self.mechanic_token1 = encode_token(1, role="mechanic")
        self.client = self.app.test_client()

    # =============== UNPROTECTED - BUT LIMITED ============================
    def test_create_mechanics(self):
        mechanics_payload = self.mechanics2
        response = self.client.post("/mechanicss/", json=mechanics_payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], mechanics_payload["name"])

    def test_existing_create_mechanics(self):
        mechanics_payload = self.mechanics1
        response = self.client.post("/mechanics/", json=mechanics_payload)

        self.assertEqual(response.status_code, 401)
        self.assertIn("already", response.json["error"])

    def test_mechanics_login(self):
        login_payload = {
            "email": self.mechanics1["email"],
            "password": self.mechanics1["password"],
        }
        response = self.client.post("/mechanics/login", json=login_payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "success")

    def test_invalid_mechanics_creation(self):
        # payload missing email field
        incomplete_payload = {
            "name": "kyle",
            "phone": "1234567890",
            "password": "test",
        }
        response = self.client.post("/mechanics/", json=incomplete_payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn("all mechanic data required", response.json["message"])

    def test_invalid_mechanics_login(self):
        login_payload = {
            "email": self.mechanics1["email"],
        }
        response = self.client.post("/mechanics/login", json=login_payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Username and password required.")

    # =================== MECHANICS TOKEN PROTECTED ===========================
    # def test_update_mechanics(self):
    #     updated_payload = {
    #         "name": "ed",  # changed to uppercase
    #         "email": "",  # blank strings falsy and aren't reassigned
    #         "phone": "9876543210",  # changed phone number
    #         "password": "",
    #         "salary": 0
    #     }

    #     mechanics1_header = {"Authorization": "Bearer " + self.token1}

    #     response = self.client.put(
    #         "/mechanicss/",
    #         json=updated_payload,
    #         headers=mechanics1_header,
    #     )

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json["name"], self.updated_mechanics1["name"])
    #     self.assertEqual(response.json["phone"], "9876543210")

    # def test_invalid_update_mechanics(self):
    #     # missing email field
    #     incomplete_payload = {
    #         "name": "Kyle",
    #         "phone": "9876543210",
    #         "password": "",
    #     }

    #     mechanics1_header = {"Authorization": "Bearer " + self.token1}

    #     response = self.client.put(
    #         "/mechanicss/", json=incomplete_payload, headers=mechanics1_header
    #     )

    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("all mechanics data fields required.", response.json["message"])

    # def test_delete_mechanics(self):
    #     mechanics2_obj = Mechanics(**self.mechanics2)
    #     with self.app.app_context():
    #         db.session.add(mechanics2_obj)
    #         db.session.commit()

    #     token2 = encode_token(2)
    #     mechanics2_header = {"Authorization": "Bearer " + token2}

    #     response = self.client.delete("/mechanicss/", headers=mechanics2_header)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.json["message"], "Mechanics successfully marked for deletion"
    #     )

    # def test_get_mechanics(self):
    #     mechanics2_obj = Mechanics(**self.mechanics2)
    #     with self.app.app_context():
    #         db.session.add(mechanics2_obj)
    #         db.session.commit()

    #     token2 = encode_token(2)
    #     mechanics2_header = {"Authorization": "Bearer " + token2}

    #     response = self.client.get("/mechanicss/my-account", headers=mechanics2_header)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json["name"], "rev")

    # # ========================= MECHANIC TOKEN PROTECTED ==============================
    # def test_mechanic_get_all_mechanicss(self):
    #     mechanics2_obj = Mechanics(**self.mechanics2)
    #     with self.app.app_context():
    #         db.session.add(mechanics2_obj)
    #         db.session.commit()
    #     mechanic1_header = {"Authorization": "Bearer " + self.mechanic_token1}

    #     response = self.client.get("/mechanicss/", headers=mechanic1_header)

    #     # remove password and add id and soft_delete fields to match mechanic_view_mechanicss_schema output
    #     del self.mechanics1["password"]
    #     self.mechanics1["id"] = 1
    #     self.mechanics1["soft_delete"] = False

    #     del self.mechanics2["password"]
    #     self.mechanics2["id"] = 2
    #     self.mechanics2["soft_delete"] = False

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.mechanics1, dict(response.json[0]))
    #     self.assertEqual(self.mechanics2, dict(response.json[1]))

    # def test_mechanic_get_all_mechanicss_paginated(self):
    #     mechanics2_obj = Mechanics(**self.mechanics2)
    #     with self.app.app_context():
    #         db.session.add(mechanics2_obj)
    #         db.session.commit()
    #     mechanic1_header = {"Authorization": "Bearer " + self.mechanic_token1}

    #     # paginated to view mechanicss 1 at a time, only page 2
    #     response = self.client.get(
    #         "/mechanicss/?page=2&per_page=1", headers=mechanic1_header
    #     )

    #     # remove password and add id and soft_delete fields to match mechanic_view_mechanicss_schema output
    #     del self.mechanics2["password"]
    #     self.mechanics2["id"] = 2
    #     self.mechanics2["soft_delete"] = False

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.mechanics2, dict(response.json[0]))

    # # def test_mechanic_get_mechanics
    # def test_mechanic_get_mechanics_by_id(self):
    #     mechanic1_header = {"Authorization": "Bearer " + self.mechanic_token1}

    #     response = self.client.get("/mechanicss/1", headers=mechanic1_header)

    #     # remove password and add id and soft_delete fields to match mechanic_view_mechanics_schema output
    #     del self.mechanics1["password"]
    #     self.mechanics1["id"] = 1
    #     self.mechanics1["soft_delete"] = False

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(dict(response.json), self.mechanics1)

import unittest
import logging
from requests import request
from secrets import compare_digest

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class TestApi(unittest.TestCase):
    def setUp(self):
        self.create_url = "http://127.0.0.1:8000/api/v1/event/create/"
        self.all_url = "http://127.0.0.1:8000/api/v1/event/all/"
        self.detail_url = "http://127.0.0.1:8000/api/v1/event/detail/1/"
        self.__token_admin = '9679cda006cd8e63352c7a0e466c70939a7769d0'
        self.__token_user = '612bcfeaef41556a7c04d0ec2c68c0739fb5770b'
        self.payload = "{\n    \"info\": {\"test\": \"create\"},\n    \"timestamp\": \"2021-03-11T15:01:28.250723Z\"," \
                       "\n    \"event_type\": 1\n} "
        self.payload_to_update = "{\n    \"'id\": 1,\n    \"info\": {\"test\": \"update\"},\n    \"timestamp\": " \
                                 "\"2021-03-11T15:01:28.250723Z\"," \
                                 "\n    \"event_type\": 1\n} "

    # CREATE PART
    def test_create_post_by_admin(self):
        response = request("POST", self.create_url, headers=header(self.__token_admin), data=self.payload)
        self.assertEqual(response.status_code, 201)

    def test_create_post_auth_user(self):
        response = request("POST", self.create_url, headers=header(self.__token_user), data=self.payload)
        self.assertEqual(response.status_code, 201)

    def test_create_post_guest(self):
        response = request("POST", self.create_url, headers=header(), data=self.payload)
        self.assertEqual(response.status_code, 401)
    # # END CREATE PART

    # # UPDATE PART
    def test_update_post_by_admin(self):
        response = request("PUT", self.detail_url, headers=header(self.__token_admin), data=self.payload_to_update)
        self.assertEqual(response.status_code, 200)

    def test_update_post_auth_user(self):
        response = request("PUT", self.detail_url, headers=header(self.__token_user), data=self.payload_to_update)
        self.assertEqual(response.status_code, 200)

    def test_update_post_guest(self):
        response = request("PUT", self.detail_url, headers=header(), data=self.payload_to_update)
        self.assertEqual(response.status_code, 401)
    # END UPDATE PART


def header(token='guest'):
    if compare_digest(token, 'guest'):
        return {'Content-Type': 'application/json'}
    return {'Authorization': f"Token {token}", 'Content-Type': 'application/json'}


if __name__ == '__main__':
    unittest.main()

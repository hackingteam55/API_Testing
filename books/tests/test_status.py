from books.requests.status import *


class TestStatus:

    def test_status_200(self):
        assert get_status().status_code == 200, 'status code is not ok'
        assert get_status().json()['status'] == 'OK', 'status message is incorrect'

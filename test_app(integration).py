from flask_testing import TestCase # type: ignore
from app import app  # Import your Flask app

class TestIntegration(TestCase):
    def create_app(self):
        return app  

    def test_get_person_by_id(self):
        response = self.client.get('/test')  
        self.assertEqual(response.status_code, 200)  
        
import unittest
from app import app, people

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        people.clear()

    def test_add_person(self):
        response = self.app.post('/add_person', data=dict(name='John', age='30'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)
        self.assertIn(b'30', response.data)
        self.assertEqual(len(people), 1)
        self.assertEqual(people[0]['name'], 'John')
        self.assertEqual(people[0]['age'], '30')

    def test_view_people(self):
        people.append({'name': 'Jane', 'age': '25'})
        response = self.app.get('/view_people')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane', response.data)
        self.assertIn(b'25', response.data)

if __name__ == '__main__':
    unittest.main()

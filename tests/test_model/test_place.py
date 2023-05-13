import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    def test_attributes(self):
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

        c = City()
        c.save()
        u = User()
        u.save()
        a = Amenity()
        a.save()

        p.city_id = c.id
        p.user_id = u.id
        p.name = "Test Place"
        p.description = "This is a test place."
        p.number_rooms = 2
        p.number_bathrooms = 1
        p.max_guest = 4
        p.price_by_night = 100
        p.latitude = 37.7749
        p.longitude = -122.4194
        p.amenity_ids = [a.id]

        self.assertEqual(p.city_id, c.id)
        self.assertEqual(p.user_id, u.id)
        self.assertEqual(p.name, "Test Place")
        self.assertEqual(p.description, "This is a test place.")
        self.assertEqual(p.number_rooms, 2)
        self.assertEqual(p.number_bathrooms, 1)
        self.assertEqual(p.max_guest, 4)
        self.assertEqual(p.price_by_night, 100)
        self.assertEqual(p.latitude, 37.7749)
        self.assertEqual(p.longitude, -122.4194)
        self.assertEqual(p.amenity_ids, [a.id])

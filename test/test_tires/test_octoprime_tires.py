import unittest


from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear = [0.9,0.9,0.9,0.9]
        tires = OctoprimeTires(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear = [0.1,0.2,0.1,0.3]
        tires = OctoprimeTires(tires_wear)
        self.assertFalse(tires.needs_service())

   
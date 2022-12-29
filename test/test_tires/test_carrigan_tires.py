import unittest


from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear = [0.9,0.8,0.5,0.3]
        tires = CarriganTires(tires_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear = [0.1,0.2,0.5,0.3]
        tires = CarriganTires(tires_wear)
        self.assertFalse(tires.needs_service())

   
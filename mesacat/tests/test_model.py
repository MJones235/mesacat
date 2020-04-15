from mesacat.model import EvacuationModel
from unittest import TestCase


class TestEvacuationModel(TestCase):

    def test_create_movie(self):

        model = EvacuationModel(10, 'sample_data/bwaise.osm', seed=1)

        model.create_movie('model.mp4', steps=100)
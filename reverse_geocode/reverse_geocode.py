import typing

from . import utils
from . import resources
from . import vendored


class Geocode(metaclass=utils.Singleton):
    _instance = None

    def __init__(self,
                 sources: [resources.resource.Resource] = [
            resources.geonames.Geonames(),
            resources.countries.Countries()]):
        self.sources = vendored.setutils.IndexedSet(sources)

        for source in sources:
            source.load()

    def query(self, coordinates):
        """Find closest match to this list of coordinates."""
        results = []

        for coordinate_pair in coordinates:
            result = {}

            for source in self.sources:
                result = source.query(coordinate_pair, result)

            results.append(result)

        return results


def search(*coordinates):
    geocode_data = Geocode()

    return geocode_data.query(coordinates)

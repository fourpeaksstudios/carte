import csv
import dataclasses

from . import resource


@dataclasses.dataclass
class Countries(resource.Resource):
    resource_filename = "countries.csv"

    def __hash__(self):
        return super().__hash__()

    def load(self):
        "Load a map of country code to name"
        self.countries = {}
        for code, country in csv.reader(open(self.fetch_resource_data())):
            self.countries[code] = country

    def query(self, coordinates, result) -> dict:
        result.update(
            {"country": self.countries.get(result["country_code"], "")})

        return result

import dataclasses
import logging
import os

import appdirs

import reverse_geocode.config
import reverse_geocode.utils


@dataclasses.dataclass
class Resource(object):
    def __init__(self, resource_filename, url):
        self.resource_filename = resource_filename
        self.url = url
        self.logs = logging.getLogger(__name__)

    def __hash__(self):
        return hash(repr(self))

    def fetch_resource_data(self) -> str:
        data_dir_path = appdirs.user_data_dir(
            reverse_geocode.config.APP_NAME)

        if not os.path.exists(data_dir_path):
            os.makedirs(data_dir_path)

        resource_path = os.path.join(data_dir_path, self.resource_filename)

        if not os.path.exists(resource_path):
            raw_resource_data = reverse_geocode.utils.download_resource(
                self.url)

            self.save_resource_data(raw_resource_data, resource_path)

        return resource_path

    def save_resource_data(self, resource_data, resource_data_path):
        with open(resource_data_path, "w") as f:
            f.write(resource_data)

    def load(self):
        pass

    def query(self, coordinates, result) -> dict:
        pass

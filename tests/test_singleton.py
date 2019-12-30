import logging
import os

import reverse_geocode

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler = logging.FileHandler(
    os.path.join(os.pardir, __name__)
)
logs = logging.getLogger(__name__)

handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logs.addHandler(handler)


def locate():
    return reverse_geocode.search((-37.81, 144.96))


def test_answer():
    assert locate() == [{'country_code': 'AU', 'city': 'Melbourne',
                         'admin1': 'Victoria', 'admin2': 'Melbourne',
                         'country': 'Australia'}]

import carte


def locate():
    return carte.search((-37.81, 144.96))


def test_answer():
    assert locate() == [
        {
            "country_code": "AU",
            "city": "Melbourne",
            "admin1": "Victoria",
            "admin2": "Melbourne",
            "country": "Australia",
        }
    ]

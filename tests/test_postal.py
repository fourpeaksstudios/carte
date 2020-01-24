import carte
import carte.resources


def locate():
    carte_instance = carte.Carte(
        carte.resources.postal_codes.PostalCodesUS,
        carte.resources.countries.Countries,
    )

    return carte_instance.query((32.847, -117.274))


def test_answer():
    assert locate() == [
        {
            "city": "La Jolla",
            "admin1": "San Diego",
            "admin2": "California",
            "postal_code": "92038",
            "country_code": "US",
            "country": "United States",
        }
    ]

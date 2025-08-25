from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]
    def test_cities_spain() -> None:
        """
        Test the /countries/Spain/cities endpoint to ensure it returns the correct list of cities for Spain.

        Verifies:
        - The response status code is 200.
        - The returned data is a list.
        - The list contains only the expected cities (edge case: only 'Seville' exists).
        """
        response = client.get("/countries/Spain/cities")
        assert response.status_code == 200
        cities = response.json()
        assert isinstance(cities, list)
        # Edge case: Only 'Seville' should be present
        assert cities == ["Seville"]

    def test_cities_invalid_country() -> None:
        """
        Test the /countries/{country}/cities endpoint with an invalid country.

        Verifies:
        - The response status code is 200.
        - The returned data contains an error message.
        """
        response = client.get("/countries/Narnia/cities")
        assert response.status_code == 200
        result = response.json()
        assert "error" in result
        assert result["error"] == "Country 'Narnia' not found."

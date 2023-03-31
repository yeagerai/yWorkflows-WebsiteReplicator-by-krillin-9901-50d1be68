
import pytest
from pydantic import BaseModel
from typing import List
from core.abstract_component import AbstractComponent

from fastapi.testclient import TestClient
from your_module import FetchTechnologies, FetchTechnologiesInputDict, FetchTechnologiesOutputDict, fetch_technologies_app

client = TestClient(fetch_technologies_app)

class MockResponse:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]


@pytest.fixture
def mock_builtwith(mocker):
    mocker.patch("your_module.builtwith")


@pytest.mark.parametrize(
    "input_data, expected_output_data",
    [
        (
            {"target_website": "https://example.com"},
            {"technologies": ["Python", "Django"]}
        ),
        (
            {"target_website": "https://another-example.com"},
            {"technologies": ["Node.js", "Express"]}
        )
    ],
)
def test_transform(mock_builtwith, input_data, expected_output_data):
    mocked_response_data = MockResponse({**expected_output_data, "other_key": "other_value"})
    mock_builtwith.parse.return_value = mocked_response_data

    response = client.post("/transform/", json=input_data)
    assert response.status_code == 200
    assert response.json() == expected_output_data

    mock_builtwith.parse.assert_called_with(**input_data)


@pytest.mark.parametrize(
    "input_data",
    [
        {"target_website": "not-a-url"},
        {"target_website": ""},
    ],
)
def test_transform_invalid_input(mock_builtwith, input_data):
    response = client.post("/transform/", json=input_data)

    # Note: Replace 400 with an appropriate error code if the component's transform method raises a
    # specific exception or has custom error handling for invalid input.
    assert response.status_code == 400
    assert "technologies" not in response.json()

    mock_builtwith.parse.assert_not_called()

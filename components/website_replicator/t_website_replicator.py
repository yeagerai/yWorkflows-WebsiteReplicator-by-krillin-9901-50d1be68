
import pytest
from pydantic import BaseModel
from typing import Optional
from core.workflows.abstract_workflow import AbstractWorkflow
from .your_fastapi_module import WebsiteReplicator, WebsiteReplicatorIn, WebsiteReplicatorOut

# Define test cases with mocked input and expected output data
test_data = [
    (
        WebsiteReplicatorIn(target_website="https://target.example.com"),
        WebsiteReplicatorOut(
            replica_url="https://example.com/replica",
            replica_status="Completed"
        )
    ),
    (
        WebsiteReplicatorIn(target_website="https://another-target.example.com"),
        WebsiteReplicatorOut(
            replica_url="https://example.com/replica",
            replica_status="Completed"
        )
    ),
]

# Error handling and edge case scenarios
error_data = [
    WebsiteReplicatorIn(target_website="invalid_url"),  # Invalid URL
    WebsiteReplicatorIn(target_website=""),  # Empty string
    None,  # None value
]

@pytest.mark.parametrize("input_data,expected_output", test_data)
async def test_website_replicator(input_data: WebsiteReplicatorIn, expected_output: WebsiteReplicatorOut) -> None:
    # Call the component's transform() method
    website_replicator = WebsiteReplicator()
    result = await website_replicator.transform(input_data, callbacks=None)

    # Assert that the output matches the expected output
    assert result == expected_output

@pytest.mark.parametrize("input_data", error_data)
async def test_website_replicator_errors(input_data: Optional[WebsiteReplicatorIn]) -> None:
    website_replicator = WebsiteReplicator()

    # Test error handling and edge cases
    with pytest.raises(Exception):
        await website_replicator.transform(input_data, callbacks=None)

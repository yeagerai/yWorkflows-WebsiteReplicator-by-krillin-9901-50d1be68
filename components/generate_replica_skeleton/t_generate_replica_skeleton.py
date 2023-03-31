
import os
import yaml
import pytest
from typing import List
from fastapi.testclient import TestClient
from pydantic import BaseModel

from core.abstract_component import AbstractComponent
from components.GenerateReplicaSkeleton import (
    GenerateReplicaSkeleton,
    GenerateReplicaSkeletonInputDict,
    GenerateReplicaSkeletonOutputDict,
)

# Test cases with mocked input and expected output data
test_cases = [
    (
        ["react", "nodejs"],
        "http://example.com/skeleton_url",
    ),
    (
        ["angular", "django"],
        "http://example.com/skeleton_url",
    ),
    (
        [],
        "http://example.com/skeleton_url",
    ),
]

# Using @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("technologies, expected_skeleton_url", test_cases)
def test_generate_replica_skeleton(technologies: List[str], expected_skeleton_url: str):
    """
    Test function that takes the mocked input, calls the component's transform() method, and 
    asserts that the output matches the expected output.
    """
    # Instantiate the component
    gen_replica_skeleton = GenerateReplicaSkeleton()
    
    # Create the input data object
    input_data = GenerateReplicaSkeletonInputDict(technologies=technologies)
    
    # Call the component's transform() method
    output_data = gen_replica_skeleton.transform(input_data)
    
    # Assertions
    assert isinstance(output_data, GenerateReplicaSkeletonOutputDict)
    assert output_data.skeleton_url == expected_skeleton_url

# Optional: Write error handling and edge case scenarios
def test_generate_replica_skeleton_with_invalid_technologies():
    # Instantiate the component
    gen_replica_skeleton = GenerateReplicaSkeleton()
    
    # Create the input data object with an invalid value for technologies
    input_data = GenerateReplicaSkeletonInputDict(technologies=["invalid"])
    
    with pytest.raises(Exception):
        gen_replica_skeleton.transform(input_data)

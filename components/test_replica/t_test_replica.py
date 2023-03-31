
# Imports
import pytest
from pydantic import ValidationError
from core.test_replica import TestReplica, TestReplicaInputDict, TestReplicaOutputDict

# Test cases with mocked input and expected output data
test_data = [
    (
        TestReplicaInputDict(skeleton_url="https://example1.com/skeleton"),
        TestReplicaOutputDict(replica_url="https://example1.com/skeleton", replica_status="Success"),
    ),
    (
        TestReplicaInputDict(skeleton_url="https://example2.com/skeleton"),
        TestReplicaOutputDict(replica_url="https://example2.com/skeleton", replica_status="Success"),
    ),
    (
        TestReplicaInputDict(skeleton_url="https://example3.com/skeleton"),
        TestReplicaOutputDict(replica_url="https://example3.com/skeleton", replica_status="Success"),
    ),
]

# Parameterized test function
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_test_replica_transform(input_data: TestReplicaInputDict, expected_output: TestReplicaOutputDict):
    test_replica = TestReplica()
    output = test_replica.transform(input_data)

    assert output == expected_output

# Example of a test for an edge case scenario
def test_test_replica_invalid_url():
    with pytest.raises(ValidationError):
        TestReplicaInputDict(skeleton_url="invalid_url")

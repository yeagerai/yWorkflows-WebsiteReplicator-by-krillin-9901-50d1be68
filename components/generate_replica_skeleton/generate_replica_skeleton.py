
import os
import yaml
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class GenerateReplicaSkeletonInputDict(BaseModel):
    technologies: List[str]


class GenerateReplicaSkeletonOutputDict(BaseModel):
    skeleton_url: str


class GenerateReplicaSkeleton(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.skeleton_templates_path: str = yaml_data["parameters"]["skeleton_templates_path"]

    def transform(
        self, args: GenerateReplicaSkeletonInputDict
    ) -> GenerateReplicaSkeletonOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Load the skeleton templates path from the configuration file
        templates_path = self.skeleton_templates_path

        # Iterate through the technologies list
        for technology in args.technologies:
            # Find a matching template in the skeleton_templates_path
            # Merge the templates to generate a combined replica skeleton
            # Initialize the development environment using the generated skeleton
            pass

        # Generate a temporary URL for the generated replica skeleton
        skeleton_url = "http://example.com/skeleton_url"

        # Output skeleton_url as the URL of the generated replica skeleton
        out = GenerateReplicaSkeletonOutputDict(skeleton_url=skeleton_url)
        return out


gen_replica_skeleton_app = FastAPI()


@gen_replica_skeleton_app.post("/transform/")
async def transform(
    args: GenerateReplicaSkeletonInputDict,
) -> GenerateReplicaSkeletonOutputDict:
    gen_replica_skeleton = GenerateReplicaSkeleton()
    return gen_replica_skeleton.transform(args)


import os
from typing import List

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import builtwith

from core.abstract_component import AbstractComponent


class FetchTechnologiesInputDict(BaseModel):
    target_website: str


class FetchTechnologiesOutputDict(BaseModel):
    technologies: List[str]


class FetchTechnologies(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["api_key"]
        )

    def transform(
        self, args: FetchTechnologiesInputDict
    ) -> FetchTechnologiesOutputDict:
        builtwith.api_key = self.api_key
        print(f"Executing the transform of the {type(self).__name__} component...")

        response = builtwith.parse(args.target_website)
        technologies = response["technologies"]

        out = FetchTechnologiesOutputDict(
            technologies=technologies
        )
        return out


load_dotenv()
fetch_technologies_app = FastAPI()


@fetch_technologies_app.post("/transform/")
async def transform(
    args: FetchTechnologiesInputDict,
) -> FetchTechnologiesOutputDict:
    fetch_technologies = FetchTechnologies()
    return fetch_technologies.transform(args)

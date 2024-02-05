from datetime import datetime

from pydantic import BaseModel
from pydantic_settings.main import ConfigDict

from src.utils.formatter import fmt


class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
        json_encoders={datetime: fmt.datetime_to_isoformat},
        alias_generator=fmt.snake_to_camel,
    )

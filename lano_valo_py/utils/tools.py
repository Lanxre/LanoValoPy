from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def convert_model(
    source: BaseModel, target_model: Type[T], exclude_none: bool = True, **extra_kwargs
) -> T:
    """
    Convert one Pydantic model to another, optionally skipping None values

    Args:
        source: Source model to convert from
        target_model: Target model class to convert to
        exclude_none: Whether to exclude None values
        extra_kwargs: Additional fields to include in the target model

    Returns:
        Instance of the target model
    """
    source_dict = source.model_dump(exclude_none=exclude_none)
    source_dict.update(extra_kwargs)
    return target_model(**source_dict)

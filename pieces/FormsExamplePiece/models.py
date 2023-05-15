from pydantic import BaseModel, Field
from enum import Enum


class EnumType(str, Enum):
    key_1 = "value_1"
    key_2 = "value_2"


class InputModel(BaseModel):
    enum_value: EnumType = Field(
        description="Example of enum input"
    )
    float_value: float = Field(
        description="Example of float input"
    )
    int_value: int = Field(
        description="Example of int input"
    )
    string_value: str = Field(
        description="Example of string input"
    )
    boolean_value: bool = Field(
        description="Example of boolean input"
    )


class OutputModel(BaseModel):
    enum_output: EnumType = Field(
        description="Example of enum output"
    )
    float_output: float = Field(
        description="Example of float output"
    )
    int_output: int = Field(
        description="Example of int output"
    )
    string_output: str = Field(
        description="Example of string output"
    )
    boolean_output: bool = Field(
        description="Example of boolean output"
    )


class SecretsModel(BaseModel):
    enum_secret: EnumType = Field(
        description="Example of enum secret"
    )
    float_secret: float = Field(
        description="Example of float secret"
    )
    int_secret: int = Field(
        description="Example of int secret"
    )
    string_secret: str = Field(
        description="Example of string secret"
    )
    boolean_secret: bool = Field(
        description="Example of boolean secret"
    )
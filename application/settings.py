import json
from io import StringIO
from optparse import Option
from typing_extensions import TypedDict

from dataclasses import dataclass
from typing import List, Optional
from xmlrpc.client import Boolean
from dacite import from_dict
from dacite.exceptions import MissingValueError
    
@dataclass
class Options:
    x_column: str
    y_column: str

@dataclass
class threshold:
    lower: float
    upper: float

@dataclass
class CurveConfig:
    name: str
    options: Options
    remove_mean: Optional[bool] = None
    threshold: Optional[threshold] = None

@dataclass
class ConfigData:
    data: List[CurveConfig]

@dataclass
class Settings:
    data: ConfigData = None

    def load_config(self) -> ConfigData:
        try:
            with open('config.json') as config_file:
                raw_data = json.load(config_file)
                str_data: ConfigData = raw_data
                self.data = from_dict(data_class=ConfigData, data=str_data)
                return self.data
        except MissingValueError as ex:
            print(ex)
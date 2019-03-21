from .readonly_store import *
# Internal
from src.common.decorators import override
from src.common.project_paths import pathToConfig
# Python
import os, yaml


class ConfigFile(ReadOnlyStore):

    @override
    @private
    def getParameters(self) -> dict:

        try:
            with open(os.path.join(pathToConfig, 'event_registry.conf'), 'r') as config:

                data = yaml.load(config)
                return data

        except FileNotFoundError:

            defaultConfig = {'ip': '127.0.0.1', 'port': 4567, 'pathToDatabase': '/tmp/pilotb_server'}
            return defaultConfig

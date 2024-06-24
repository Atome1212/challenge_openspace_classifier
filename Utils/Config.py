import json
import os
import copy

class Config:
    """
    This class wil charge Config.json.
    """

    def __init__(self, link: str='./Data/config.json'):
        """
        Constructor of the class Config.py

        Parameters
        ----------
        link : str
            link of the config.
        """
        self.link = link  # the link of config.json
        self.config = {}

    def loadOrCreateConfig(self):
        default_config = {
            "nbCapacity": 24,
            "capacity": 4,
            "limitTable" : 6
        }
        
        if os.path.exists(self.link):
            with open(self.link, 'r') as file:
                config = json.load(file)
        else:
            with open(self.link, 'w') as file:
                json.dump(default_config, file, indent=4)
            config = default_config
        
        self.config = config

    @property
    def getConfig(self) -> dict:
        return copy.deepcopy(self.config)
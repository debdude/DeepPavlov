from typing import List, Dict

from deeppavlov.core.models.inferable import Inferable


# TODO Create this class dynamically?
class Agent(Inferable):
    def __init__(self, skill_configs: List[Dict], commutator_config: Dict):
        self.skill_configs = skill_configs
        self.commutator_config = commutator_config
        self.history = []

    def infer(self):
        pass

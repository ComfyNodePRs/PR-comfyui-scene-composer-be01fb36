from ..scene.component import Component
from ..composition.composition import Composition
from ..action.action import Action
from ..subject.character import Character
from ..environment.environment import Environment


class Scene(Component):
    def __init__(self, seed=None):
        super().__init__(seed)

        self.components = {
            'composition': Composition(self.seed),
            'action': Action(self.seed),
            'subject': Character(self.seed),
            'environment': Environment(self.seed)
        }

    def define_action(self, action_type):
        self.components['action'] = Action(self.seed, action_type)

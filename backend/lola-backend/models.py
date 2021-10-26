import os

from joblib import load as j_load
from tensorflow_hub import load


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)

        return cls._instances[cls]


class SingletonModels(metaclass=Singleton):
    def __init__(self) -> None:
        self.vgg = load("https://tfhub.dev/google/vggish/1")
        self.random_forest = j_load(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "../assets/models/random_forest.joblib",
                )
            )
        )

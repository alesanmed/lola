from typing import Dict, Type

from .classes import Page
from .data_exploration import DataExploration
from .index import IdentifyAudio
from .models_evaluation import ModelsEvaluation

PAGES: Dict[str, Type[Page]] = {
    "Identify your audio": IdentifyAudio,
    "Data Exploration": DataExploration,
    "Model Evaluation": ModelsEvaluation,
}

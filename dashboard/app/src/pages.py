from typing import Dict, Type

from .classes import Page
from .data_exploration import DataExploration
from .models_evaluation import ModelsEvaluation

PAGES: Dict[str, Type[Page]] = {
    "Data Exploration": DataExploration,
    "Model Evaluation": ModelsEvaluation,
}

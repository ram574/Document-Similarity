from enum import Enum
import nltk

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


class Split(str, Enum):
    TRAIN: str = "train"
    DEV: str = "dev"
    TEST: str = "test"

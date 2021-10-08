from typing import Tuple


class AudioSource:
    """
    Base class for audio source.
    It's an iterator that obtains audios from whatever source and returns its path
    """

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[str, int]:
        raise RuntimeError("Not Implemented")

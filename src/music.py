"""Holds all music-related operations."""
import os
import random
from itertools import count

import sox

from audio_sources import AudioSource
from audio_sources.youtube import YoutubeAudioSource


class AudioProcessor:
    """
    Audio processor for getting the downloaded files and trimming them
    into random samples of 30 seconds
    """

    def __init__(self, source: AudioSource, count_start: int = 0) -> None:
        self.source = source
        self.counter = count(count_start)

    def process_audios(self):
        """
        Begins the audio processing in each file provided by the audio source
        """
        for audio_path, duration in self.source:
            self.split_audio(audio_path, duration)

            os.remove(audio_path)

    def split_audio(self, audio_path: str, duration: int):
        """
        Aux function for splitting an audio file in random samples of 30 seconds
        """
        splits = duration // 120

        for i in range(splits + 1):
            start = 120 * i
            end = start + 120

            if end > duration:
                end = duration

            if end - start < 30:
                print("Not long enough")
                continue

            print(start, end)

            sample_start = random.randint(start, end - 30)

            tfm = sox.Transformer()

            tfm.trim(sample_start, sample_start + 30)

            tfm.fade(0.3, 0.3)

            tfm.build_file(
                audio_path, f"{os.path.dirname(audio_path)}/{next(self.counter)}.wav"
            )


if __name__ == "__main__":
    source = YoutubeAudioSource(
        ["https://www.youtube.com/watch?v=0PB7KesvhIw"], "bulerias"
    )

    processor = AudioProcessor(source)

    processor.process_audios()

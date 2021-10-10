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
        audio_ext = audio_path.split(".")[-1]

        for i in range(splits + 1):
            start = 120 * i
            end = start + 120

            if end > duration:
                end = duration

            sample_length = random.randint(30, 50)

            if end - start < sample_length:
                print("Not long enough")
                continue

            sample_start = random.randint(start, end - sample_length)

            tfm = sox.Transformer()

            tfm.trim(sample_start, sample_start + sample_length)

            tfm.fade(0.3, 0.3)

            tfm.build_file(
                audio_path,
                f"{os.path.dirname(audio_path)}/{next(self.counter)}.{audio_ext}",
            )


if __name__ == "__main__":
    source_bulerias = YoutubeAudioSource(
        [
            "https://www.youtube.com/watch?v=0PB7KesvhIw",
            "https://www.youtube.com/watch?v=QUQeRZsK39Q",
            "https://www.youtube.com/watch?v=T06qedkgfbA",
            "https://www.youtube.com/watch?v=pWRZXgU7JaI",
            "https://www.youtube.com/watch?v=4sEwogXClIQ",
            "https://www.youtube.com/watch?v=nTTc4YNePqo",
            "https://www.youtube.com/watch?v=97_tZaXegng",
            "https://www.youtube.com/watch?v=ivaWkiBl8J4",
            "https://www.youtube.com/watch?v=IyaW4Llr-dM",
            "https://www.youtube.com/watch?v=nbyvYhkXahw",
            "https://www.youtube.com/watch?v=zmO4ra2VKGA",
        ],
        "bulerias",
    )

    processor_bulerias = AudioProcessor(source_bulerias)

    processor_bulerias.process_audios()

    source_alegrias = YoutubeAudioSource(
        [
            "https://www.youtube.com/watch?v=hGiW7uD55zs",
            "https://www.youtube.com/watch?v=mZiJaAcOE5U",
            "https://www.youtube.com/watch?v=Q4sty2Yht2Y",
            "https://www.youtube.com/watch?v=Q7jS00Z5VCU",
            "https://www.youtube.com/watch?v=WpighLFNLto",
            "https://www.youtube.com/watch?v=R6HNhQ43FY8",
            "https://www.youtube.com/watch?v=UjsrZj2dr3A",
            "https://www.youtube.com/watch?v=JE7Y_KZIeAc",
            "https://www.youtube.com/watch?v=ZSe3Rd-A6h0",
            "https://www.youtube.com/watch?v=QB04Hhhjw_k",
            "https://www.youtube.com/watch?v=swYiDAvNUac",
            "https://www.youtube.com/watch?v=g-FecEhHPt4",
            "https://www.youtube.com/watch?v=TzlmR4e_XHo",
            "https://www.youtube.com/watch?v=GV73YIJMaM4",
            "https://www.youtube.com/watch?v=5sG_J6erAPo",
            "https://www.youtube.com/watch?v=QT1zr8m3irM",
            "https://www.youtube.com/watch?v=Y5RmGcTawlA",
            "https://www.youtube.com/watch?v=y_YSxf_pvzE",
            "https://www.youtube.com/watch?v=o-qDSSHNGCE",
            "https://www.youtube.com/watch?v=O0lnZqKVemc",
            "https://www.youtube.com/watch?v=lQCdT6tKRxo",
            "https://www.youtube.com/watch?v=E9U3X0fuoaM",
        ],
        "alegrias",
    )

    processor_alegrias = AudioProcessor(source_alegrias, 41)

    processor_alegrias.process_audios()

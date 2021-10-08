"""Support for youtube audio source"""
import os
from typing import Iterable, Tuple

from youtube_dl import YoutubeDL

from . import AudioSource


class VideoNotDownloadableError(Exception):  # pylint: disable=missing-class-docstring
    pass


class YoutubeAudioSource(AudioSource):
    """
    Class for downloading audios from youtube
    """

    def __init__(self, links: Iterable[str], palo: str) -> None:
        super().__init__()
        self.links = iter(links)
        self.palo = palo

    def __next__(self) -> Tuple[str, int]:
        """
        Takes a link and and a callback which is called with the
        raw audio data
        """
        link = next(self.links)

        audio_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f"../../assets/audios/{self.palo}")
        )

        if not os.path.exists(audio_folder) or not os.path.isdir(audio_folder):
            os.makedirs(audio_folder)

        ydl_params = {
            "format": "bestaudio",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "wav",
                    "preferredquality": "320",
                }
            ],
            # "progress_hooks": [lambda status_info: _download_hook(status_info, callback)],
            "verbose": True,
            "outtmpl": audio_folder + "/%(id)s.%(ext)s",
            "forceduration": True,
        }

        with YoutubeDL(ydl_params) as ydl:
            video_info = ydl.extract_info(link)

            if video_info is not None:
                audio_path: str = f"{audio_folder}/{video_info['id']}.wav"
                duration: int = video_info["duration"]

                return audio_path, duration
            else:
                raise VideoNotDownloadableError(f"Could not download video {link}")

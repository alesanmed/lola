"""Module for audio sources"""
from .generic import AudioSource
from .youtube import YoutubeAudioSource

__all__ = ["YoutubeAudioSource", "AudioSource"]

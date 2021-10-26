from numpy import array, ndarray
from pydub import AudioSegment

from .models import SingletonModels


def encode_audio(audio_path: str) -> ndarray:
    data = AudioSegment.from_mp3(audio_path)
    vgg = SingletonModels().vgg

    if isinstance(data, AudioSegment):
        data = data.set_frame_rate(16000)
        data = array(data.get_array_of_samples())

        encoded = vgg(data)

        return encoded.numpy()

    raise ValueError("Invalid audio")

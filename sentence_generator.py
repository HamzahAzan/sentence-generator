# Libraries

# Provides functions that allows us to interacte with the operating system
import os
# Audio processing functions i.e read, write and concatenate + filters etc
from pydub import AudioSegment, effects
# Helps us to remove unnecessary silence segments from audio
from pydub.silence import split_on_silence


# Helper function : Splits silent parts and then concatenate the audible chunks

def remove_silence(audio):
    '''
    Removes silent parts given an audio file
    '''
    audio_chunks = split_on_silence(
        audio, silence_thresh=-15, min_silence_len=100, keep_silence=90)
    result = AudioSegment.empty()
    for chunk in audio_chunks:
        result += chunk
    return result

# concarenates words separately, removes silence and fades in


def concatenate_word(phonemes):
    '''
    Joins audio files after removing any silent parts.
    crossfade_duration defualt = 20, can be changed to smoothen the audio output
    '''
    word = AudioSegment.silent(duration=20)

    for phoneme in phonemes:
        phoneme = remove_silence(phoneme)
        word += phoneme.fade_in(200)

    return word

# Reads the input path and reorders the files to form the required sentence


def read_files(dir):
    '''
    Reads the input path and reorders the files to form the required sentence
    '''
    dir_list = os.listdir(dir)
    phonemes_order = [10, 27, 9, 28, 8, 23, 3, 5, 17, 11, 20, 13, 21, 23, 26, 22,
                      32, 1, 25, 31, 29, 14, 18, 2, 24, 16, 7, 30, 12, 15, 6, 19, 4, 16]
    phonemes = [dir_list[i] for i in phonemes_order]

    return phonemes


def generate_sentence(input_paths, output_path):
    '''
    generates a sentence from given input directory. 
    '''
    # Read the files from directory in order
    audio_files = read_files(input_paths)

    # Create a list of audio segments using pydub and remove any non wav files then normalize the signals and iterate for each audio file in the list of files
    phonemes = [AudioSegment.from_file(os.path.join(
        input_paths, file), format="wav").normalize() for file in audio_files]

    # Configuring the words by slicing method, to combine them separately for individual processes
    word_configs = [
        (phonemes[:2]),  # First word
        (phonemes[2:6]),  # Second word
        (phonemes[6:8]),  # Third word
        (phonemes[8:10]),  # Fourth word
        (phonemes[10:14]),  # Fifth word
        (phonemes[14:19]),  # Sixth word
        (phonemes[19:21]),  # Seventh word
        (phonemes[21:25]),  # Eighth word
        (phonemes[25:29]),  # Ninth word
        (phonemes[29:31]),  # Tenth word
        (phonemes[31:34])  # Last word
    ]

    # Concatenate the words
    words = [concatenate_word(phonemes) for phonemes in word_configs]

    # Create silent output audio segment
    output = AudioSegment.silent(duration=50)

    # Concatenate words to generate the sentence with fade in
    for word in words:
        output += word.fade_in(200)

    # print on terminal
    print(f"Exporting resulting audio file to {output_path}")

    # Low pass filter to eliminate high noise freq + reducing the gain by 4dB for clearer audio
    output = effects.low_pass_filter(output, 1000) - 4

    # Exporting Audio using Pydub
    output.export(output_path, format='wav')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Audio file combiner using wave module in Python")
    parser.add_argument(
        "-i", "--input", help="Path to the directory containing the list of audio files")
    parser.add_argument(
        "-o", "--output", help="Path to the output audio file, file name and extension must be given 'WAV ' ")

    args = parser.parse_args()

    generate_sentence(args.input, args.output)

# Sentence Generator with Audio Concatenation

This Python script allows you to generate a sentence from a directory containing individual generated phoneme audio files.
It concatenates the audio files to form  **ނާީ ރކޔަި ުެ ހފގީުެ ޮ ސޓޯ ް ހނލޏޖަ ާިް ކއތގަި ީެ ޅު ޮ ނަ ުް ރއގޒަާި ު** which is a dhevhi sentence formed using a specific order of the phomemes. 
The script applies audio processing techniques to enhance the output audio quality and to make it sound as human-like as possible.

**Stuff you might be looking for**:
 - [System Requirements](https://github.com/HamzahAzan/sentence-generator#system-requirements)
 - [Setup](https://github.com/hamzahazan/sentence-generator#setup)
 - [Usage](https://github.com/hamzahazan/sentence-generator#usage)
 - [Example](https://github.com/hamzahazan/sentence-generator#example)


## Features

- Removes silent parts from audio files.
- Applies fade-in effects to create smooth transitions between words.
- Configurable low-pass filter for noise reduction.
- Exports the generated sentence as a WAV audio file.


## System Requirements

- Python 3.x
- Required Python libraries:
  - `pydub`


## Setup

1. Ensure you have `python3.x` installed in your machine.

2. Install `pydub` using the following command `pip install pydub`.


## Usage

1. Clone this repository to your local machine or download the script.

2. Navigate to the directory where the script is located.

3. Run the script using the following command:

```python
python3 sentence_generator.py -i <input_directory> -o <output_file.wav>
```

Replace `<input_directory>` with the path to the directory containing the phoneme audio files and `<output_file.wav>` with the desired output file name and extension (WAV).

4. The script will process the audio files, generate the sentence, and export it as a WAV file in the current directory.


## Example

To generate a sentence from audio files located in the `input_audio` directory and save the output as `output_sentence.wav`, you can use the following command:

```python
python3 sentence_generator.py -i /path/to/phonemes -o /path/to/generated_sentence.wav
```


## Author

Hamzah Azan

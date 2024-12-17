import os
import wave
import json
import sys
import time
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

def convert_to_wav(input_file):
    """
    Converts MP3 to WAV format and returns the WAV file path.
    If the file is already a WAV, it returns the same path.
    """
    if input_file.lower().endswith(".mp3"):
        print("Converting MP3 to WAV...")
        wav_file = input_file.rsplit(".", 1)[0] + ".wav"
        audio = AudioSegment.from_mp3(input_file)
        audio = audio.set_channels(1)  # Mono channel
        audio = audio.set_frame_rate(16000)  # 16 kHz sample rate
        audio.export(wav_file, format="wav")
        print(f"Conversion completed: {wav_file}")
        return wav_file
    elif input_file.lower().endswith(".wav"):
        print("Input file is already a WAV file.")
        return input_file
    else:
        raise ValueError("Unsupported file format. Only MP3 and WAV files are supported.")

def transcribe_audio(wav_path, model_path):
    """
    Transcribes the audio from a WAV file using Vosk and shows progress.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model path does not exist. Please download the model.")

    # Load the Vosk model
    model = Model(model_path)

    # Open WAV file
    with wave.open(wav_path, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getframerate() != 16000:
            raise ValueError("Audio file must be mono and 16 kHz.")

        # Initialize recognizer
        recognizer = KaldiRecognizer(model, wf.getframerate())

        # Transcribe audio with progress bar
        transcription = []
        print("Transcribing audio...")

        total_frames = wf.getnframes()
        start_time = time.time()

        while True:
            data = wf.readframes(4000)
            current_frame = wf.tell()
            elapsed_time = time.time() - start_time

            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                transcription.append(result.get("text", ""))

            # Update progress
            progress = current_frame / total_frames
            remaining_time = elapsed_time / progress - elapsed_time if progress > 0 else 0
            progress_bar = f"[{'#' * int(progress * 50):<50}]"
            print(
                f"\r{progress_bar} {progress * 100:.1f}% - ETA: {remaining_time:.1f} sec",
                end="",
                flush=True,
            )

        # Final result
        print("\nFinalizing transcription...")
        final_result = json.loads(recognizer.FinalResult())
        transcription.append(final_result.get("text", ""))

    return " ".join(transcription)

def save_transcription(text, input_file):
    """
    Saves the transcribed text to a .txt file with the same base name as the input file.
    """
    base_name = os.path.splitext(input_file)[0]
    output_file = base_name + ".txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Transcription saved to: {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe_podcast.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    model_dir = "vosk-model-small-pt"  # Path to the Vosk model

    try:
        # Step 1: Convert MP3 to WAV if necessary
        wav_file = convert_to_wav(input_file)

        # Step 2: Transcribe audio
        transcription = transcribe_audio(wav_file, model_dir)

        # Step 3: Save transcription to a file
        save_transcription(transcription, input_file)

        # Step 4: Output transcription
        print("\nTranscription completed:")
        print("-" * 40)
        print(transcription)
        print("-" * 40)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

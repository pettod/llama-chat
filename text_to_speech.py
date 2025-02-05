import torch
import torchaudio
from TTS.api import TTS

def text_to_speech(text, output_path="output.wav", model_name="tts_models/en/ljspeech/tacotron2-DDC", device="cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"):
    """
    Convert text to high-quality speech using Coqui TTS
    
    Args:
        text (str): Text to convert to speech
        output_path (str): Path to save the audio file
        model_name (str): Name of the TTS model to use
        device (str): Device to run inference on ('cuda', 'mps' or 'cpu')
    """
    try:
        # Initialize TTS with the selected model
        tts = TTS(model_name=model_name).to(device)
        
        # Generate speech
        tts.tts_to_file(text=text, 
                       file_path=output_path,
                       speaker=tts.speakers[0] if tts.speakers else None)
        
        return output_path
        
    except Exception as e:
        print(f"Error generating speech: {str(e)}")
        return None

def change_speech_speed(input_path, output_path, speed_factor=1.0):
    """
    Change the speed of the generated speech without affecting pitch
    
    Args:
        input_path (str): Path to input audio file
        output_path (str): Path to save modified audio
        speed_factor (float): Speed modification factor (1.0 = normal speed)
    """
    try:
        # Load the audio file
        waveform, sample_rate = torchaudio.load(input_path)
        
        # Initialize the speed transform
        transform = torchaudio.transforms.Speed(speed_factor)
        
        # Apply the transform
        modified_waveform = transform(waveform)
        
        # Save the modified audio
        torchaudio.save(output_path, modified_waveform, sample_rate)
        
        return output_path
        
    except Exception as e:
        print(f"Error modifying speech speed: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    text = "Hello! This is a high-quality text-to-speech system."
    
    # Generate speech
    audio_path = text_to_speech(text)
    
    # Optionally modify speech speed
    if audio_path:
        modified_path = "modified_output.wav"
        change_speech_speed(audio_path, modified_path, speed_factor=1.2)

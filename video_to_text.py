import os
import whisper
import moviepy.editor as mp

def extract_audio_from_video(video_file, output_audio_file):
    """Extracts audio from video and saves it as an audio file."""
    try:
        video = mp.VideoFileClip(video_file)
        video.audio.write_audiofile(output_audio_file)
        print(f"Audio extracted from {video_file} and saved as {output_audio_file}.")
    except Exception as e:
        print(f"Failed to extract audio from {video_file}: {e}")

def transcribe_audio_with_whisper(audio_file, model):
    """Transcribes audio to text using the Whisper model."""
    try:
        result = model.transcribe(audio_file)
        print(f"Transcription completed for {audio_file}.")
        return result['text']
    except Exception as e:
        print(f"Failed to transcribe {audio_file}: {e}")
        return "[Transcription Error]"

def process_videos(video_folder, model):
    """Processes all videos in a folder, transcribes them, and saves the transcription."""
    for video_file in os.listdir(video_folder):
        if video_file.endswith('.mp4'):
            video_path = os.path.join(video_folder, video_file)
            audio_file = video_file.replace('.mp4', '.wav')
            audio_path = os.path.join(video_folder, audio_file)
            
            try:
                # Extract audio from video
                extract_audio_from_video(video_path, audio_path)
                
                # Transcribe audio with Whisper
                transcription = transcribe_audio_with_whisper(audio_path, model)
                
                # Save transcription to a text file
                transcription_file = video_file.replace('.mp4', '.txt')
                transcription_path = os.path.join(video_folder, transcription_file)
                with open(transcription_path, 'w') as f:
                    f.write(transcription)
                
                print(f"Transcription saved as {transcription_file}.")
                
            except Exception as e:
                print(f"Error processing {video_file}: {e}")
            
            finally:
                # Clean up: Optionally remove the temporary audio file
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                    print(f"Temporary audio file {audio_file} deleted.")

if __name__ == "__main__":
    # Set the path to your video folder
    video_folder = "Named_Class_Recordings/"  
    
    try:
        # Load the Whisper model
        model = whisper.load_model("large")  
        print("Whisper model loaded successfully.")
        
        # Process all videos in the folder
        process_videos(video_folder, model)
        
    except Exception as e:
        print(f"An error occurred: {e}")

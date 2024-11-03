from transformers import AutoTokenizer, AutoModel
import os

def download_models():
    # Create models directory
    os.makedirs("models", exist_ok=True)
    
    # Download emotion recognition model
    print("Downloading emotion recognition model...")
    tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
    model = AutoModel.from_pretrained("SamLowe/roberta-base-go_emotions")
    
    # Save models
    tokenizer.save_pretrained("models/emotion_recognition")
    model.save_pretrained("models/emotion_recognition")
    
    print("Models downloaded successfully!")

if __name__ == "__main__":
    download_models() 
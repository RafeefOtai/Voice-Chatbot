import os
import whisper
import cohere

from gtts import gTTS
from playsound import playsound


# Load Whisper model
model = whisper.load_model("small.en")


# Read Cohere API key from the terminal
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    raise ValueError(
        "COHERE_API_KEY was not found. "
        "Set it in the terminal before running the program."
    )


co = cohere.ClientV2(api_key=api_key)


def process_turn(audio_file, output_file, messages):
    # Play the user's recording
    playsound(audio_file)

    # 1. Convert audio to text
    result = model.transcribe(
        audio_file,
        language="en",
        task="transcribe",
        fp16=False,
        temperature=0,
        condition_on_previous_text=False,
        initial_prompt="This conversation is about AI chatbots and AI assistants."
    )

    user_text = result["text"].strip()

    if not user_text:
        print("\nRafeef: No speech was detected.")
        return messages

    print(f"\nRafeef: {user_text}")

    messages.append(
        {
            "role": "user",
            "content": user_text
        }
    )

    # 2. Generate a response using Cohere
    try:
        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a simple voice chatbot"
                        "The user's name is Rafeef, spelled R-A-F-E-E-F"
                        "If you address the user by name, always write Rafeef"
                        "Answer clearly in English using no more than two short sentences"
                    )
                },
                *messages
            ],
            max_tokens=100,
            temperature=0.3
        )

        reply_text = response.message.content[0].text.strip()

    except Exception as error:
        print("\nBot: An error occurred while generating the response.")
        print(f"Error details: {error}")
        return messages

    print(f"\nBot: {reply_text}")

    messages.append(
        {
            "role": "assistant",
            "content": reply_text
        }
    )

    # 3. Convert the response to audio
    try:
        tts = gTTS(
            text=reply_text,
            lang="en",
            slow=False
        )

        tts.save(output_file)
        playsound(output_file)

    except Exception as error:
        print("\nBot audio could not be played.")
        print(f"Error details: {error}")

    print("\n" + "-" * 50)

    return messages


print("=" * 50)
print("                 Voice Chatbot")
print("=" * 50)


history = []

history = process_turn(
    "input1.wav",
    "output1.mp3",
    history
)

input("\nPress Enter to continue...")

history = process_turn(
    "input2.wav",
    "output2.mp3",
    history
)
import pyttsx3
import speech_recognition as aa
import webbrowser
import datetime
import requests



def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    joke_data = response.json()

    if joke_data['type'] == 'single':
        return joke_data['joke']
    else:
        return f"{joke_data['setup']} ... {joke_data['delivery']}"
    
def sptext():
    recognizer = aa.Recognizer()
    with aa.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()  # Convert recognized text to lowercase here
        except aa.UnknownValueError:
            print("Sorry! Couldn't understand!")
            return None


def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Choose the desired voice
    engine.setProperty("rate", 150)  # Set the speaking rate
    engine.say(text)
    engine.runAndWait()


# Main program
if __name__ == "__main__":
    data1 = sptext()

    if data1:  # Ensure sptext returned valid input
        if "your name" in data1:
            name = "Hi Vighnesh, my name is Vighnesh. You are very good."
            speechtx(name)

        elif "old are you" in data1:  # Match the correct phrase
            age = "Hi, I am 4 years old."
            speechtx(f"Hey Vaishu, {age}")

        elif "what's the time" in data1 or "what is the time" in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")  # Properly format time
            speechtx(f"The time is {time}")

        elif "please open youtube for me" in data1:
            webbrowser.open("https://www.youtube.com/")
            speechtx("Sure! Here you go!")

        elif "tell me a joke" in data1:
            # Fix for jokes
            joke = get_joke()
            print(joke)
            speechtx(f"Hehehe! Here's a joke for you: {joke}")




            

            
        
        


 




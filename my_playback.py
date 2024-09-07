def main():
    message = input("message: ")
    message_playback = playback_of(message)
    print(f"message: {message_playback}")

def playback_of(message):
    message_playback = message.strip().replace(" ", "...")
    return message_playback


if __name__ == "__main__":
    main()

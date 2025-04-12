def main():
    remix = input().strip()
    original_words = remix.split("WUB")
    song = " ".join([word for word in original_words if word])
    print(song)

if __name__ == "__main__":
    main()

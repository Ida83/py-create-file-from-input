def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    with open(f"{file_name}.txt", "a") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(f"{text}\n")


if __name__ == "__main__":
    main()

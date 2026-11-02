# Text Editor with Character-by-Character and Word-by-Word Undo/Redo
# Using Python Lists as Stacks

current_text = ""
undo_stack = []
redo_stack = []
editing_mode = "word"


def write_text(new_text):
    global current_text

    if not new_text:
        print("No text entered!")
        return

    if editing_mode == "character":
        # Save each previous state, character by character
        for char in new_text:
            undo_stack.append(current_text)
            current_text += char

    else:
        # Save each previous state, word by word
        words = new_text.split()

        for word in words:
            undo_stack.append(current_text)

            if current_text:
                current_text += " " + word
            else:
                current_text = word

    # A new edit clears the redo history
    redo_stack.clear()

    print(f'\nCurrent Text: "{current_text}"')


def undo_text():
    global current_text

    if not undo_stack:
        print("Nothing to undo!")
        return

    # Save the current state for redo
    redo_stack.append(current_text)

    # Restore the previous state
    current_text = undo_stack.pop()

    print(f'\nUndo performed. Current Text: "{current_text}"')


def redo_text():
    global current_text

    if not redo_stack:
        print("Nothing to redo!")
        return

    # Save the current state for undo
    undo_stack.append(current_text)

    # Restore the next state
    current_text = redo_stack.pop()

    print(f'\nRedo performed. Current Text: "{current_text}"')


def show_text():
    print(f'\nCurrent Text: "{current_text}"')


def change_mode():
    global editing_mode

    print("\n--- SELECT EDITING MODE ---")
    print("1. Character-by-character")
    print("2. Word-by-word")

    choice = input("Choose mode (1-2): ")

    if choice == "1":
        editing_mode = "character"
        print("Editing mode changed to Character-by-character.")

    elif choice == "2":
        editing_mode = "word"
        print("Editing mode changed to Word-by-word.")

    else:
        print("Invalid mode selection!")


def show_history():
    print("\n--- EDITING HISTORY ---")
    print("Undo stack:", undo_stack)
    print("Redo stack:", redo_stack)


def main():
    while True:
        print("\n====== TEXT EDITOR ======")
        print("Editing Mode:", editing_mode)
        print("Current Text:", current_text)
        print("-------------------------")
        print("1. Write Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Show Current Text")
        print("5. Change Editing Mode")
        print("6. Show Stack History")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            new_text = input("Enter text to write: ")
            write_text(new_text)

        elif choice == "2":
            undo_text()

        elif choice == "3":
            redo_text()

        elif choice == "4":
            show_text()

        elif choice == "5":
            change_mode()

        elif choice == "6":
            show_history()

        elif choice == "7":
            print("Exiting Text Editor. Goodbye!")
            break

        else:
            print("Invalid choice! Enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

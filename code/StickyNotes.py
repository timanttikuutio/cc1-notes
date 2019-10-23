import sys
import os

#Ik it's ugly but it works
def os_ver():
    return f"{sys.platform}"

def clear_cmd():
    if os_ver() == "win32":
        os.system("cls")
    elif os_ver() == "linux":
        os.system("clear")

def main():
    if not os.path.exists("notes.txt"):
        with open("notes.txt", "w"):
            pass

    clear_cmd()
    note_id = 0
    note_list = ""
    note_length = 16
    with open("notes.txt", "r") as file:
        for note in file:
            note = note.strip()
            note_id += 1
            note_list += f"{note_id}. {note}\n"
            if note_length < len(note):
                note_length = len(note) + 3

    print("Notes")
    print("1) Create Note")
    print("2) Delete Note")
    print("3) Exit")
    print("=" * note_length)
    print(note_list)
    inp = input("What would you like to do? ")
    if inp == "1":
        note = input("Input your note here to finish creating the note: ")
        with open("notes.txt", "a+") as output:
            output.write(str(f"{note}\n"))
        main()
    elif inp == "2":
        inp = input("Give the selected notes ID shown on the left side of the note to delete it.")
        note = (note_list.split(f"{inp}."))[1].split("\n")[0]
        with open("notes.txt", "r") as f:
            lines = f.readlines()
        with open("notes.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != note[1:]:
                    f.write(line)
        main()
    elif inp == "3":
        sys.exit()
    else:
        main()
        
main()
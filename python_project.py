"""
File Manager Chatbot
====================

A command-line chatbot that allows users to manage files and folders
using simple text-based commands.



Language: Python 3
"""

import os
import shutil


def list_files(path="."):
    """
    List files and directories in the given path.

    :param path: Directory path (default is current directory)
    """
    try:
        items = os.listdir(path)
        if not items:
            print("📂 Directory is empty.")
        else:
            print("📂 Files and folders:")
            for item in items:
                print(" -", item)
    except Exception as e:
        print(f"❌ Error: {e}")


def create_file(filename):
    """
    Create an empty file.

    :param filename: Name of the file to create
    """
    try:
        with open(filename, 'x'):
            pass
        print(f"✅ File '{filename}' created.")
    except FileExistsError:
        print("⚠️ File already exists.")
    except Exception as e:
        print(f"❌ Error: {e}")


def read_file(filename):
    """
    Read and display the contents of a file.

    :param filename: Name of the file to read
    """
    try:
        with open(filename, 'r') as file:
            print("\n📄 File contents:\n")
            print(file.read())
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_file(filename):
    """
    Delete a file.

    :param filename: Name of the file to delete
    """
    try:
        os.remove(filename)
        print(f"🗑️ File '{filename}' deleted.")
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ Error: {e}")


def create_folder(foldername):
    """
    Create a new folder.

    :param foldername: Name of the folder
    """
    try:
        os.mkdir(foldername)
        print(f"📁 Folder '{foldername}' created.")
    except FileExistsError:
        print("⚠️ Folder already exists.")
    except Exception as e:
        print(f"❌ Error: {e}")


def move_file(source, destination):
    """
    Move or rename a file.

    :param source: Source file path
    :param destination: Destination file path
    """
    try:
        shutil.move(source, destination)
        print(f"🚚 Moved '{source}' to '{destination}'.")
    except FileNotFoundError:
        print("⚠️ Source file not found.")
    except Exception as e:
        print(f"❌ Error: {e}")


def show_help():
    """Display available commands."""
    print("""
🤖 File Manager Chatbot Commands:

- list files
- create file <filename>
- read file <filename>
- delete file <filename>
- create folder <foldername>
- move file <source> to <destination>
- help
- exit
""")


def chatbot():
    """Main chatbot loop."""
    print("🤖 File Manager Chatbot Started!")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input("💬 You: ").strip().lower()

        if command == "exit":
            print("👋 Goodbye!")
            break

        elif command == "help":
            show_help()

        elif command == "list files":
            list_files()

        elif command.startswith("create file"):
            filename = command.replace("create file", "").strip()
            create_file(filename)

        elif command.startswith("read file"):
            filename = command.replace("read file", "").strip()
            read_file(filename)

        elif command.startswith("delete file"):
            filename = command.replace("delete file", "").strip()
            delete_file(filename)

        elif command.startswith("create folder"):
            foldername = command.replace("create folder", "").strip()
            create_folder(foldername)

        elif command.startswith("move file"):
            try:
                parts = command.replace("move file", "").strip().split(" to ")
                move_file(parts[0], parts[1])
            except IndexError:
                print("⚠️ Invalid move command format.")

        else:
            print("❓ Unknown command. Type 'help' for assistance.")


if __name__ == "__main__":
    chatbot()
import os
import shutil

class FileManager:
    def __init__(self):
        self.folder = "files"

        # Create files folder if it doesn't exist
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def get_path(self, filename):
        return os.path.join(self.folder, filename)

    def create_file(self):
        filename = input("Enter filename (e.g., notes.txt): ").strip()
        filepath = self.get_path(filename)

        if os.path.exists(filepath):
            print("❌ File already exists.")
            return

        content = self.multiline_input()

        with open(filepath, "w") as file:
            file.write(content)

        print("✅ File created successfully.")

    def multiline_input(self):
        print("\nEnter text below.")
        print("Type 'SAVE' on a new line when finished.\n")

        lines = []

        while True:
            line = input()

            if line.upper() == "SAVE":
                break

            lines.append(line)

        return "\n".join(lines)

    def read_file(self):
        filename = input("Enter filename: ").strip()
        filepath = self.get_path(filename)

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        with open(filepath, "r") as file:
            content = file.read()

        print("\n----- FILE CONTENT -----")
        print(content)
        print("------------------------")

    def edit_file(self):
        filename = input("Enter filename: ").strip()
        filepath = self.get_path(filename)

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        print("Enter new content:")
        content = self.multiline_input()

        with open(filepath, "w") as file:
            file.write(content)

        print("✅ File updated successfully.")

    def delete_file(self):
        filename = input("Enter filename: ").strip()
        filepath = self.get_path(filename)

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        confirm = input(
            f"Are you sure you want to delete '{filename}'? (y/n): "
        ).lower()

        if confirm == "y":
            os.remove(filepath)
            print("✅ File deleted successfully.")
        else:
            print("❌ Deletion cancelled.")

    def rename_file(self):
        old_name = input("Enter current filename: ").strip()
        old_path = self.get_path(old_name)

        if not os.path.exists(old_path):
            print("❌ File not found.")
            return

        new_name = input("Enter new filename: ").strip()
        new_path = self.get_path(new_name)

        if os.path.exists(new_path):
            print("❌ A file with that name already exists.")
            return

        os.rename(old_path, new_path)
        print("✅ File renamed successfully.")

    def list_files(self):
        files = os.listdir(self.folder)

        if not files:
            print("📂 No files found.")
            return

        print("\n----- FILES -----")
        for index, file in enumerate(files, start=1):
            print(f"{index}. {file}")
        print("-----------------")

    def copy_file(self):
        source = input("Enter file to copy: ").strip()
        source_path = self.get_path(source)

        if not os.path.exists(source_path):
            print("❌ Source file not found.")
            return

        destination = input(
            "Enter new file name for copy: "
        ).strip()

        destination_path = self.get_path(destination)

        shutil.copy(source_path, destination_path)

        print("✅ File copied successfully.")

    def move_file(self):
        filename = input(
            "Enter filename to move: "
        ).strip()

        source_path = self.get_path(filename)

        if not os.path.exists(source_path):
            print("❌ File not found.")
            return

        destination_folder = input(
            "Enter destination folder: "
        ).strip()

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(
            destination_folder,
            filename
        )

        shutil.move(
            source_path,
            destination_path
        )

        print(
            f"✅ File moved to '{destination_folder}'"
        )

    def search_file(self):
        filename = input("Enter filename to search: ").strip()
        filepath = self.get_path(filename)

        if os.path.exists(filepath):
            print("✅ File exists.")
        else:
            print("❌ File not found.")

    def file_info(self):
        filename = input("Enter filename: ").strip()
        filepath = self.get_path(filename)

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        size = os.path.getsize(filepath)

        print("\n----- FILE INFO -----")
        print(f"Filename: {filename}")
        print(f"Size: {size} bytes")
        print("---------------------")

    def word_count(self):
        filename = input("Enter filename: ").strip()
        filepath = self.get_path(filename)

        if not os.path.exists(filepath):
            print("❌ File not found.")
            return

        with open(filepath, "r") as file:
            content = file.read()

        words = content.split()

        print(f"📝 Total words: {len(words)}")

    def menu(self):
        while True:
            print("\n" + "=" * 35)
            print("      SIMPLE FILE MANAGER")
            print("=" * 35)
            print("1. Create File")
            print("2. Read File")
            print("3. Edit File")
            print("4. Delete File")
            print("5. Rename File")
            print("6. View All Files")
            print("7. Search File")
            print("8. File Information")
            print("9. Word Count")
            print("10. Copy File")
            print("11. Move File")
            print("12. Exit")

            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                self.create_file()

            elif choice == "2":
                self.read_file()

            elif choice == "3":
                self.edit_file()

            elif choice == "4":
                self.delete_file()

            elif choice == "5":
                self.rename_file()

            elif choice == "6":
                self.list_files()

            elif choice == "7":
                self.search_file()

            elif choice == "8":
                self.file_info()

            elif choice == "9":
                self.word_count()

            elif choice == "10":
                self.copy_file()

            elif choice == "11":
                self.move_file()

            elif choice == "12":
                print("👋 Exiting File Manager...")
                break

            else:
                print("❌ Invalid option. Try again.")


def main():
    file_manager = FileManager()
    file_manager.menu()


if __name__ == "__main__":
    main()
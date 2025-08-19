import hashlib
from difflib import SequenceMatcher
from pathlib import Path

def main() -> None:
    text: str = 'Hello. Please inform us the name of 2 files'
    print(text)
    file1 = input("File name 1:")
    file2 = input("File name 2:")

    teste = Path(file1).exists()
    teste2 = Path(file2).exists()
    if teste and teste2:
        msg1, msg2 = hash_file(file1, file2)

        if(msg1 == msg2):
            print("These files are identical")
        else:
            print("These files are not identical")
    else:
        print("File not found")

def hash_file(fileName1, fileName2):

    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    try:
        with open(fileName1, "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h1.update(chunk)
    except FileNotFoundError:
        return None, None
    
    try:
        with open(fileName2, "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h2.update(chunk)
    except FileNotFoundError:
        return None, None

    return h1.hexdigest(), h2.hexdigest()

if __name__ == '__main__':
    main()
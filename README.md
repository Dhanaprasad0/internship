# Text Manipulation and File Compression Utility

This script provides various functionalities for text manipulation and file compression. It supports creating, renaming, deleting, and manipulating text files as well as compressing and decompressing files using different methods.

## Prerequisites

Ensure you have Python installed on your system. This script uses standard Python libraries, so no additional installations are required.

## Usage

The script can be run from the command line with different subcommands for text manipulation and file compression. Below are the details for each subcommand.



## Text Manipulation Commands

### Create a File

```sh
python main.py text create <file> <text>
```

Example:
```sh
python main.py text create example.txt "Hello, World!"
```

### Rename a File

```sh
python main.py text rename <file> <renamefile>
```

Example:
```sh
python main.py text rename example.txt new_example.txt
```

### Delete a File

```sh
python main.py text delete <file>
```

Example:
```sh
python main.py text delete example.txt
```

### Replace Text in a File

```sh
python main.py text replace <file> <find> <replace>
```

Example:
```sh
python main.py text replace example.txt World Earth
```

### Remove Text from a File

```sh
python main.py text remove <file> <find>
```

Example:
```sh
python main.py text remove example.txt Hello
```

### Read File Content

```sh
python main.py text read <file>
```

Example:
```sh
python main.py text read example.txt
```

### Find Text in a File

```sh
python main.py text find <file> <find>
```

Example:
```sh
python main.py text find example.txt World
```

### Trim Whitespace from a File

```sh
python main.py text trim <file>
```

Example:
```sh
python main.py text trim example.txt
```

### Convert Case of Text in a File

```sh
python main.py text case <file> <upper|lower|swapcase>
```

Example:
```sh
python main.py text case example.txt upper
```

### Count Words in a File

```sh
python main.py text count <file> [--word <word>]
```

Example:
```sh
python main.py text count example.txt --word Hello
```

### Reverse the Content of a File

```sh
python main.py text reverse <file>
```

Example:
```sh
python main.py text reverse example.txt
```

### Append Text to a File

```sh
python main.py text append <file> <append>
```

Example:
```sh
python main.py text append example.txt "More text"
```

---

## File Compression Commands

### Compress a File

```sh
python main.py compression compress <file> <output> <gzip|zip|bz2|lzma|tar>
```

Example:
```sh
python main.py compression compress example.txt example.zip zip
```

### Decompress a File

```sh
python main.py compression decompress <file> <output> <gzip|zip|bz2|lzma|tar>
```

Example:
```sh
python main.py compression decompress example.zip decompressed_files/ zip
```

### List Contents of a ZIP File

```sh
python main.py compression list_file <file>
```

Example:
```sh
python main.py compression list_file example.zip
```

### Add a File to an Existing ZIP File

```sh
python main.py compression add_file <file> <append>
```

Example:
```sh
python main.py compression add_file existing.zip new_file.txt
```

---

## License

This project is licensed under the MIT License.
```

### Explanation

This version maintains a clearer structure with headings and subheadings for each command category (`Text Manipulation Commands` and `File Compression Commands`). Each command includes a brief description, usage syntax, and example command to run with the script (`main.py`). This structure improves readability and usability for users exploring your utility script.

# Text Manipulation and File Compression Utility

This script provides various functionalities for text manipulation and file compression. It supports creating, renaming, deleting, and manipulating text files as well as compressing and decompressing files using different methods.

## Prerequisites

Ensure you have Python installed on your system. This script uses standard Python libraries, so no additional installations are required.

## Usage

The script can be run from the command line with different subcommands for text manipulation and file compression. Below are the details for each subcommand.

## Text Manipulation Commands

- Create a File

 python script.py text create <file> <text>

Ex:python main.py text create example.txt "Hello, World"

- Rename a File

python main.py text rename <file> <renamefile>

Ex:python main.py text create example.txt main.txt

- Delete a File

python main.py text delete <file>

Ex: 
   python main.py text create main.txt

Replace Text in a File

python main.py text replace <file> <find> <replace>

Ex:
   python main.py text replace example.txt World hi
   
    "Hello, hi"

- Remove Text from a File

python main.py text remove <file> <find>

Ex:
   python main.py text remove example.txt  hi
   "Hello, "

- Find Text in a File

python main.py text find <file> <find>

Ex:
   python main.py text find  example.txt hello

- Trim Whitespace from a File

python main.py text trim <file>

Ex:
   python main.py text trim example.txt

- Convert Case of Text in a File

python main.py text case <file> <upper|lower|swapcase>

Ex:i)Convert Case of Upper

     python main.py text case example.txt upper
     
     "HI,"
     
   ii)Convert Case of Lower
   
      python main.py text case example.txt lower
      
      "hi,"
   iii)Convert Case of SwapCase
   
       python main.py text case example.txt swapcase
       
       "Hi,"

- Count Words in a File

python main.py text count <file> [--word <word>]

Ex:i)All word counts in the file

     python main.py text count example.txt
     
     The word 'hi' occurs 1 times.
     
     The word 'world' occurs 1 times.
     
   ii)Count Words in a File
   
     python main.py text count example.txt --word Hi
     
     The word 'hi' occurs 1 times.

- Reverse the Content of a File

python main.py text reverse <file>

Ex:python main.py text reverse example.txt

    World Hi

- Append Text to a File

python main.py text append <file> <append>

Ex:python main.py text append example.txt Me

    "Hi, World Me"

## File Compression Commands
- Compress a File

python main.py compression compress <file> <output> <gzip|zip|bz2|lzma|tar>

Ex: Compress a File Using gzip

    python main.py compression compress example.txt example.txt.gz gzip

- Decompress a gzip File

python main.py compression decompress <file> <output> <gzip|zip|bz2|lzma|tar>

Ex: Decompress a gzip File

     python main.py compression decompress example.txt.gz decompressed_example.txt gzip

- For additional help, use the -h or --help flag with any command or subcommand.

python main.py --help

python main.py text --help

python main.py compression --help

## License

This project is licensed under the MIT License.\n

This script and `README.md` should now be ready for use. Let me know if there are any further modifications or if you need any additional features!





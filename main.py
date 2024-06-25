import argparse
import os
import zipfile
import re
from collections import Counter

def create_file(file,text):
    if os.path.exists(file):
        print(f"File '{file}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'w') as f:
            f.write(text)
        with open(file, 'r') as f:
            content=f.read()
            print(content)
        print("File " + file + " created successfully.")
    except FileNotFoundError:
        print(f"Error: could not create file" + file)

def rename_file(file,renamefile):
    try:
        os.rename(file, renamefile)
        print("File " + file + " renamed to " + renamefile + " successfully.")
    except FileNotFoundError:
        print(f"Error: could not rename file " + file)

def delete_file(file):
    try:
        os.remove(file)
        print("File " + file + " deleted successfully.")
    except :
        print(f"Error: could not delete file " + file)

def replace_text(file, find, replace):
    try:
        with open(file, 'r') as f:
            content = f.read()
        content = content.replace(find, replace)
        print(content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Replaced '{find}' with '{replace}' in '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def remove_text(file, find):
    try:
        with open(file, 'r') as f:
            content = f.read()
        content = content.replace(find, '')
        print(content)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Removed '{find}' from '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def find_text(file, find):
    try:
        with open(file, 'r') as f:
            content = f.read()
            print(content)
        split = ''.join(content.split())
        index = split.find(find)
        if index != -1:
            print(f"'{find}' found at index {index}.")
        else:
            print(f"'{find}' not found.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def trim_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
        trimmed_content = content.strip()
        print(f"Trimmed '{file}' is successfully.")
        print(f"Trimmed content:\n'{trimmed_content}'")
        # return trimmed_content
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def convert_case(file, case):
    try:
        with open(file, 'r') as f:
            content = f.read()
        if case == 'upper':
            content = content.upper()
        elif case == 'lower':
            content = content.lower()
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def count_word_in_file(file, word):
    try:
        with open(file, 'r') as f:
            content = f.read()
        count = content.count(word)
        print(f"The word '{word}' occurs {count} times.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def reverse_file_content(file):
    try:
        with open(file, "r") as f:
            content = f.readlines()
            print(content)
        for content in content:
            reversed_texts=" ".join(reversed(content.split()))
            print(reversed_texts)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def count_all_words_in_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
            words = re.findall(r'\b\w+\b', content.lower())
            word_counts = Counter(words)
            print("All word counts in the file:")
            for word, count in word_counts.items():
                print(f" The word '{word}' occurs {count} times.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def append_string_to_file(file, append):
    try:
        with open(file, 'a') as f:
            f.write('\n'+ append)
        with open(file, 'r') as f:
            content=f.read()
            print(content)
        print(f"\nSuccessfully appended '{append}' to the file '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def compress_file(file, output):
    try:
        with zipfile.ZipFile(output, 'w') as zipf:
            zipf.write(file, os.path.basename(file))
        print(f"File '{file}' compressed into '{output}'")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Text Manipulation Utility')
    subparsers = parser.add_subparsers(dest='command')

    parser_create = subparsers.add_parser('create', help='Create the file')
    parser_create.add_argument('file', help='File to process')
    parser_create.add_argument('text', help='Create of new file')

    parser_rename = subparsers.add_parser('rename', help='Rename the file')
    parser_rename.add_argument('file', help='File to process')
    parser_rename.add_argument('renamefile', help='file name to rename file')

    parser_delete = subparsers.add_parser('delete', help='Delete the file')
    parser_delete.add_argument('file', help='File to process')

    parser_replace = subparsers.add_parser('replace', help='Find and replace text')
    parser_replace.add_argument('file', help='File to process')
    parser_replace.add_argument('find', help='Text to find')
    parser_replace.add_argument('replace', help='Text to replace with')

    parser_remove = subparsers.add_parser('remove', help='Find and remove text')
    parser_remove.add_argument('file', help='File to process')
    parser_remove.add_argument('find', help='Text to find')

    parser_find = subparsers.add_parser('find', help='Find the text')
    parser_find.add_argument('file', help='File to process')
    parser_find.add_argument('find', help='Text to find')

    parser_trim = subparsers.add_parser('trim', help='Trim  the file content')
    parser_trim.add_argument('file', help='File to process')

    parser_case = subparsers.add_parser('case', help='Convert text case')
    parser_case.add_argument('file', help='File to process')
    parser_case.add_argument('case', choices=['upper', 'lower'], help='Case to convert to')

    parser_count = subparsers.add_parser('count', help='Count occurrences of a word')
    parser_count.add_argument('file', help='File to process')
    parser_count.add_argument('--word', help='Word to count')

    parser_reverse = subparsers.add_parser('reverse', help='Reverse occurrences of a word')
    parser_reverse.add_argument('file', help='File to process')

    parser_append = subparsers.add_parser('append', help='append to the file')
    parser_append.add_argument('file', help='File to process')
    parser_append.add_argument('append', help='Text to append')

    parser_compress = subparsers.add_parser('compress', help='Compress a file into a ZIP archive')
    parser_compress.add_argument('file', help='File to compress')
    parser_compress.add_argument('output', help='Output ZIP file name')

    args = parser.parse_args()

    if args.command == 'create':
        create_file(args.file,args.text)
    elif args.command == 'rename':
        rename_file(args.file,args.renamefile)
    elif args.command == 'delete':
        delete_file(args.file)
    elif args.command == 'replace':
        replace_text(args.file, args.find, args.replace)
    elif args.command == 'remove':
        remove_text(args.file, args.find)
    elif args.command == 'find':
        find_text(args.file, args.find)
    elif args.command == 'trim':
        trim_file(args.file)
    elif args.command == 'case':
        convert_case(args.file, args.case)
    elif args.command == 'count':
        if args.word:
            count_word_in_file(args.file, args.word)
        else:
            count_all_words_in_file(args.file)
    elif args.command == 'append':
        append_string_to_file(args.file,args.append)
    elif args.command == 'compress':
        compress_file(args.file, args.output)
    elif args.command == 'reverse':
        reverse_file_content(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


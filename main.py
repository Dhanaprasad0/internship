import argparse
import os
import zipfile
import re
from collections import Counter
import lzma
import shutil
import bz2
import tarfile
import gzip

def create_file(file, text):
    if os.path.exists(file):
        print(f"File '{file}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'w+') as f:
            f.write(text)
            f.seek(0)
            content = f.read()
            print(content)
        print("File " + file + " created successfully.")
    except FileNotFoundError:
        print(f"Error: could not create file " + file)

def rename_file(file, renamefile):
    try:
        os.rename(file, renamefile)
        print("File " + file + " renamed to " + renamefile + " successfully.")
    except FileNotFoundError:
        print(f"Error: could not rename file " + file)

def delete_file(file):
    try:
        os.remove(file)
        print("File " + file + " deleted successfully.")
    except:
        print(f"Error: could not delete file " + file)

def replace_text(file, find, replace):
    try:
        with open(file, 'r+') as f:
            content = f.read()
            content = content.replace(find, replace)
            f.seek(0)
            f.write(content)
            f.truncate()
            print(content)
        print(f"Replaced '{find}' with '{replace}' in '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def remove_text(file, find):
    try:
        with open(file, 'r+') as f:
            content = f.read()
            content = content.replace(find, '')
            f.seek(0)
            f.write(content)
            f.truncate()
            print(content)
        print(f"Removed '{find}' from '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def read_text(file):
    try:
        with open(file,"r") as f:
            content = f.read()
        return print(content)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

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
        with open(file, 'r+') as f:
            content = f.read()
            trimmed_content = content.strip()
            f.seek(0)
            f.write(trimmed_content)
            f.truncate()
            print(f"Trimmed '{file}' successfully.")
            print(f"Trimmed content:\n'{trimmed_content}'")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def convert_case(file, case):
    try:
        with open(file, 'r+') as f:
            content = f.read()
            if case == 'upper':
                content = content.upper()
            elif case == 'lower':
                content = content.lower()
            elif case == 'swapcase':
                content = content.swapcase()
            f.seek(0)
            f.write(content)
            f.truncate()
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
            reversed_texts = " ".join(reversed(content.split()))
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
        with open(file, 'a+') as f:
            f.write('\n' + append)
            f.seek(0)
            content = f.read()
            print(content)
        print(f"\nSuccessfully appended '{append}' to the file '{file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")

def decompress_file_zip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with zipfile.ZipFile(file, 'r') as zipf:
            zipf.extractall(output)
        print(f"File '{file}' decompressed into directory '{output}'")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_contents(file):
    try:
        with zipfile.ZipFile(file, 'r') as zipf:
            contents = zipf.namelist()
        print(f"Contents of '{file}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_to_zip(file, append):
    try:
        with zipfile.ZipFile(file, 'a') as zipf:
            zipf.write(append, os.path.basename(append))
        print(f"File '{file}' added to '{append}'")
    except FileNotFoundError:
        print(f"Error: The file '{zip_file}' or '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_zip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file)
        print(f'File {file} compressed to {output}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_bz2(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'rb') as f_in, bz2.open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {file} compressed to {file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file_bz2(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with bz2.open(file, 'rb') as f_in, open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {input_file} decompressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_lzma(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'rb') as f_in, lzma.open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {input_file} compressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file_lzma(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with lzma.open(file, 'rb') as f_in, open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {input_file} decompressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_tar(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with tarfile.open(output, 'w') as tar:
            tar.add(file, arcname=os.path.basename(file))
        print(f'File {input_file} compressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file_tar(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with tarfile.open(file, 'r') as tar:
            tar.extractall(path=output)
        print(f'File {input_file} decompressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_gzip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'rb') as f_in, gzip.open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {input_file} compressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file_gzip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with gzip.open(file, 'rb') as f_in, open(output, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f'File {input_file} decompressed to {output_file}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Text Manipulation and Compression Utility.')
    subparsers = parser.add_subparsers(dest='command')

    text_parser = subparsers.add_parser('text', help='Text manipulation commands')
    text_subparsers = text_parser.add_subparsers(dest='subcommand')

    create_parser = text_subparsers.add_parser('create', help='Create a file with text')
    create_parser.add_argument('file', help='The file to create')
    create_parser.add_argument('text', help='The text to write to the file')

    rename_parser = text_subparsers.add_parser('rename', help='Rename a file')
    rename_parser.add_argument('file', help='The file to rename')
    rename_parser.add_argument('renamefile', help='The new name for the file')

    delete_parser = text_subparsers.add_parser('delete', help='Delete a file')
    delete_parser.add_argument('file', help='The file to delete')

    replace_parser = text_subparsers.add_parser('replace', help='Replace text in a file')
    replace_parser.add_argument('file', help='The file to replace text in')
    replace_parser.add_argument('find', help='The text to find')
    replace_parser.add_argument('replace', help='The text to replace with')

    remove_parser = text_subparsers.add_parser('remove', help='Remove text in a file')
    remove_parser.add_argument('file', help='The file to remove text in')
    remove_parser.add_argument('find', help='The text to remove')

    read_parser = text_subparsers.add_parser('read',help='Read content of file')
    read_parser.add_argument('file', help='The file to read')

    find_parser = text_subparsers.add_parser('find', help='Find text in a file')
    find_parser.add_argument('file', help='The file to find text in')
    find_parser.add_argument('find', help='The text to find')

    trim_parser = text_subparsers.add_parser('trim', help='Trim file content')
    trim_parser.add_argument('file', help='The file to trim')

    case_parser = text_subparsers.add_parser('case', help='Convert text case in a file')
    case_parser.add_argument('file', help='The file to convert text case in')
    case_parser.add_argument('case', choices=['upper', 'lower', 'swapcase'], help='The case conversion to apply')

    count_parser = text_subparsers.add_parser('count', help='Count word occurrences in a file')
    count_parser.add_argument('file', help='The file to count words in')
    count_parser.add_argument('--word', help='The specific word to count')

    reverse_parser = text_subparsers.add_parser('reverse', help='Reverse file content')
    reverse_parser.add_argument('file', help='The file to reverse content in')

    count_all_parser = text_subparsers.add_parser('count_all', help='Count all words in a file')
    count_all_parser.add_argument('file', help='The file to count all words in')

    append_parser = text_subparsers.add_parser('append', help='Append string to file')
    append_parser.add_argument('file', help='The file to append string to')
    append_parser.add_argument('append', help='The string to append')

    compress_parser = subparsers.add_parser('compression', help='File compression commands')
    compress_subparsers = compress_parser.add_subparsers(dest='subcommand')

    compress_file_parser = compress_subparsers.add_parser('compress', help='Compress a file')
    compress_file_parser.add_argument('file', help='The file to compress')
    compress_file_parser.add_argument('output', help='The output compressed file')
    compress_file_parser.add_argument('method', choices=['zip', 'bz2', 'lzma', 'tar', 'gzip'], help='The compression method to use')

    decompress_file_parser = compress_subparsers.add_parser('decompress', help='Decompress a file')
    decompress_file_parser.add_argument('file', help='The file to decompress')
    decompress_file_parser.add_argument('output', help='The output directory or file')
    decompress_file_parser.add_argument('method', choices=['zip', 'bz2', 'lzma', 'tar', 'gzip'], help='The decompression method to use')

    list_parser = compress_subparsers.add_parser('list_file', help='List contents of a ZIP file')
    list_parser.add_argument('file', help='The ZIP file to list contents of')

    add_file_parser = compress_subparsers.add_parser('add_file', help='Add a file to an existing ZIP file')
    add_file_parser.add_argument('file', help='The existing ZIP file')
    add_file_parser.add_argument('append', help='The file to add to the ZIP')

    args = parser.parse_args()
    if args.command == 'text':
        if args.subcommand == 'create':
            create_file(args.file, args.text)
        elif args.subcommand == 'rename':
            rename_file(args.file, args.renamefile)
        elif args.subcommand == 'delete':
            delete_file(args.file)
        elif args.subcommand == 'replace':
            replace_text(args.file, args.find, args.replace)
        elif args.subcommand == 'remove':
            remove_text(args.file, args.find)
        elif args.subcommand == 'read':
            read_text(args.file)
        elif args.subcommand == 'find':
            find_text(args.file, args.find)
        elif args.subcommand == 'trim':
            trim_file(args.file)
        elif args.subcommand == 'case':
            convert_case(args.file, args.case)
        elif args.subcommand == 'count':
            if args.word:
                count_word_in_file(args.file, args.word)
            else:
                count_all_words_in_file(args.file)
        elif args.subcommand == 'reverse':
            reverse_file_content(args.file)
        elif args.subcommand == 'count_all':
            count_all_words_in_file(args.file)
        elif args.subcommand == 'append':
            append_string_to_file(args.file, args.append)
    elif args.command == 'compression':
        if args.subcommand == 'compress':
            if args.method == 'zip':
                compress_file_zip(args.file, args.output)
            elif args.method == 'bz2':
                compress_file_bz2(args.file, args.output)
            elif args.method == 'lzma':
                compress_file_lzma(args.file, args.output)
            elif args.method == 'tar':
                compress_file_tar(args.file, args.output)
            elif args.method == 'gzip':
                compress_file_gzip(args.file, args.output)
        elif args.subcommand == 'decompress':
            if args.method == 'zip':
                decompress_file_zip(args.file, args.output)
            elif args.method == 'bz2':
                decompress_file_bz2(args.file, args.output)
            elif args.method == 'lzma':
                decompress_file_lzma(args.file, args.output)
            elif args.method == 'tar':
                decompress_file_tar(args.file, args.output)
            elif args.method == 'gzip':
                decompress_file_gzip(args.file, args.output)
        elif args.subcommand == 'list_file':
            list_contents(args.file)
        elif args.subcommand == 'add_file':
            add_to_zip(args.file, args.append)

if __name__ == '__main__':
    main()

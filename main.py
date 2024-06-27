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
        elif case == 'swapcase':
            content = content.swapcase()
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
    if os.path.exists(file):
        print(f"File '{file}' already exists. Skipping creation.")
        return
    if os.path.exists(append):
        print(f"File '{append}' already exists. Skipping creation.")
        return
    try:
        with zipfile.ZipFile(file, 'a') as zipf:
            zipf.write(append, os.path.basename(append))
        print(f"File '{file}' added to '{append}'")
    except FileNotFoundError:
        print(f"Error: The file '{zip_file}' or '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

'''def compress_file_zip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with zipfile.ZipFile(output, 'w') as zipf:
            for file in file:
                if os.path.isfile(file):
                    zipf.write(file, os.path.basename(file))
        print(f"File '{file}' compressed into '{output}'")
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")'''

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
        with open(file, 'rb') as f_in:
            with bz2.open(output, 'wb') as f_out:
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
        with bz2.open(file, 'rb') as f_in:
            with open(output, 'wb') as f_out:
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
        with open(file, 'rb') as f_in:
            with lzma.open(output, 'wb') as f_out:
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
        with lzma.open(file, 'rb') as f_in:
            with open(output, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f'File {file} decompressed to {output}')
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
            tar.add(file)
        print(f'File {file} compressed to {output}')
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
            tar.extractall(output)
        print(f'File {file} decompressed to {output}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file_gzip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with open(file, 'rb') as f_in:
            with gzip.open(output, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f'File {file} compressed to {output}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file_gzip(file, output):
    if os.path.exists(output):
        print(f"File '{output}' already exists. Skipping creation.")
        return
    try:
        with gzip.open(file, 'rb') as f_in:
            with open(output, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f'File {file} decompressed to {output}')
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
def main():
    parser = argparse.ArgumentParser(description='Text Manipulation And File Compression ` Utility')
    subparsers = parser.add_subparsers(dest='command')

    parser_text = subparsers.add_parser('text', help='Text manipulation commands')
    text_subparsers = parser_text.add_subparsers(dest='subcommand')

    parser_create = text_subparsers.add_parser('create', help='Create the file')
    parser_create.add_argument('file', help='File to process')
    parser_create.add_argument('text', help='Create of new file')

    parser_rename = text_subparsers.add_parser('rename', help='Rename the file')
    parser_rename.add_argument('file', help='File to process')
    parser_rename.add_argument('renamefile', help='file name to rename file')

    parser_delete = text_subparsers.add_parser('delete', help='Delete the file')
    parser_delete.add_argument('file', help='File to process')

    parser_replace = text_subparsers.add_parser('replace', help='Find and replace text')
    parser_replace.add_argument('file', help='File to process')
    parser_replace.add_argument('find', help='Text to find')
    parser_replace.add_argument('replace', help='Text to replace with')

    parser_remove = text_subparsers.add_parser('remove', help='Find and remove text')
    parser_remove.add_argument('file', help='File to process')
    parser_remove.add_argument('find', help='Text to find')

    parser_find = text_subparsers.add_parser('find', help='Find the text')
    parser_find.add_argument('file', help='File to process')
    parser_find.add_argument('find', help='Text to find')

    parser_trim = text_subparsers.add_parser('trim', help='Trim  the file content')
    parser_trim.add_argument('file', help='File to process')

    parser_case = text_subparsers.add_parser('case', help='Convert text case')
    parser_case.add_argument('file', help='File to process')
    parser_case.add_argument('case', choices=['upper', 'lower', 'swapcase' ], help='Case to convert to')

    parser_count = text_subparsers.add_parser('count', help='Count occurrences of a word')
    parser_count.add_argument('file', help='File to process')
    parser_count.add_argument('--word', help='Word to count')

    parser_reverse = text_subparsers.add_parser('reverse', help='Reverse occurrences of a word')
    parser_reverse.add_argument('file', help='File to process')

    parser_append = text_subparsers.add_parser('append', help='append to the file')
    parser_append.add_argument('file', help='File to process')
    parser_append.add_argument('append', help='Text to append')

    parser_compress = subparsers.add_parser('compression', help='File compression commands')
    compress_subparsers = parser_compress.add_subparsers(dest='subcommand',required=True)

    parser_compression_file = compress_subparsers.add_parser('compress', help='Compress a file into methods')
    parser_compression_file.add_argument('file', help='File to process')
    parser_compression_file.add_argument('output', help='Output file name')
    parser_compression_file.add_argument('method', choices=['gzip', 'zip', 'bz2', 'lzma', 'tar'], help='Compression method')

    parser_compression_file = compress_subparsers.add_parser('decompress', help='Compress a file into methods')
    parser_compression_file.add_argument('file', help='File to process')
    parser_compression_file.add_argument('output', help='Output file name')
    parser_compression_file.add_argument('method', choices=['gzip', 'zip', 'bz2', 'lzma', 'tar'],help='Compression method')

    parser_list = compress_subparsers.add_parser('list_file', help='List contents of a ZIP file')
    parser_list.add_argument('file', help='ZIP file to list contents of')

    parser_add = compress_subparsers.add_parser('add_file', help='Add a file to an existing ZIP archive')
    parser_add.add_argument('file', help='ZIP file to add to')
    parser_add.add_argument('append', help='File to add to the ZIP archive')

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
        elif args.subcommand == 'append':
            append_string_to_file(args.file, args.append)
        else:
            parser.print_help()
    elif args.command == 'compression':
        if args.subcommand == 'compress':
            if args.method == 'gzip':
                compress_file_gzip(args.file, args.output)
            elif args.method == 'zip':
                compress_file_zip(args.file, args.output)
            elif args.method == 'bz2':
                compress_file_bz2(args.file, args.output)
            elif args.method == 'lzma':
                compress_file_lzma(args.file, args.output)
            elif args.method == 'tar':
                compress_file_tar(args.file, args.output)
        elif args.subcommand == 'decompress':
            if args.method == 'gzip':
                decompress_file_gzip(args.file, args.output)
            elif args.method == 'tar':
                decompress_file_tar(args.file, args.output)
            elif args.method == 'lzma':
                decompress_file_lzma(args.file, args.output)
            elif args.method == 'bz2':
                decompress_file_bz2(args.file, args.output)
            elif args.method == 'zip':
                decompress_file_zip(args.file, args.output)
        elif args.subcommand == 'list_file':
            list_to_zip(args.file)
        elif args.subcommand == 'add_file':
            add_to_zip(args.file, args.append)
        else:
            parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


'''ef compress_file_zip(input_file, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file)
    print(f'File {input_file} compressed to {output_file}')'''

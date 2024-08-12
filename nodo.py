import glob

# Finding all .txt files in the current directory
txt_files = glob.glob('*.txt')
print("Text files in current directory:", txt_files)

# Finding all .txt files recursively in a directory
all_txt_files = glob.glob('/my_directory/**/*.txt', recursive=True)
print("All text files:", all_txt_files)

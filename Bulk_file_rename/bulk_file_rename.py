import os

def bulk_rename(folder_path, old_name, new_name):
    for file_name in os.listdir(folder_path):
        if old_name in file_name:
            new_file_name = file_name.replace(old_name, new_name)
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
            print(f"Renaming the files {file_name} to {new_file_name}")

bulk_rename(r'D:\demo_files', 'Samples', 'SamplesNewSampler')
import os 
from subprocess import call

def get_file_extension(file_path: str) -> str:
    _, extension = os.path.splitext(file_path)
    return extension.lower()

def copy_media(output_path: str, image: str, dry_run: bool = False):
    copy_command = f"cp '{image}' '{output_path}'"
    print("output_copy=", os.path.dirname(output_path), "  input=", image)
    if not dry_run:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        call(copy_command, shell=True)

def delete_media(path: str):
    delete_command = f"rm '{path}'"
    call(delete_command, shell=True)

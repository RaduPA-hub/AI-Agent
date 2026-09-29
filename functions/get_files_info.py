import os

def process_files(directory: str):
    data = []
    for file in os.listdir(directory):
            absolut = os.path.join(directory, file)
            file_name = file
            file_size = os.path.getsize(absolut)
            is_dir = os.path.isdir(absolut)
            data.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")
    return data

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolut = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolut, directory))
        valid_target_dir = os.path.commonpath([absolut, target_dir]) == absolut
        if not os.path.isdir(target_dir):
            return (f'Error: "{directory}" is not a directory')
        if not valid_target_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message
    try:
        data = process_files(target_dir)
        joined_data = "\n".join(data)
        return joined_data
    except Exception as e:
        error_message = f"Error : {str(e)}"
        return error_message

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
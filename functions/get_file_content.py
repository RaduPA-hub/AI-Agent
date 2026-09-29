import config
import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolut = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolut, file_path))
        valid_target_path = os.path.commonpath([absolut, target_path]) == absolut
        if not os.path.isfile(target_path):
            return (f'Error: File not found or is not a regular file: "{file_path}"')  
        if not valid_target_path:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory') 
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message
    try:
        with open(target_path, 'r') as f:
            content = f.read(config.MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return content
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the first 10000 characters from a specified file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the file which's content you need to get, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["file_path"]
        },
    },
}
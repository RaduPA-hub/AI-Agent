import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolut = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolut, file_path))
        valid_target_path = os.path.commonpath([absolut, target_path]) == absolut
        if not valid_target_path:
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory') 
        if os.path.isdir(target_path):
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message
    try:
        with open(target_path, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Overwrites a file with the specific content",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path to the file in which it will write, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "The content meant to be written",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}
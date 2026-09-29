import os 
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolut = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolut, file_path))
        valid_target_path = os.path.commonpath([absolut, target_path]) == absolut
        if not valid_target_path:
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if not file_path.endswith('.py'):
            return (f'Error:"{file_path}" is not a Python file' )
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return error_message
    try:
        command = ["python", target_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(args = command, cwd = absolut,capture_output = True, text = True,
        timeout = 30)
        output = ""
        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode}\n"
        if completed_process.stdout == "" and completed_process.stderr == "":
            output += "No output produced"
        else:
            output += f"STDOUT: {completed_process.stdout}\n STDERR: {completed_process.stderr}"
        return output
    except Exception as e:
        error_message = f"Error :{str(e)}"
        return error_message

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python script with the mentioned arguments, if the file doesn't exist or is not a python file, it will return an error message",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the script meant to be run, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "description": "The list of arguments given to the called script ",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": ["file_path"]
        },
    },
}

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
def test():
    #test1
    joined_data = get_files_info("calculator",".")
    print(f"Result for current directory: \n {joined_data}")
    #test2
    joined_data = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg': \n {joined_data}")
    #test3
    joined_data = get_files_info("calculator","/bin")
    print(f"Result for '/bin': \n {joined_data}")
    #test4
    joined_data = get_files_info("calculator", "../")
    print(f"Result for '../': \n {joined_data}")
    #test5
    print(get_file_content("calculator", "pkg/calculator.py"))
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    print(get_file_content("calculator", "main.py"))

    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
if __name__ == "__main__":
    test()
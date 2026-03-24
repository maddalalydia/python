#Creating a new file
'''try:
    with open('sample.txt', 'w') as file:
        print("New file created")
except Exception as e:
    print(f"Error:{e}")'''

#Writing content to a file
'''try:
    with open('sample.txt', 'w') as file:
       string = """Hi hello
       How are you?"""
       file.write(string)
       lines = ['\n i am an python student\n','at codegnan\n']
       file.writelines(lines)
except Exception as e:
    print(f"Error:{e}")'''

#Reading content from a file
'''try:
    with open('sample.txt', 'r') as file:
       content = file.read()
       content1 = file.read()
       print(content)
       print("content1:",content1)
       file.seek(0)
       lines = file.readline()
       print("Lines:", lines)
except Exception as e:
    print(f"Error:{e}")'''

#append content to a file
try:
    with open('sample.txt', 'a') as file:
       string = """\nI am learning python file handling\n"""
       file.write(string)
except Exception as e:
    print(f"Error:{e}")


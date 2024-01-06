

def examples_file_read() :
    file_emp = open("employees.txt", "r")
    #print(file_emp.readable())  # check if it is readable
    #print(file_emp.read()) # read entire file

    #print(file_emp.readline())  # read line & move to next line

    #print(file_emp.readlines())  # read lines & add to an array
    #print(file_emp.readlines()[1])  # read 2nd line from the array

    for emp in file_emp.readlines():
        print (emp)

    file_emp.close() 
    return

def examples_file_append() :
    file_emp = open ("employees.txt", "a")
    file_emp.write("Kelly - Customer Service\n")
    file_emp.close()

    return

def examples_file_write () :
    file_emp = open ("employees2.txt", "w")
    file_emp.write ("Dave - Boss\n")
    file_emp.close()
    return

def TEST_fileio():
    examples_file_write()
    examples_file_append()
    examples_file_read()
    return


# ------ main
TEST_fileio()



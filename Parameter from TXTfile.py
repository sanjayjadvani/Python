
def search_parameter(file_name,param):
    with open(file_name, 'r') as report:
        ln_no=0
        for line in report:
            ln_no+=1
            if param in line:
                print(param, 'is in line ',ln_no)
                print(line)
                print(line.find(param))
                break



param1=input('Please enter the Parameter to search :')
search_parameter('1905100476.txt',param1)





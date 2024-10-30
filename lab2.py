def display_main_menu():
    print("display_main_menu")
    print("Enter some number s separatd by commas (e.g. 5,67,32)")



def get_usr_input():
    print("get user input")
    inputstr = input()
    print("raw input = " + inputstr)
    #split the input string in to segments of strings using comma as splitter
    splitlist = inputstr.split(",")
    print("after splitting: " , splitlist)

    #next step is to convert each short string in the list into float 
    floatlist = [] #define an empty list of float numbers
    for x in splitlist:
      floatnum =   float(x) #convert string into float
      floatlist.append(floatnum) #ad the float number to the float list
      
    print("floatlist" , floatlist)
    return floatlist

def cal_average(input_list):
    print("calc_average")
    total  = sum(input_list)
    average = total/len(input_list)
    print("average = ", average)

def find_min_max(input_list):
    print("find_min_max")
    input_list.sort()
    resultlist = [input_list[0],input_list[-1]]
    print("Min & Max list = " ,resultlist )
    return resultlist


def sort_temperature(input_list):
    print("sort_temperature")
    input_list.sort()

def calc_median_temperature(input_list):
    print("calc_median_temperature")
    count = len(input_list)
    if count % 2 is 1:
        median = input_list[(count-1)//2] #// is an integer divide
    else:
        median = (input_list[count//2] + input_list[count//2-1])/2
    print("median = ", median)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    flaotlist =  get_usr_input()
    cal_average(flaotlist)
    find_min_max(flaotlist)
    sort_temperature(flaotlist)
    print("after sorting = ", flaotlist)
    calc_median_temperature(flaotlist)


if __name__ == "__main__":
    main()

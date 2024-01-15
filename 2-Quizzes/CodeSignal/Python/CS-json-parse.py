

# ========================= common
def log_trace(func_name):
    print ("\n--- " + func_name + "()")
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return

def solution(jsonData):
    tmp_numbedrooms = []
    i_num_bedroom = 0
    #print (len(jsonData))
    if (len(jsonData) == 0):
        return tmp_numbedrooms

    for each_row in jsonData:
        i_num_bedroom = 0
        #print (each_row)
        #print(each_row.get("unit"))
        p_desc = each_row.get("description")
        #print ("")
        #print(p_desc)
        if (p_desc.find("studio") >= 0): # "studio" found
            #print("studio")
            if (p_desc.find("yoga studio") >= 0):
                i_num_bedroom = 1
        else: # apartment
            i_num_bedroom = 1

        tmp_numbedrooms.append(i_num_bedroom)

    #print (tmp_numbedrooms)
    return tmp_numbedrooms



# ========================= main
jsonData = [{"id": "1", "agent": "Radulf Katlego", "unit": "#3", "description" : "This luxurious studio apartment is in the heart of downtown.", "num_bedrooms": 1},{"id": "2", "agent": "Kelemen Konrad", "unit": "#36", "description": "We have a 1-bedroom available on the third floor.", "num_bedrooms": 1},{"id": "3", "agent": "Ton Jett", "unit": "#12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num_bedrooms": 1},{"id": "4", "agent": "Fishel Salman", "unit": "#13", "description": "Beautiful studio with a nearby art studio.", "num_bedrooms": 1}]

num_bedrooms = solution(jsonData)
print ("num bedrooms:")
print(num_bedrooms)


import math
def log_trace(func_name):
    print ("\n--- " + func_name)
    #print (inspect.stack()[1][3])
    #frame = inspect.currentframe()
    #print (inspect.getframeinfo(frame).function)
    #print(inspect.getframeinfo(inspect.currentframe()).function)
    return


# ---- json
#import json
def TEST_json():
    # from json to python
    json_1 = '{ "name":"jim", "dept":"sales", "age":30, "city":"scranton"}'
    parse_json_1 = json.loads(json_1)
    print(parse_json_1["city"])

    # from python to json
    pyt_obj = {
        "name": "pam",
        "age": 29,
        "location": "front",
        "city": "philly"
    }
    pam_json_obj = json.dumps(pyt_obj)
    print (pam_json_obj)

    #back to python
    pam_pyt_obj = json.loads(pam_json_obj)
    print (pam_pyt_obj["location"])

    return

# ------ main
TEST_json()



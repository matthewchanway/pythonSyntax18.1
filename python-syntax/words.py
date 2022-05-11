

# list = ["cat","dog","mouse","rabbit"]
# for item in list:
#     print(item.upper())
 

# def print_upper_words(a):
#     for item in a:
#         print(item.upper())

# def print_upper_words(a):
#     for item in a:
#         if (item.startswith("e",0,1)) or (item.startswith("E",0,1)): print(item.upper())

b=("c","d","g")
a=["hello","cat","dog","you","goodbye"]

def print_upper_words_v2(list,must_start_with):
    for item in list:
        if (item.startswith(must_start_with,0,1)) or (item.startswith(must_start_with,0,1)): print(item.upper())   

print_upper_words_v2(a,b) 



	
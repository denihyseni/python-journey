try:
    a_dic = {'key' : 'value'}
    print(a_dic["sdsdsdsdsdsd"])
except KeyError as error_message:
    print(f"That key {error_message} doesnt exist")
    print(type(error_message))
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('This is an error i made up')







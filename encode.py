import base64 
print"______ _   _ ______   _   _ _     _"
print"| ___ \ | | || ___ \ | | | (_)   | |"          
print"| |_/ / |_| || |_/ / | |_| |_  __| | ___ _ __" 
print"|  __/|  _  ||  __/  |  _  | |/ _` |/ _ \ '__|"
print"| |   | | | || |     | | | | | (_| |  __/ |   "
print"\_|   \_| |_/\_|     \_| |_/_|\__,_|\___|_|   \n"
source_file=raw_input("Enter the name of file>>")
f = open(str(source_file), "r")
source_code=f.read()
php_code=source_code.replace('<?php', '')
php_code=php_code.replace('?>', '')
sample_string = str(php_code)
sample_string_bytes = sample_string.encode("ascii") 
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 
source_code_compiled="<?php $code_compiled_in_pys='"+base64_string+"';eval(base64_decode($code_compiled_in_pys));?>"
with open("encoded_"+str(source_file), "w") as text_file:
    text_file.write(source_code_compiled)
print("File secured:Success\n")
print("Comiled to >>"+"encoded_"+str(source_file))


# Which extensions it can see :
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# modify the code a lil it can easily do big stuff

user_input = input("File name: ").lower()
for char in (user_input):
    if char == "":
        user_input = user_input.lstrip(" ")
    else:
        break
for char in reversed(user_input):
    if char == " ":
        user_input = user_input.rstrip(" ")
    else:
        break
    
count = 0
for char in reversed(user_input):
    if char == ".":
        break
    count -= 1
if (count == -4):
    ext = user_input[count:]
    if ext in ["jpeg"]:
       print("image/jpeg")
elif(count == -3):
    ext = user_input[count:]
    if ext in ["gif"]:
        print("image/gif")
    elif ext in ["jpg"]:
        print("image/jpeg")
    elif ext in ["png"]:
        print("image/png")
    elif ext in ["zip"]:
        print("application/zip")
    elif ext in ["txt"]:
        print("text/plain")
    elif ext in ["pdf"]:
        print("application/pdf")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
# change url  to channel.zip --> download a zip file that contains a readme.txt
import re
import zipfile

channel_zip_file = zipfile.ZipFile("channel.zip")
file_name = str(90052)
commentList = []

while file_name != "":
    f = open("channel/"+ file_name + ".txt", "r")
    data = f.read()
    print(data)
    number = re.findall(r'\d+', data)
    commentList.append(channel_zip_file.getinfo(file_name + ".txt").comment.decode('ascii'))
    if number != []:
        file_name = str(number[0])
    else:
        break

print(''.join(commentList))


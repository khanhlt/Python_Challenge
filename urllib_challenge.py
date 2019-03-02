import urllib.request
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
html = ""
for i in range(400):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        print(str(i) + "\t" + html)
        code = re.findall(r'\d+', html)
        if (i == 84):
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+ str(int(re.findall(r'\d+', html)[0])/ 2)
        elif (i == 139):
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + re.findall(r'\d+', html)[1]
        elif (code == []):
            break
        else:
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+ re.findall(r'\d+', html)[0]

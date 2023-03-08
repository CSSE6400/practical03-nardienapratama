from requests import request

res = request(method="GET", url="https://www.google.com")

print("request status")
print(res.status_code)
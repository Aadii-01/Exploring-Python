import requests
from datetime import datetime
Username = "Your_username_here"
Token = "Your_token_here"

"""Playing with pixela"""
pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token" : Token,
    "username" : Username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# resp = requests.post(url = pixela_endpoint, json = params)
# print(resp.text)

"""Creating a graph"""
# graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"
# graph_params = {
#     "id" : "sheet1",
#     "name" : "Walking Graph",
#     "unit" : "Km",
#     "type" : "float",
#     "color" : "sora"
# }
# header = {
#     "X-USER-TOKEN" : Token,
# }
# requests.post(url = graph_endpoint,json = graph_params, headers = header)

now = datetime.now()


"""Post a pixel in sheet1"""
graph_endpoint = f"{pixela_endpoint}/{Username}/graphs/sheet1"
sheet1_params = {
    "date" : now.strftime("%Y%m%d"),
    "quantity" : "3.75",
}
header = {
    "X-USER-TOKEN" : Token,
}
resp = requests.post(url = graph_endpoint, json = sheet1_params, headers= header)
print(resp.status_code)

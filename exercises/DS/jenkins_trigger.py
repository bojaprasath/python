import requests

url = "https://engci-private-sjc.cisco.com/jenkins/tesseract/job/CD/job/MAGLEV/job/common/job/Testing-Shyam-shyg/job/SingleNode/buildWithParameters"

querystring = {"MAGLEV_VERSION":"1.4.0.90"}

# auth = HTTPBasicAuth('shyg','11f4bccb3d0aca0dd3fb9d4a9b5c6626bf');

# userAndPass = base64.b64encode(b"username:password").decode("ascii")
# headers = { 'Authorization' : 'Basic %s' % userAndPass  }

# headers = {
#     'Accept': "*/*",
#     'Accept-Encoding': "gzip, deflate",
#     'Content-Length': "0",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache",
#     'Authorization': auth,
#
#     }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
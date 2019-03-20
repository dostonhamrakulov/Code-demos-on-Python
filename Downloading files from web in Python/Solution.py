# Step_1:  imported the requests library
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

# Step_2: URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object

# Step_3: send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:

	# Saving received content as a png file in
	# binary format

	# Step_4: write the contents of the response (r.content)
	# to a new file in binary mode.
	f.write(r.content)

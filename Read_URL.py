import requests

# Define the response object with the image URL
URL_content = requests.get('https://sdtimes.com/wp-content/uploads/2018/12/python-logo-master-v3-TM-flattened-490x166.png')

# Save the URL content in the specified location
with open(r'C:\Users\ASUS\Documents\Images\new.png','wb') as f:
    f.write(URL_content.content)

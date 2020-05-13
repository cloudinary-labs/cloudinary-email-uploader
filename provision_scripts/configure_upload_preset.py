import os,sys,json

import cloudinary
import cloudinary.api
from cloudinary.utils import cloudinary_url

#check what is the upload preset
upload_preset = str(os.environ.get('UP_PRESET', 'email_uploader'))

'''
check if the requested upload preset exists?
if it's found we will update it to suit our needs
'''
try:
	up_found = cloudinary.api.upload_preset(upload_preset)
	print('An upload preset by the configured name already exsists: ',up_found)
	print('Will update it to suit the app needs')
	try:
		result = cloudinary.api.update_upload_preset(
			name = upload_preset,
			unsigned = 'true', 
			tags = "upload_by_email", 
			use_filename = 'true', 
			unique_filename= 'true', 
			type = 'upload'
		)
		print(result)

	except Exception as e:
		print('Failed to update upload preset', e)
#if we hit this exception then the requested name is free for us to use
#and we will use it to create the upload preset
except cloudinary.exceptions.NotFound as e:
	try:
		result = cloudinary.api.create_upload_preset(
			name = upload_preset,
			unsigned = 'true', 
			tags = "upload_by_email", 
			use_filename = 'true', 
			unique_filename= 'true', 
			type = 'upload'
		)
		print(result)

	except Exception as e:
		print('Failed to create upload preset', e)

import os,sys,json

import cloudinary
import cloudinary.api
from cloudinary.utils import cloudinary_url

#check what is the upload preset
upload_preset = str(os.environ.get('UP_PRESET', 'email_uploader'))

'''
This is a cleanup script
check if the requested upload preset exists?
if it's found we will delete it
'''
try:
	up_found = cloudinary.api.upload_preset(upload_preset)
	print('An upload preset by the configured name was found, we will try and remove it')

	#attempt the removal of the upload preset
	try:
		result = cloudinary.api.delete_upload_preset(
			name = upload_preset,
		)
		print(result)
	except Exception as e:
		print('Failed to delete upload preset', e)

#should an execution removal exception happen print out for debug
except Exception as e:
	print(e)
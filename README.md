# cloudinary-email-uploader

# What is this tool?
	A standalone state-less app which will listen for a webhook coming from sendgrid incoming parser.
	once such a hook in incoming it will ingest the hook contents and upload it to cloudinary as a base 64 asset.

	This app is part of a full flow desriced in a blog by cloudinary.

# What do we need to make it work? (Requirements)
	1. A Cloudinary account - Yes, a free one is just fine for this app to work.
	if you have yet to get one, you can sign up [here](https://cloudinary.com/signup)

	2. A Sendgrid account - Yes, a free account will do just fine and will provide you with all the options in this example
	if you have yet to get one, you can sign up [here](https://signup.sendgrid.com/)

	3. A domain of your own you can manage.
	you will need to add some records to it (MX records) telling the world you have an "email server" listening on thet place

	4. A place to run your code, we used heroku since we like it, but really any sort of service will do.
	Should you choose heroku a free account will do just fine.
	if you have yet to get one, you can sign up [here](https://signup.heroku.com/)

# How to make it work? (The wiring stage)
	1. You need to deploy a version of this code in your selected service provider (we used Heroku)
	choosing a name for the app will provide you with a url of it, Keep it!

	2. In your cloudinary account setup an "unsigned upload preset".

	3. Login to your sendgrid account and setup an incoming parse flow at [Settings --> Inbound Parse](https://app.sendgrid.com/settings/parse)
	you will need to follow the instructions to add your domain, the whole process should not take more then 5 minutes
	during that process you will add the MX record to your domain.
	once the enrollment process is done you will be able to add a "Host & URL"
		the host will be the value you used in your MX record i.e. "upload.your-domain.com"
		the URL will be the value you got when you deployed your app i.e. "https://your-app.herokuapp.com/"
		be sure to check the 2 boxes to activate the spam filter and forwarding the full MIME content.

	4. Send a test email to your self !
		the format is cloudname@upload.your-domain.com
		the attached images should be a vailable in your cloudinary account in a moment


# Deploying the code
Looking at the what you are looking to achive you can do one of two things:
- Deploy It:
	Click the deploy button and have a deployment of your own of this code.
	[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/talknopf/cloudinary-email-uploader)
- Improve It:
	Clone this repository and start playing around with this basic example of code.
	you might want to customize this example and make it more suitable to your needs
	or you might find a bug and you wish to suggest a PR with a fix or an improvement (both are welcome).
	```bash
	git clone https://github.com/talknopf/cloudinary-email-uploader
	cd cloudinary-email-uploader
	pip install -r requirements.txt
	python cld-email-uploader.py
	```
	The local development environment will utilize port 80

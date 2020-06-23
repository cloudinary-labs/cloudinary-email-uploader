## What Is This Tool?
This tool, **cloudinary-email-uploader**, is a stand-alone, stateless app that listens for a webhook from SendGrid’s incoming parser. After detecting such a hook, the app ingests and uploads the content to Cloudinary as a Base64 asset.

cloudinary-email-uploader is part of a workflow described in this [post](https://cloudinary.com/blog/securely_uploading_images_to_cloudinary_by_email) in the Cloudinary blog.
## How Can You Get the Tool?

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-email-uploader)

By clicking the above button, you—

1. Deploy the latest code of cloudinary-email-uploader to your Heroku account.
2. Configure the upload preset in Cloudinary.
3. Create a free SendGrid account and attach it to the generated dyno (a container in Heroku lingo), which is a building block that powers the Heroku app cloudinary-email-uploader.

Afterwards, attach your domain to SendGrid and perform the configuration steps below.
### Setting Up the Prerequisites 
Set up the following:

**A Cloudinary account.** [Sign up for a free account](https://cloudinary.com/signup), which is adequate for your purpose. Clicking the **Deploy to Heroku**' button elicits a prompt for your Cloudinary URL, which enables the application-deployment script to build all the Cloudinary-related configurations for you. Any time you delete cloudinary-email-uploader, it will “clean up after itself,” i.e., remove the upload preset from your Cloudinary account and the SendGrid account the app created.

**A SendGrid account.** A free account will also suffice. [Sign up on SendGrid](https://signup.sendgrid.com/). Clicking the **Deploy to Heroku** button creates an account for you, which is linked to the deployed instance of the code.

**A network domain of your own.** Be sure to add MX records to tell the world that you have an active email server. SendGrid guides you through that process.

**A server in which to run your code.** Heroku is our choice but feel free to pick another service. A [free Heroku account](https://signup.heroku.com/) will suffice.

### Wiring the Tool

Do the following:

From your Cloudinary dashboard, copy the Cloudinary URL value (without the `CLOUDINARY_URL=` prefix).


Deploy a version of the code in Heroku by clicking the **Deploy to Heroku** button.
Parse the Cloudinary URL you copied and choose a name for the app and for the upload preset to be created for your Cloudinary account.

Subsequent to deployment, cloudinary-email-uploader automatically configures your Cloudinary account, simultaneously creating a Sendgrid account that’s affiliated with the app.


Log in to the SendGrid account by clicking the login link in the cloudinary-email-uploader’s Overview screen under Add-Ons. Next, set up an incoming parse flow by choosing [Settings > Inbound Parse](https://app.sendgrid.com/settings/parse) and then follow the instructions to add your domain.
That enrollment process takes less than five minutes, during which you’ll also add the MX record to your domain.
Now add the following under **Host & URL**:
A host name, which is the value in your MX record, e.g., `upload.your-domain.com`.
A URL, which is the one you received after deploying the app, e.g.,  [`https://your-app.herokuapp.com/`](https://your-app.herokuapp.com/). 
**Important:** Select the two checkboxes to activate the spam filter and forward the full MIME content.
Finally, send a test email to yourself at `cloudname@upload.your-domain.com` along with an image attachment. You’ll see the image in your Cloudinary Media Library within moments.
If you have multiple cloud names (subaccounts), be sure to address your email to the correct one.

### Deploying the Code
Depending on your goal, do either of the following:

* **Deploy the code.** Click the Deploy button for a deployment of your own along with the automation features described in this [Cloudinary post](https://cloudinary.com/blog/securely_uploading_images_to_cloudinary_by_email).
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-email-uploader) 
   
* **Enhance the code.** Clone the repository and play around with that basic example to suit your needs. If you find a bug, we would appreciate your filing a pull request (PR) with a suggestion for a fix or an improvement.


```bash
git clone https://github.com/cloudinary-devs/cloudinary-email-uploader
 cd cloudinary-email-uploader
 pip install -r requirements.txt
 python cld-email-uploader.py
```


Unless you’ve configured the environmental variable `PORT`, the local development environment runs on port 80 by default. Also, you can change the name of the upload preset on the development environment by setting the `UP_PRESET` variable. To facilitate development, both `PORT` and `UP_PRESET` contain default values, as follows:


``` bash
export PORT=80
export UP_PRESET=’email_uploader’
```

# Python Email Sender

This project provides a simple Python script to send an email using Gmail's SMTP server. The script allows you to customize the sender and recipient emails, subject, and message content, and it supports secure SSL connection for safe password handling.

## Prerequisites

- Python 3.x installed
- An email account with **Gmail**
- **App Password** if using 2-Step Verification (recommended for security)

> **Note**: Google requires App Passwords for accounts with 2-Step Verification enabled. If you don’t have 2-Step Verification enabled, you may also need to enable "Less secure app access" in your Google account settings.

## Setup

1. Clone this repository to your local machine:
   git clone https://github.com/Sachin-Tharaka/Mailing_Client.git
   cd python-email-sender

2. Install any dependencies if necessary (though this script only relies on Python's standard library).

3. Create a file named `password.py` in the same directory with the following content:
   password1 = "your_email_password"
   
   Replace `"your_email_password"` with your actual email password or App Password if using Gmail with 2-Step Verification.

5. Replace the placeholder `email_of_the_sender` and `email_of_the_receiver` in the script with your actual sender and receiver email addresses.

## Usage

1. Run the script using the following command:
   python send_email.py
   
2. Upon running the script, it will:
   - Establish an SSL connection to Gmail's SMTP server.
   - Log in to the Gmail account specified as `email_of_the_sender`.
   - Send an email with the specified subject and body to the `email_of_the_receiver`.

## Code Overview

The code makes use of the `smtplib`, `ssl`, and `email.message.EmailMessage` modules:

- `smtplib`: Provides an SMTP client session object that can be used to send mail.
- `ssl`: Used to wrap the SMTP connection in an SSL context for secure email transfer.
- `email.message.EmailMessage`: Used to build and structure the email with custom headers and content.

### Key Sections of the Code

- **EmailMessage Object**: Used to construct the email message with `From`, `To`, `Subject`, and body content fields.
- **SSL Context**: Ensures a secure connection for password protection.
- **SMTP_SSL Connection**: Connects to Gmail's SMTP server with SSL encryption on port 465 and logs in using the provided credentials.

## Example

email_sender = 'sender@gmail.com'
email_receiver = 'receiver@gmail.com'
subject = 'Sample Python Email'
body = """
     Hello,
     This is a test email sent from a Python script!
     Best regards,
     Your Python Script
"""

## Disclaimer

Ensure you handle your credentials securely. Do not hard-code sensitive information directly in the script. This repository is provided as-is without warranty, and it’s recommended to use environment variables or encrypted storage solutions for production use.

## License

This project is open-source and available under the [MIT License](LICENSE).

Replace the placeholders like `your-username`, `python-email-sender`, and any email or password values with actual details relevant to your project.

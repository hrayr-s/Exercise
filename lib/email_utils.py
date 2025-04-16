import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import BytesIO
from typing import Tuple, List, Union

from dotenv import load_dotenv

if __name__ == '__main__':
    # in case if the python file ran directly
    load_dotenv('../.env', override=True)
else:
    load_dotenv('.env')


def make_attachment_from_file(filename: str, file_or_path: Union[str, BytesIO]) -> MIMEBase:
    # Open and attach file
    part = MIMEBase("application", "octet-stream")
    if isinstance(file_or_path, str):
        with open(file_or_path, "rb") as attachment:
            part.set_payload(attachment.read())
    else:
        part.set_payload(file_or_path.read())

    # Encode file and add headers
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )
    return part



def send_email(to: List[str], subject: str, body: str, attachments: List[Tuple[str, Union[str, BytesIO]]] = None) -> None:
    """
    Send email with attachments.
    :param to: receiver
    :param subject: email subject
    :param body: email body
    :param attachments: files to be attached
    """
    # Configuration
    sender_email = "report@hrayr.org"
    to_emails = ', '.join(to)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_emails
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    if attachments:
        for filename, file_or_path in attachments:
            msg.attach(make_attachment_from_file(filename, file_or_path))

    # Send the email
    with smtplib.SMTP_SSL(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as server:
        server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
        for email in to:
            server.sendmail(sender_email, email, msg.as_string())

    print("Email sent successfully.")

if __name__ == '__main__':
    receiver_email = "hrayr.stepanyan.a@gmail.com"
    send_email([receiver_email, 'i@hrayr.am'], "Hello from Python", "Hello from Python!", attachments=[
        ('dummySample.csv', '../data/dummySamples.csv'),
        ('dummyDescSample.csv', '../data/dummyDescSample.csv'),
    ])

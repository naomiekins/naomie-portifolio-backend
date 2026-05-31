import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import APIRouter, HTTPException, BackgroundTasks
from models.schemas import ContactRequest, ContactResponse

router = APIRouter()

SMTP_HOST   = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT   = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER   = os.getenv("SMTP_USER", "")
SMTP_PASS   = os.getenv("SMTP_PASS", "")
OWNER_EMAIL = os.getenv("OWNER_EMAIL", "")


def _send_email(data: ContactRequest):
    if not all([SMTP_USER, SMTP_PASS, OWNER_EMAIL]):
        print(f"[contact] Email not configured. From: {data.email} — {data.message}")
        return
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[Portfolio] {data.subject} — from {data.name}"
    msg["From"]    = SMTP_USER
    msg["To"]      = OWNER_EMAIL
    msg["Reply-To"] = data.email
    msg.attach(MIMEText(
        f"Name: {data.name}\nEmail: {data.email}\nSubject: {data.subject}\n\n{data.message}",
        "plain"
    ))
    msg.attach(MIMEText(f"""
    <html><body style="font-family:sans-serif;max-width:600px;margin:auto;">
      <h2 style="color:#b8922a;">New Portfolio Message</h2>
      <p><strong>Name:</strong> {data.name}</p>
      <p><strong>Email:</strong> <a href="mailto:{data.email}">{data.email}</a></p>
      <p><strong>Subject:</strong> {data.subject}</p>
      <hr/><p>{data.message.replace(chr(10), '<br>')}</p>
    </body></html>""", "html"))
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, OWNER_EMAIL, msg.as_string())
    except Exception as e:
        print(f"[contact] Email send failed: {e}")


@router.post("/", response_model=ContactResponse)
def submit_contact(data: ContactRequest, background_tasks: BackgroundTasks):
    if len(data.name.strip()) < 2:
        raise HTTPException(status_code=422, detail="Please provide your name.")
    if len(data.message.strip()) < 10:
        raise HTTPException(status_code=422, detail="Message is too short.")
    background_tasks.add_task(_send_email, data)
    return ContactResponse(
        success=True,
        message="Thanks for reaching out! I will get back to you soon.",
    )

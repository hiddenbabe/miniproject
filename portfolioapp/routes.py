from flask import Flask,render_template,abort,request,redirect,flash,make_response,session
from flask_mail import Mail, Message
from portfolioapp import myapp,mail

@myapp.route("/")
def home():
   return render_template("index.html")

@myapp.route("/contact/")
def contact():
   return render_template("hireme.html")

@myapp.route("/resume/")
def resume():
   return render_template("resume.html")

@myapp.route("/portfolio/")
def portfolio():
   return render_template("portfolio.html")

@myapp.route("/contactform/")
def contactform():
   fname = request.args.get("name")
   email =  request.args.get("email")
   message = request.args.get("msg")

   msg= Message(subject=f"Work Inquiry From {fname}",sender=email,recipients=[ "izemajebi2@gmail.com"])
   msg.html = f"This message is from {email} - {message}"
   mail.send(msg)
   return "<p alert alert-success>I have received your message and will send you a mail shortly! Looking forward to working with you.</p>"
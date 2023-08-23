from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from VBB_project.settings import EMAIL_PASSWORD


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        useremail = request.POST.get('email')
        phone = request.POST.get('phone')
        areaOfInterest = request.POST.get('areaOfInterest')
        message = request.POST.get('message')
        print(name,useremail,'#######')
        email = MIMEMultipart()
        email.set_unixfrom('author')
        email['From']="noreply@atishkumar.co.in"
        email['To']="atishkumar98@atishkumar.co.in"
        email['Subject'] = 'Details from User VBB Law Firm'
        #   bcc = "siddhu.dhangar@tiss.edu"
        #   mails_to = ' , '.join(mail_from) if True else you
        # subject_txt = 'Registration Confirmation for %s' %(conference_title)
        # subject_txt = 'You are registered as Kalaakaar'
        # BillingName = str(conf_detail_obj.cr_title) + ' ' +  str(conf_detail_obj.cr_fullname) 
        # msg_body = '\n%s,\n\n A payment of Rs.%s received towards the registration fees for the "%s". Thank you for the payment. Your Registration is confirmed and the registration number is %s.\n\n Note: This is an auto-generated mail, please dot not respond to this email.'%(BillingName,request.POST['amt'],conference_title,request.POST['mer_txn'])
        msg_body = f'<h3>User : {name} , {phone} , {areaOfInterest}, {message} <h3><br><img src = "https://kalaakaar.co/static/images/Business-logo.png" style="width:10%;height:10%;">'
        # msg = 'Subject:{}\n\n{}'.format(email['Subject'], msg_body)
        email.attach(MIMEText(msg_body,"html"))
        server = smtplib.SMTP_SSL('smtpout.secureserver.net',465)
        server.ehlo()
        # server.starttls(context=simple_email_context)
        server.login('atishkumar98@atishkumar.co.in',EMAIL_PASSWORD)
        #   server.login('AKIAYNJZLMUQQXPKMG5B','BItsVQqmsAojywKw8YzfvgpMbPyNBhOXgJ1e0Iz/OJB3')
        server.sendmail('atishkumar98@atishkumar.co.in', useremail, email.as_string())
        print('SENT MAIL','FROM',email['From'],email['TO'],useremail ,msg_body)
        server.quit()
    context = {'home':'home'}
    return render(request, "HOME.html",context)

def about_us(request):
    context = {'abouts_us':'about_us'}
    return render(request,'ABOUT_US.html',context)

def whyus(request):
    context = {'whyus':'whyus'}
    return render(request,'whyus.html',context)


def ourteam(request):
    context = {'ourteam':'ourteam'}
    return render(request,'our_team.html',context)


def contact(request):
    context = {'contact':'contact'}
    return render(request,'contact.html',context)
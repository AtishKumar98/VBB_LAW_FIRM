from django.shortcuts import render
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.http import HttpResponse, HttpResponseNotFound
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
        email['From']="noreply@VBBLAWFIRM.co"
        email['To']="atishkumar31518@gmail.com"
        email['Subject'] = 'Mail Details from User VBB Law Firm'
        #   bcc = "siddhu.dhangar@tiss.edu"
        #   mails_to = ' , '.join(mail_from) if True else you
        # subject_txt = 'Registration Confirmation for %s' %(conference_title)
        # subject_txt = 'You are registered as Kalaakaar'
        # BillingName = str(conf_detail_obj.cr_title) + ' ' +  str(conf_detail_obj.cr_fullname) 
        # msg_body = '\n%s,\n\n A payment of Rs.%s received towards the registration fees for the "%s". Thank you for the payment. Your Registration is confirmed and the registration number is %s.\n\n Note: This is an auto-generated mail, please dot not respond to this email.'%(BillingName,request.POST['amt'],conference_title,request.POST['mer_txn'])
        msg_body = f'<h3>Hello Team, User has requested a callback.</h3><br/><br/><b>Kindly note Information given below</b> <br/><br/>Name of the client : {name} , <br/> Phone Number: {phone} , <br/> Interest: {areaOfInterest}, <br/> Messsage: {message} <h3><br> ////Signature////'
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

profiles = {
    'profile1': {
        'name': 'Vinayak Mishra',
        'role': 'Founder',
        'image':'/../static/images/Vinayak_Mishra-removebg-previe_bf@2x.png',
        'description': """
    <h4>The Legal Guardian: Navigating the Complex World of Law</h4>

    <p>Lawyers, often referred to as the architects of justice, are the unsung heroes of our society. They are the individuals who provide a voice to those in need, defending their rights, and ensuring that justice prevails in the face of adversity. Lawyers play a pivotal role in upholding the principles of law and order in our increasingly complex world.</p>

    <h5>A Noble Profession:</h2>

    <p>The legal profession is one of the oldest and most respected callings in human history. Lawyers have existed in various forms in nearly all civilizations, dating back to ancient Greece, Rome, and beyond. The role of lawyers has evolved over time, but their fundamental purpose has remained consistent: to advocate for their clients' rights and uphold the rule of law.</p>

    <h5>Education and Training:</h2>

    <p>Becoming a lawyer is not an easy path. It requires a rigorous educational journey that typically begins with a bachelor's degree in a related field. Most aspiring lawyers then pursue a Juris Doctor (JD) degree from an accredited law school. This graduate-level program is designed to equip students with the legal knowledge and skills necessary to practice law.</p>

    <!-- Add more content as needed -->

    <h5>Conclusion:</h2>

    <p>In a world where legal complexities are ever-present, lawyers stand as the guardians of justice, ensuring that the principles of fairness and equity prevail. They are educators, advisors, advocates, and problem solvers, dedicated to upholding the rule of law and protecting the rights of individuals and organizations alike. With unwavering commitment to ethical principles and an unyielding pursuit of justice, lawyers are an essential pillar of a just and orderly society, making the world a better place, one case at a time.</p>
"""
,
    },
    'profile2': {
        'name': 'Adv. Binita Y. Sharma',
        'role': 'Co-Founder',
        'image':'/../static/images/Adv_binita_Y_Sharma-removebg-p@2x.png',
        'description':"""
    <h4>The Legal Guardian: Navigating the Complex World of Law</h4>

    <p>Lawyers, often referred to as the architects of justice, are the unsung heroes of our society. They are the individuals who provide a voice to those in need, defending their rights, and ensuring that justice prevails in the face of adversity. Lawyers play a pivotal role in upholding the principles of law and order in our increasingly complex world.</p>

    <h5>A Noble Profession:</h2>

    <p>The legal profession is one of the oldest and most respected callings in human history. Lawyers have existed in various forms in nearly all civilizations, dating back to ancient Greece, Rome, and beyond. The role of lawyers has evolved over time, but their fundamental purpose has remained consistent: to advocate for their clients' rights and uphold the rule of law.</p>

    <h5>Education and Training:</h2>

    <p>Becoming a lawyer is not an easy path. It requires a rigorous educational journey that typically begins with a bachelor's degree in a related field. Most aspiring lawyers then pursue a Juris Doctor (JD) degree from an accredited law school. This graduate-level program is designed to equip students with the legal knowledge and skills necessary to practice law.</p>

    <!-- Add more content as needed -->

    <h5>Conclusion:</h2>

    <p>In a world where legal complexities are ever-present, lawyers stand as the guardians of justice, ensuring that the principles of fairness and equity prevail. They are educators, advisors, advocates, and problem solvers, dedicated to upholding the rule of law and protecting the rights of individuals and organizations alike. With unwavering commitment to ethical principles and an unyielding pursuit of justice, lawyers are an essential pillar of a just and orderly society, making the world a better place, one case at a time.</p>
""" ,
    },

     'profile3': {
        'name': 'B D Tripathi',
        'role': 'Lawyer Core-Team',
        'image':'/../static/images/BD_Tripathi-removebg-preview_by@2x.png',
        'description':"""
    <h4>The Legal Guardian: Navigating the Complex World of Law</h4>

    <p>Lawyers, often referred to as the architects of justice, are the unsung heroes of our society. They are the individuals who provide a voice to those in need, defending their rights, and ensuring that justice prevails in the face of adversity. Lawyers play a pivotal role in upholding the principles of law and order in our increasingly complex world.</p>

    <h5>A Noble Profession:</h2>

    <p>The legal profession is one of the oldest and most respected callings in human history. Lawyers have existed in various forms in nearly all civilizations, dating back to ancient Greece, Rome, and beyond. The role of lawyers has evolved over time, but their fundamental purpose has remained consistent: to advocate for their clients' rights and uphold the rule of law.</p>

    <h5>Education and Training:</h2>

    <p>Becoming a lawyer is not an easy path. It requires a rigorous educational journey that typically begins with a bachelor's degree in a related field. Most aspiring lawyers then pursue a Juris Doctor (JD) degree from an accredited law school. This graduate-level program is designed to equip students with the legal knowledge and skills necessary to practice law.</p>

    <!-- Add more content as needed -->

    <h5>Conclusion:</h2>

    <p>In a world where legal complexities are ever-present, lawyers stand as the guardians of justice, ensuring that the principles of fairness and equity prevail. They are educators, advisors, advocates, and problem solvers, dedicated to upholding the rule of law and protecting the rights of individuals and organizations alike. With unwavering commitment to ethical principles and an unyielding pursuit of justice, lawyers are an essential pillar of a just and orderly society, making the world a better place, one case at a time.</p>
""" ,
    },

     'profile4': {
        'name': 'Pritesh H. Sahu',
        'role': 'Lawyer Core-Team',
        'image':'/../static/images/Pritesh_H_Sahu__legal_Executiv@2x.png',
        'description':"""
    <h4>The Legal Guardian: Navigating the Complex World of Law</h4>

    <p>Lawyers, often referred to as the architects of justice, are the unsung heroes of our society. They are the individuals who provide a voice to those in need, defending their rights, and ensuring that justice prevails in the face of adversity. Lawyers play a pivotal role in upholding the principles of law and order in our increasingly complex world.</p>

    <h5>A Noble Profession:</h2>

    <p>The legal profession is one of the oldest and most respected callings in human history. Lawyers have existed in various forms in nearly all civilizations, dating back to ancient Greece, Rome, and beyond. The role of lawyers has evolved over time, but their fundamental purpose has remained consistent: to advocate for their clients' rights and uphold the rule of law.</p>

    <h5>Education and Training:</h2>

    <p>Becoming a lawyer is not an easy path. It requires a rigorous educational journey that typically begins with a bachelor's degree in a related field. Most aspiring lawyers then pursue a Juris Doctor (JD) degree from an accredited law school. This graduate-level program is designed to equip students with the legal knowledge and skills necessary to practice law.</p>

    <!-- Add more content as needed -->

    <h5>Conclusion:</h2>

    <p>In a world where legal complexities are ever-present, lawyers stand as the guardians of justice, ensuring that the principles of fairness and equity prevail. They are educators, advisors, advocates, and problem solvers, dedicated to upholding the rule of law and protecting the rights of individuals and organizations alike. With unwavering commitment to ethical principles and an unyielding pursuit of justice, lawyers are an essential pillar of a just and orderly society, making the world a better place, one case at a time.</p>
""" ,
    },

     'profile5': {
        'name': 'Adv. Himanshu S. Mishra',
        'role': 'Lawyer Core-Team',
        'image':'/../static/images/BD_Tripathi-removebg-preview_by@2x.png',
        'description':"""
    <h4>The Legal Guardian: Navigating the Complex World of Law</h4>

    <p>Lawyers, often referred to as the architects of justice, are the unsung heroes of our society. They are the individuals who provide a voice to those in need, defending their rights, and ensuring that justice prevails in the face of adversity. Lawyers play a pivotal role in upholding the principles of law and order in our increasingly complex world.</p>

    <h5>A Noble Profession:</h2>

    <p>The legal profession is one of the oldest and most respected callings in human history. Lawyers have existed in various forms in nearly all civilizations, dating back to ancient Greece, Rome, and beyond. The role of lawyers has evolved over time, but their fundamental purpose has remained consistent: to advocate for their clients' rights and uphold the rule of law.</p>

    <h5>Education and Training:</h2>

    <p>Becoming a lawyer is not an easy path. It requires a rigorous educational journey that typically begins with a bachelor's degree in a related field. Most aspiring lawyers then pursue a Juris Doctor (JD) degree from an accredited law school. This graduate-level program is designed to equip students with the legal knowledge and skills necessary to practice law.</p>

    <!-- Add more content as needed -->

    <h5>Conclusion:</h2>

    <p>In a world where legal complexities are ever-present, lawyers stand as the guardians of justice, ensuring that the principles of fairness and equity prevail. They are educators, advisors, advocates, and problem solvers, dedicated to upholding the rule of law and protecting the rights of individuals and organizations alike. With unwavering commitment to ethical principles and an unyielding pursuit of justice, lawyers are an essential pillar of a just and orderly society, making the world a better place, one case at a time.</p>
""" ,
    },
}

def profile_view(request, profile_id):
    profile_data = profiles.get(profile_id)
    if profile_data:
        context = {'profile': profile_data,'ourteam':'ourteam'}
        return render(request, 'Profile.html', context)
    else:
        # Handle the case when the requested profile doesn't exist
        return render(request, 'profile_not_found.html')

def contact(request):
    context = {'contact':'contact'}
    return render(request,'contact.html',context)
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
        'role': 'Advocate Bombay High Court and Supreme Court of India.',
        'image':'/../static/images/Vinayak_Mishra.png',
        'description': """
   

    <p>Adv. Vinayak D. Mishra, an esteemed legal luminary, stands as a founding partner at VBB Legal, where his profound expertise in criminal law shines brightly. Renowned for his specialization in criminal matters, Adv. Vinayak D. Mishra is a distinguished practitioner whose legal prowess extends to various jurisdictions, encompassing a diverse array of criminal legal proceedings.</p>

    
    <p>Within the expansive landscape of legal practice, Adv. Vinayak D. Mishra has earned distinction in Criminal and Civil litigation across Magistrate and Session Courts, High Court advocacy, Consumer Court disputes, Real Estate Regulatory Authority (RERA) matters, and Debt Recovery Tribunal (DRT) cases. His exceptional legal acumen shines most notably in his mastery of criminal law, where his expertise includes handling bail, anticipatory bail matters, post-criminal writ petition proceedings, special leave petitions, and execution proceedings.</p>



    <p>Clients entrust their most intricate criminal cases to Adv. Vinayak D. Mishra, seeking his adept counsel and representation in Session Courts, High Courts, and even the exalted precincts of the Supreme Court. His remarkable success record in securing bail and anticipatory bail, coupled with his proficiency in post-criminal writ petition matters, special leave petitions, and execution proceedings, underscores his prowess in strategic advocacy and his unwavering commitment to justice.</p>

    <!-- Add more content as needed -->

    

    <p>As a founding partner at VBB Legal, Adv. Vinayak D. Mishra epitomizes an unparalleled commitment to client welfare, transcending conventional legal boundaries. His personalized guidance and steadfast support provide clients with a sense of empowerment as they navigate the intricacies of the legal system, including specialized proceedings such as special leave petitions and execution matters. His exceptional communication skills and profound dedication to justice have solidified his standing as an esteemed and sought-after legal practitioner.
</p>
<p>
An influential figure in Mumbai, Thane, Navi Mumbai, and surrounding areas, Adv. Vinayak D. Mishra's stature within the legal fraternity reflects his unwavering pursuit of excellence. His exceptional mastery of criminal law, spanning bail, anticipatory bail, post-criminal writ petition proceedings, special leave petitions, and execution matters, distinguishes him as a legal professional of exceptional repute.
</p>
"""
,
    },
    'profile2': {
        'name': 'Adv. Binita Y. Sharma',
        'role': 'Co-Founder',
        'image':'/../static/images/Adv._Binita_Y. Sharma.png',
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
        'name': 'Adv. Dhwani S. Rughani',
        'role': 'A Rising Advocate',
        'image':'/../static/images/BD_Tripathi-removebg-preview_by@2x.png',
        'description':"""
    <h4>Dhwani S. Rughani, a dynamic advocate at VBB Legal, shines as a promising newcomer in the legal arena.</h4>

    <p>Dhwani's dedication to justice is evident through her areas of expertise:<br/>

Intellectual Property Law: Skillfully navigating the complexities of patents, trademarks, and copyrights.<br/>
Medical Negligence Cases: Fearlessly advocating for clients affected by medical malpractice, ensuring their voices are heard.<br/>
Cases Against Government: Tenaciously safeguarding individual rights in legal battles against state and central government entities.<br/>
As a fresh advocate, Dhwani's impact is felt at VBB Legal, where her commitment to ethics and diligence align seamlessly with the firm's values. With each case she handles, Dhwani demonstrates an unwavering commitment to justice and a promising future in the legal profession.</p>
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

def our_services(request):
    context = {'our_services':'our_services'}
    return render(request,'our_services.html',context)
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
        'name': 'Adv. Vinayak Mishra',
        'desg': 'Founder and Partner - VBB Legal',
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
        'desg': 'Founder and Partner - VBB legal',
        'role': 'Advocate Bombay High Court and Supreme Court of india',
        'image':'/../static/images/Adv._Binita_Y. Sharma.png',
        'description':"""

    <p>Adv. Binita Sharma, co- founder and partner of VBB Legal is a distinguished legal professional with a wealth of experience across diverse legal domains. Her extensive practice encompasses High Court litigation, Consumer Court disputes, Real Estate Regulatory Authority (RERA) matters, Debt Recovery Tribunal (DRT) cases, and a comprehensive range of Civil and Criminal proceedings in Magistrate and Session Courts.<br>

With a proven track record of successfully representing clients in these varied jurisdictions, Adv. Binita Sharma is renowned for her strategic acumen, meticulous approach, and unwavering commitment to securing favorable outcomes. Her deep understanding of the intricacies of each legal area allows her to offer comprehensive and tailored solutions to clients seeking resolution in complex legal landscapes.<br>

Adv. Binita Sharma's dedication to client advocacy extends beyond the courtroom. She is a trusted advisor who goes the extra mile to educate and empower clients, ensuring they make well-informed decisions. Her exceptional communication skills, combined with a passion for justice, make her a sought-after legal professional.<br>

Based in Mumbai, Thane, Navi Mumbai, and surrounding areas, Adv. Binita Sharma has earned respect and recognition within the legal community. Her reputation is a testament to her unwavering pursuit of excellence and her ability to navigate the legal intricacies of High Court proceedings, Consumer Court matters, RERA disputes, DRT cases, and the full spectrum of Civil and Criminal litigation in Magistrate and Session Courts.</p>
""" ,
    },

     'profile3': {
        'name': 'B D Tripathi',
        'desg': 'Senior Associate',
        'role': 'Advocate Bombay High Court and Supreme Court of India.',
        'image':'/../static/images/B_D_Tripathi.png',
        'description':"""

    <p>With an illustrious career spanning 28 years, Adv. B.D. Tripathi stands as a distinguished senior legal counsel at VBB Legal, a prominent law firm based in Mumbai and Navi Mumbai. A stalwart in the field of law, Adv. Tripathi has garnered unparalleled experience across a spectrum of legal domains, ranging from criminal and civil litigation to intricate matters in banking, insurance, labor law, PF, ESIC, income tax, and corporate laws.<br>

Renowned for their formidable presence in courtrooms, Adv. Tripathi has masterfully represented clients at all levels of the judiciary, including appearances before the esteemed Supreme Court of India. Their legal acumen extends further to encompass industrial matters, NDPS cases, FEMA, and PMLA, reflecting a profound understanding of intricate legal frameworks.<br>

A visionary legal mind, Adv. Tripathi's profound expertise and unwavering commitment have earned them a well-deserved reputation as a guiding force in the legal realm. Their contributions extend beyond legal circles, making a lasting impact on the lives of individuals and the broader legal landscape. As a senior legal counsel at VBB Legal, Adv. B.D. Tripathi continues to navigate complex legal challenges with finesse, setting a benchmark for excellence in the legal profession.</p>
""" ,
    },

     'profile4': {
        'name': 'Pritesh H. Sahu',
        'desg': 'Legal Associate',
        'role': 'Advocate Bombay High Court',
        'image':'/../static/images/Pritesh_H_Sahu.png',
        'description':"""

    <p>Adv. Pritesh Sahu is an accomplished legal professional associated with VBB Legal and recognized for their expertise in civil and criminal matters.<br>
      With a robust presence in the Bombay High Court, Adv. Sahu brings a wealth of knowledge and experience to the forefront of legal proceedings.<br>
        Their adept handling of intricate legal issues, combined with a commitment to justice, has earned them a reputation as a dependable advocate.<br>
          With a focus on delivering favorable outcomes for clients, Adv. Pritesh Sahu continues to make significant contributions within the realm of law, setting a remarkable standard of excellence.</p>
""" ,
    },

     'profile5': {
        'name': 'Adv. Dhwani S. Rughani',
        'desg': 'Legal Associate',
        'role': 'Advocate Bombay High Court',
        'image':'/../static/images/B_D_Tripathi.png',
        'description':"""

    <p>
    Dhwani S. Rughani, a dynamic advocate at VBB Legal, shines as a promising newcomer in the legal arena.
    Dhwani's dedication to justice is evident through her areas of expertise:<br/>

Intellectual Property Law: Skillfully navigating the complexities of patents, trademarks, and copyrights.<br/>
Medical Negligence Cases: Fearlessly advocating for clients affected by medical malpractice, ensuring their voices are heard.<br/>
Cases Against Government: Tenaciously safeguarding individual rights in legal battles against state and central government entities.<br/>
As a fresh advocate, Dhwani's impact is felt at VBB Legal, where her commitment to ethics and diligence align seamlessly with the firm's values. With each case she handles, Dhwani demonstrates an unwavering commitment to justice and a promising future in the legal profession.
</p>
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
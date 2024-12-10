from django.shortcuts import render
from .models import Cards
# data={'one':'''MANILA, Philippines – Nurses, engineers, doctors – now cybersecurity experts. As the Philippines counts the cost of brain drain, a surge in malicious cyber activity has highlighted the country’s digital security skills gap.

# US cybersecurity firm Resecurity reported a 325% jump in hacking and other digital intrusions targeting the Philippines during the first quarter of 2024 amid rising tensions with China, largely over disputed territory in the South China Sea.

# That prompted President Ferdinand Marcos Jr to launch a cybersecurity strategy to beef up the nation’s cyber defenses to combat attacks and digital crimes. Its military said last year it would create a cyber command.

# But industry analysts say such plans could struggle due to big shortages of skilled “cyber warriors” in the Philippines, which is estimated to need tens of thousands of digital security professionals.,'''

# 'two':'''Almost four years since the Privacy Act review commenced, the Australian government has introduced a reform bill that fails to make most of the fundamental changes needed to modernise our privacy laws.

# Attorney-General Mark Dreyfus said in May that the government would introduce legislation to reform a privacy regime that’s “woefully outdated and unfit for the digital age”.

# But the new bill doesn’t touch most of the substantive principles in our privacy law, originally passed in 1988 and largely unchanged since then. This was an era long before our everyday lives were conducted via the internet or smartphones.'''}
# Create your views here.
def display(request):
    data=Cards.objects.all().order_by('id')
    context={
        'data':data
    }
    return render(request,'index.html',context)

def details(request,pk):
    data1=Cards.objects.get(id=pk)
    context={
        'data1':data1
    }
    return render(request,'details.html',context)

def about(request):
    return render(request,'about.html')

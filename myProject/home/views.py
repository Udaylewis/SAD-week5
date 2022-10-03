from re import TEMPLATE
from django.shortcuts import render

TEMPLATE = (
    'os.path.join(BASE_DIR, "templates"),'
)

def hello(req):
    return render(req, "index.html")
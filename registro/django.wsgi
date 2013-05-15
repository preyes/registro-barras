ALLDIRS = ['home/pablo/ENV1/lib/python2.7/site-packages']

import os, sys
import site

# Remember original sys.path.

#sys.path('home/pablo/ENV1/registro/registro') 

# Add each new site-packages directory.
#for directory in ALLDIRS:

site.addsitedir('home/pablo/ENV1/lib/python2.7/site-packages')
sys.path.append('/home/pablo/ENV1/registro/registro')  
sys.path.append('/home/pablo/ENV1/registro/')



#activate_this = os.path.join("home/pablo/ENV1", "bin/activate_this.py")
#execfile(activate_this, dict(__file__=activate_this))


#new_sys_path = [p for p in sys.path if p not in prev_sys_path]

#for item in new_sys_path:
 #   sys.path.remove(item)
#sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'registro.settings'

import django.core.handlers.wsgi 

application = django.core.handlers.wsgi.WSGIHandler()



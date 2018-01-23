#!/usr//bin/python

import uuid
import string
import datetime 
import random
from random import randrange
from random import randint


LASTNAME_FILE = "last.txt"
FIRSTNAME_FILE = "first.txt"
STATES = "AK,AL,AR,AZ,CA,CO,CT,DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA,MD,ME,MI,MN,MO,MS,MT,NC,ND,NE,NH,NJ,NM,NV,NY,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VA,VT,WA,WI,WV,WY"
STATES = STATES.split(",")
DELIMITER = ","

#Load name lists
with open(LASTNAME_FILE) as f:
    lastnames = f.readlines()
lastnames = [x.strip() for x in lastnames]

with open(FIRSTNAME_FILE) as f:
    firstnames = f.readlines()
firstnames = [x.strip() for x in firstnames]

#l = random.choice(lastnames)
#f = random.choice(firstnames)
#print "%s %s" % (f.title() , l.title()) 
#print "account_id,driver_id,first_name,last_name,age_first_licensed,carpool_usage,certificate_of_financial_responsibility_required,current_active_violations,driver_passed_safedriving,driver_resident_student,driver_retired,drivers_license_state,good_driver_discount,good_student_discount,updated_ts"

account_id = 10000
while account_id <= 20000:
   drivers = randint(1, 4)
   count = 0
   last_name = random.choice(lastnames).title()
   drivers_license_state = random.choice(STATES)
   while count < drivers:
       driver_id = str(uuid.uuid4())
       first_name = random.choice(firstnames).title()
       age_first_licensed =  randint(16,25)
       carpool_usage = bool(random.getrandbits(1))
       certificate_of_financial_responsibility_required = bool(random.getrandbits(1))
       current_active_violations = randint(0,3)
       driver_passed_safedriving = bool(random.getrandbits(1))
       driver_resident_student = bool(random.getrandbits(1))
       driver_retired = bool(random.getrandbits(1))
       good_driver_discount = bool(random.getrandbits(1))
       good_student_discount = bool(random.getrandbits(1))
       updated_ts = randint(1451606400000,1516406400000)
       contact_id = str(uuid.uuid4())
       contact_phone_home = str(randint(100,700)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))
       contact_phone_cell = str(randint(100,700)) + "-" + str(randint(100,999)) + "-" + str(randint(1000,9999))
       contact_email_address = first_name + "." + last_name + "@emaildomain.local"
       contact_state = drivers_license_state 
       contact_info = "\"{contact_id:" + contact_id + ", phone_home: " +  contact_phone_home + ",phone_cell:" + contact_phone_cell + ",email_address:" + contact_email_address + ",state:" + contact_state + "\"}"
       row =  account_id, driver_id , first_name , last_name , age_first_licensed , carpool_usage , certificate_of_financial_responsibility_required , current_active_violations , driver_passed_safedriving , driver_resident_student , driver_retired , drivers_license_state , good_driver_discount , good_student_discount, updated_ts, contact_info
       print ','.join(str(o) for o in row)
       count = count + 1
   account_id = account_id + 1


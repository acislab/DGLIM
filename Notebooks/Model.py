from peewee import *

db = MySQLDatabase('DGLIM_Data',host='127.0.0.1',port=3306,user='root')

# Active Business Model

class ActiveBusiness(Model):
    id = IntegerField(primary_key=True)    #1
    business_type = CharField()            #2
    name = CharField()                    
    start_date = CharField()                    
    address = CharField()                    
    latitude = CharField()                    
    longitude = CharField()                #7 fields

    class Meta:
        database = db
        db_table= 'act_bus_geocoded'

# PERMIT MODEL

class Permit(Model): 
    id = IntegerField(primary_key=True)
    permit = CharField()
    classification = CharField()
    name = CharField()
    parcel_number = CharField()
    contractor_last_name = CharField()
    contractor_first_name = CharField()
    business = CharField()
    primary_party = CharField()
    submit_date = CharField()
    issue_date = CharField()
    location = CharField()
    latitude = CharField()
    longitude = CharField()
    
    class Meta:
        database = db
        db_table = "permit"

# Tract Model

class Tract(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    total_businesses = IntegerField()
    successful_businesses = IntegerField()

    class Meta:
        database = db
        db_table = "tract"

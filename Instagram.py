# thanasxda @ github - instagram osint maltego transform wip

# imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
import requests
import json

class instagram_data(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        
        # obtain target info
        request_username = request.getProperty("person.name")
        if bool(request_username) == False:
            request_username = ''
        
        # instagram api
        instagram_url = 'https://www.instagram.com/'+request_username+'?__a=1&__d=dis'
        
        api_response = requests.get(instagram_url)
        instagram_data = api.response.json()
        instagram_data = (instagram_data['graphql']['user'])
        
        # extract info 
        for i in instagram_data:
            
            # create instagram entity
            instagram_data_entity = response.addEntity("maltego.affiliation.Instagram")
            
            # add properties to instagram entity
            response_username = i.get("username")
            if response_username:
                instagram_data_entity.addProperty("person.name", value = response_username)
            
            #response_full_name = i.get("full_name")
            #if response_full_name:
            #    instagram_data_entity.addProperty("FullName", value = response_full_name)

            #response_fbid = i.get("fbid")
            #if response_fbid:
            #    instagram_data_entity.addProperty("FbID", value = response_fbid)
                
            ##response_photo = i.get('profile_pic_url_hd')
            ##if response_photo:
            ##    instagram_data_entity.addProperty("PhotoURL", value = response_photo['href'])

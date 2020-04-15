import requests
from wit import Wit


#access token from wit.api site cinfo
access_token='D5P2KVKDHWAAC64JPZXLEIECFBHDPZL3'


client=Wit(access_token=access_token)



def wit_response(message_text):
    resp= client.message(message_text)
    entity=None
    value=None

    try:
        entity=list(resp['entities'])[0]
        value=resp['entities'][entity][0]['value']
        
    except:
        pass
    

    return(entity,value)
    


def covid_info(message_text):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":message_text}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "4c95a52ef8msh414931972ca834ap17f789jsnabff3f0eeacc"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data=response.json()
    result=data['response']
    for r in result:
        #print(r)
        elements=[]
        element={
                'country':r['country'],
                'cases_new':r['cases']['new'],
                'cases_active':r['cases']['active'],
                'cases_critical':r['cases']['critical'],
                'cases_recovered':r['cases']['recovered'],
                'cases_total':r['cases']['total'],
                'deaths_new':r['deaths']['new'],
                'deaths_total':r['deaths']['total'],
                'tests_total':r['tests']['total'],
                'day':r['day']
        }
        elements.append(element)
        
        #return(cases_new,cases_active,cases_critical,cases_recovered,cases_total,deaths_new,deaths_total,tests_total)
        return(elements)
        
    
print(covid_info("nepal"))


#print(wit_response("mero ghar nepal ma ho"))


import sys 
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict): 
    authenticator = IAMAuthenticator("7TLFNDHyGDiH9kdJL5o9dcZXnOFLirzNDphc3QALa9YM")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://f8685ea3-666e-43c4-9ef5-b7ef5d7189de-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
                db='reviews',
                selector={'dealership': {'$eq': int(dict['dealerId'])}},
            ).get_result()
    try: 
        # result_by_filter=my_database.get_query_result(selector,raw_result=True) 
        result= {
            'headers': {'Content-Type':'application/json'}, 
            'body': {'data':response} 
            }        
        return result
    except:  
        return { 
            'statusCode': 404, 
            'message': 'Something went wrong'
            }
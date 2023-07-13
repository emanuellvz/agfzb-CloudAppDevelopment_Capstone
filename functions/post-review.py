from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibmcloudant.cloudant_v1 import CloudantV1

def main(dict):
    authenticator = IAMAuthenticator('7TLFNDHyGDiH9kdJL5o9dcZXnOFLirzNDphc3QALa9YM')
    cloudant = CloudantV1(authenticator=authenticator)
    cloudant.set_service_url('https://f8685ea3-666e-43c4-9ef5-b7ef5d7189de-bluemix.cloudantnosqldb.appdomain.cloud')
    response = cloudant.post_document(db='reviews', document=dict["review"]).get_result()
    
    try:
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except ApiException as e:
        print(f"Error: {e.code} - {e.message}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': {'error': 'Internal Server Error'}
        }
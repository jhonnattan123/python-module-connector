import json
ERROR_DOUBLE_DATA = 'message and reply cannot be dict or list at the same time'

class Moduleconnector:

    def __init__(self, objectDefaultData={}):
        self.success = False
    
        self.message = "module_connector"
    
        self.code = 500
    
        self.response = []
    
        if isinstance(objectDefaultData, str):
            self.message = objectDefaultData;


    def for_list():
        self.response = []


    def for_dict():
        self.response = {}


    
    def writeMessageAndReponse(self, response=[], message=""):

        # INVERSE DATA CASE .ok('success_load', {data:1})
        if isinstance(response, str) and isinstance(message, (list, dict)): 
            self.response = message
            self.message = response
    

        # ONLY TEXT ONE CASE .ok('success_load')
        elif isinstance(response, str) and isinstance(message, str): 
            self.response = []
            self.message = response


        # NORMAL DATA CASE .ok({data:1}, 'success_load') or ONLY OBJECT CASE
        elif isinstance(response, (list, dict)) and isinstance(message, str): 
            self.response = response
            self.message = message


        # IF TWO OBJECT CASE ERROR
        elif isinstance(response, (list, dict)) and isinstance(message, (list, dict)): 
            self.response = []
            self.message = ERROR_DOUBLE_DATA
        
        return self
    
    
    def successFunctions(self, response, message, code):
        self.code = code
        self.success = True
        return self.writeMessageAndReponse(response, message)
    
    
    def failedFunctions(self, response, message, code):
        self.code = code;
        self.success = False;
        return self.writeMessageAndReponse(response, message)
    
    
    def getHTTPMessage(self):
    
        sw = {
            200: 'ok',
            201: 'created',
            202: 'accepted',
            203: 'nonAuthoritative',
            204: 'noContent',
            400: 'badRequest',
            401: 'unauthorized',
            403: 'forbidden',
            404: 'notFound',
            409: 'conflict',
        }
        return sw.get(self.code)
    
    
    def ok(self, response=[], message='ok'):
        return self.successFunctions(response, message, 200)
    
    
    def created(self, response=[], message='created'):
        return self.successFunctions(response, message, 201)
    
    
    def accepted(self, response=[], message='accepted'):
        return self.successFunctions(response, message, 202)
    
    
    def nonAuthoritative(self, response=[], message='nonAuthoritative'):
        return self.successFunctions(response, message, 203)
    
    
    def noContent(self, response=[], message='noContent'):
        return self.successFunctions(response, message, 204)
    
    
    def badRequest(self, response=[], message='badRequest'):
        return self.failedFunctions(response, message, 400)
    
    
    def unauthorized(self, response=[], message='unauthorized'):
        return self.failedFunctions(response, message, 401)
    
    
    def forbidden(self, response=[], message='forbidden'):
        return self.failedFunctions(response, message, 403)
    
    
    def notFound(self, response=[], message='notFound'):
        return self.failedFunctions(response, message, 404)
    
    
    def conflict(self, response=[], message='conflict'):
        return self.failedFunctions(response, message, 409)


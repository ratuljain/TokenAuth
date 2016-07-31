from rest_framework.response import Response
from django.http import JsonResponse
import jwt
class TokenAuthMiddleware:

    """
    Middleware to validate JWT Token in Auth Header
    
    """

    def process_request(self,request):
        token = None
        if 'HTTP_AUTHORIZATION' not in request.META:
            return
            #print "authenticating via authorization header!"
        token = request.META['HTTP_AUTHORIZATION']
        print token
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print payload['username'] + " Logged in"
            return
        except jwt.ExpiredSignatureError:
            print {'detail' : "The token expired. Need to generate again"}






# curl -X POST -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhdHVsIiwiZXhwIjoxNDcwMDAwMjU3fQ.wg4LqO8-K96bZU5Xz_VBhBaFBYO5fHJRv2hxEDn_GTI" http://localhost:8000/api/token/3

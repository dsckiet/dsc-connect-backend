from .serializers import UserSerializer


# We want token as response with Primary key so that more info can be fetched
def jwt_response_payload_handler(token, user=None, request=None):
    user = UserSerializer(user, context={'request': request}).data
    return {
        'data':{
        	'token': token,
        	'user_id': user['pk'],
        	'email':user['email'],
            'phone_nuber':user['phone_number'],
            'first_name':user['first_name'],
            'last_name':user['last_name'],
            'gender':user['gender'],
            'is_admin':user['is_admin'],
            'is_worker':user['is_worker'],
            'is_volunteer':user['is_volunteer'],
            'date_joined':user['date_joined'],
		},
        
        'msg':"Successfully Logged In",
        'error':False,


            }
    
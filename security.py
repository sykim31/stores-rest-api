from werkzeug.security import safe_str_cmp
from models.user import UserModel

#retrieve user name by our new find_by_username and find_by_id.
#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)#importing entity.
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    #return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)

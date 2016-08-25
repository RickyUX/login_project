from system.core.controller import *
import sys #sys.stderr.write('text_you_want_to_print\n')
class Logins(Controller):
    def __init__(self, action):
        super(Login, self).__init__(action)
        self.load_model('LoginModel')
        self.db = self._app.db

    def index(self):
        # courses = self.models['LoginModel'].get_all_courses()
        # sys.stderr.write('Test1\n')
        return self.load_view('index.html')

        # """
        # A loaded model is accessible through the models attribute 
        # self.models['WelcomeModel'].get_users()
        
        # self.models['WelcomeModel'].add_message()
        # # messages = self.models['WelcomeModel'].grab_messages()
        # # user = self.models['WelcomeModel'].get_user()
        # # to pass information on to a view it's the same as it was with Flask
        
        # # return self.load_view('index.html', messages=messages, user=user)
        # """



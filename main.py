import smtplib



class EmailServer:



    def __init__(self, email_server, from_email, password):

   

        self.email_server = email_server

        self.from_email = from_email

        self.password = password

       

    def send_email(self, to_email, subject, message):

       

        connection = smtplib.SMTP(self.email_server)



        connection.starttls()

        connection.login(user=self.from_email, password=self.password)



        email_message = f'Subject: {subject} \n\n {message}'

        connection.sendmail(from_addr=self.from_email, to_addrs=to_email, msg=email_message)



        connection.close()       

       

#An environmental variable module to get api key:

class EnvironmentVariables:

   

    def __init__(self, fname):

       

        self.fname = fname

        self.environment_variables = {}

       

        try:

           

            with open(self.fname, 'r') as f:

                variables = f.readlines()

               

                for variable in variables:

                   

                    data = variable.split('=')

                   

                    self.environment_variables[data[0].replace('\n', '')] =  data[1].replace('\n', '')

               

        except Exception as e:

           

            print(str(e))



    def get_environment_variable(self, v):

       

        try:

           

            return self.environment_variables[v]



        except:

           

            return None

           

    def get_all_environment_variables(self):

   

        return self.environment_variables



    def list_all_environment_variables(self):

   

        for key, value in self.environment_variables.items():

           

            print(f'{key}={value}')



#And this is the program which retrieve the ip and send out the email:

import requests, os

import emailserver    #import email module

import envvariable    #import module read password



from_email = '<sender_email>'

ev = envvariable.EnvironmentVariables('<path_to_file_with_environmental_varialbe>')

password = ev.get_environment_variable('<name_of_environmental_variable>')



if not (password == None):



    email_server = '<email_server>'

    subject = 'Public IP address'

    message = ''



    to_email = 'receipient_email'

   

    #create an instance of the email server

    emailServer = emailserver.EmailServer(email_server = email_server, from_email = from_email, password = password)



    #Get public ip - API endpoint

    data = requests.get('https://api.ipify.org?format=json')



    message = data.json()['ip']    #Email message



    #Send email messaage

    emailServer.send_email(to_email = to_email, subject = subject, message = message)

   

else:

   

    print('Email password cannot be found.')




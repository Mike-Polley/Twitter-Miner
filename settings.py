import pyodbc
# enter twitter dev details here (consumer key,
# consumer secret, access token and secret access token)

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Enter sql connection string here format = 'Driver=,Server=,Database=,Credentials='
conn = pyodbc.connect('')
c = conn.cursor()

# Enter the twitter tags to list as strings you would like to follow here eg '#Brexit'
tracked_tags = [
'',
]

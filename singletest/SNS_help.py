import oauth2 as oauth
import time

# Set the API endpoint 
url = "http://example.com/photos"

# Set the base oauth_* parameters along with any other parameters required
# for the API call.
params = {
    'oauth_version': "1.0",
    'oauth_nonce': oauth.generate_nonce(),
    'oauth_timestamp': int(time.time()),
    'user': 'joestump',
    'photoid': 555555555555
}

# Set up instances of our Token and Consumer. The Consumer.key and 
# Consumer.secret are given to you by the API provider. The Token.key and
# Token.secret is given to you after a three-legged authentication.
token = oauth.Token(key="tok-test-key", secret="tok-test-secret")
consumer = oauth.Consumer(key="con-test-key", secret="con-test-secret")

# Set our token/key parameters
params['oauth_token'] = token.key
params['oauth_consumer_key'] = consumer.key

# Create our request. Change method, etc. accordingly.
req = oauth.Request(method="GET", url=url, parameters=params)

# Sign the request.
signature_method = oauth.SignatureMethod_HMAC_SHA1()
req.sign_request(signature_method, consumer, token)


# Using the client
import oauth2 as oauth

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key="0611c062267f288d12354126737d79a7", 
    secret="0fb66e9dcfbf0abf")

# Request token URL for Twitter.
request_token_url = "http://www.douban.com/service/auth/request_token"

# Create our client.
client = oauth.Client(consumer)
print dir(client)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")
print resp
print content
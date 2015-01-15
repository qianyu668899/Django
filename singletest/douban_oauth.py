from douban_client import DoubanClient

KEY = '0611c062267f288d12354126737d79a7'
SECRET = '0fb66e9dcfbf0abf'
CALLBACK = ''
SCOPE = 'douban_basic_common,community_basic_user'

client = douban.service.DoubanService(server=SERVER, api_key=API_KEY,secret=SECRET)
client.ProgrammaticLogin(token_key=TOKEN_KEY,token_secret=TOKEN_SECRET)

client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)
client.auth_with_password('jinggeqianyu1991@163.com', 'qsjy81zwxy')

print client.user.me
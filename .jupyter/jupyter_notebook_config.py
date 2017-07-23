import os
print('Loading notebook config..')

c.NotebookApp.base_url = '/'

c.NotebookApp.certfile = os.path.expanduser('~/key/cert.pem')
c.NotebookApp.keyfile = os.path.expanduser('~/certs/key.key')
c.NotebookApp.password = u'sha1:0bfffb660e74:a03474572df5082aa99105ae9702d13c118f2c3d'
c.NotebookApp.password_required = True
c.NotebookApp.port = 8888

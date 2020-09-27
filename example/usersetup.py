import ptvsd
ptvsd.enable_attach(address=('127.0.0.1', 3000), redirect_output=True)
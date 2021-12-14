from OpenSSL import SSL


# context = (
#     '/tarkir-tools/certs/localhost.crt',
#     '/tarkir-tools/certs/localhost.key',
# )

context = SSL.Context(SSL.TLSv1_2_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

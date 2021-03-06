# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

import pem

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"

ca_private_key_filename = pem.parse_file(CA_PRIVATE_KEY_FILENAME)
ca_public_key_filename = pem.parse_file(CA_PUBLIC_KEY_FILENAME)
server_private_key_filename = pem.parse_file(SERVER_PRIVATE_KEY_FILENAME)
server_csr_key_filename = pem.parse_file(SERVER_CSR_FILENAME)
server_public_key_filename = pem.parse_file(SERVER_PUBLIC_KEY_FILENAME)

print(ca_private_key_filename)
print(ca_public_key_filename)
print(server_private_key_filename)
print(server_csr_key_filename)
print(server_public_key_filename)

#  A compléter

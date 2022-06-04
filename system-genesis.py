#!/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import authorization_client

genesisKeyID = 'CD9A3ED2-9190-4B27-86CC-9EC8F5341692'
genesisKeySecret = 'GENESIS-AC0F0164-E970-4BE5-8387-8761F23EB4FF'

def systemGenesis():
  configuration = authorization_client.Configuration('http://localhost:31202')
  apiClient = authorization_client.ApiClient(configuration)
  tokenAPI = authorization_client.TokenApi(apiClient)
  jwks = tokenAPI.get_jwks()
  print('Public Keys: ' + str(len(jwks.keys)))

  for key in jwks.keys:
      print(key.kid + ' ' + key.kty+ ' ' + key.alg)

if __name__ == '__main__':
  systemGenesis()
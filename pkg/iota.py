import os
import iota_client
from iota_client import IotaClient

class IOTA():
  def __init__(self):
    self.client = IotaClient({'nodes': [os.getenv("NODE_ENDPOINT")]})
  def get_node(self):
    return self.client


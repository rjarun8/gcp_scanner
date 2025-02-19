# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""The module with SpiderContext query model.

"""

import queue
from typing import List, Tuple

from httplib2 import Credentials


class SpiderContext:
  """A simple class to initialize the context with a list of root SAs
  """

  def __init__(self, sa_tuples: List[Tuple[str, Credentials, List[str]]]):
    """Initialize the context with a list of the root service accounts.

    Args:
      sa_tuples: [(sa_name, sa_object, chain_so_far)]
    """

    self.service_account_queue = queue.Queue()
    for sa_tuple in sa_tuples:
      self.service_account_queue.put(sa_tuple)

#---------------------------------------------------------------------------
# Copyright 2018 The Open Source Electronic Health Record Alliance
#
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
#---------------------------------------------------------------------------

import json
import glob

def run(fileNo, outName, filesDir):
  output = "%s/%s" % (filesDir, outName)
  menuJsonFiles = glob.glob("%s/menus/%s/VistAMenu-*.json" % (filesDir, fileNo))
  outjson = []

  for menuFile in menuJsonFiles:
    menuItem = {}
    with open(menuFile, 'r') as menuFp:
      menuJson = json.load(menuFp);
      menuItem['label'] = menuJson['option'] + ': ' + menuJson['name']
      menuItem['id'] = menuJson['ien']
      outjson.append(menuItem)

  with open(output, 'w') as outFp:
    json.dump(outjson, outFp)

  print("*** Updated %s" % output)

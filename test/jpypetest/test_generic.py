# *****************************************************************************
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   See NOTICE file for details.
#
# *****************************************************************************
import jpype
import common


class GenericTestCase(common.JPypeTestCase):
    """ Test for JClass with generic types
    """

    def setUp(self):
        common.JPypeTestCase.setUp(self)

    def testArray0(self):
        cls = jpype.JClass('java.util.ArrayList<>')

    def testArray1(self):
        cls = jpype.JClass('java.util.ArrayList<?>')

    def testArray2(self):
        with self.assertRaises(TypeError):
            cls = jpype.JClass('java.util.ArrayList<?,?>')

    def testMap0(self):
        cls = jpype.JClass('java.util.HashMap<>')

    def testMap1(self):
        with self.assertRaises(TypeError):
            cls = jpype.JClass('java.util.HashMap<?>')

    def testMap2(self):
        cls = jpype.JClass('java.util.HashMap<?,?>')

    def testObject0(self):
        with self.assertRaises(TypeError):
            cls = jpype.JClass('java.lang.Object<>')

    def testObject1(self):
        with self.assertRaises(TypeError):
            cls = jpype.JClass('java.lang.Object<?>')


import unittest
from jmatch import match

MOCK_JSON_LIST = '''
                    [
                        {
                            "track": {
                                "title": "Shame Shame Shame",
                                "duration": "3:10"
                            }
                        },
                        {
                            "track": {
                                "title": "Road Runner",
                                "duration": "2:50"
                            }
                        }
                    ]
                 '''

MOCK_JSON_DICT = '''
                    {
                        "entry-1" : {
                            "name":"first entry",
                            "other" : "some other data"
                        },
                        "entry-2" : {
                            "name":"second entry",
                            "other": " "
                        },
                        "entry-3" : {
                            "name":"third entry",
                            "other": "something else"
                        }
                    }
                 '''

MOCK_JSON_DICT_OF_LIST = '''
            {
                "glossary": {
                    "title": "example glossary",
                    "GlossDiv": {
                        "title": "S",
                        "GlossList": {
                            "GlossEntry": {
                                "ID": "SGML",
                                "SortAs": "SGML",
                                "GlossTerm": "Standard Generalized Markup Language",
                                "Acronym": "SGML",
                                "Abbrev": "ISO 8879:1986",
                                "GlossDef": {
                                    "para":
                                    "A meta-markup language, used to create markup languages such as DocBook.",
                                    "GlossSeeAlso": [{"value": "GML", "type": []}]
                                },
                                "GlossSee": "markup"
                            }
                        }
                    }
                }
            }
                        '''

MOCK_JSON_ONE_OBJECT = '''
                            {
                                "name":"Bond",
                                "city":"London",
                                "profession": "secret agent"
                            }
                       '''


class TestJsonMatch(unittest.TestCase):
    def test001_one_object_response(self):
        result = match(expected='{"name": "Bond"}',
                       actual=MOCK_JSON_ONE_OBJECT)
        self.assertTrue(result)

    def test002_one_object_response(self):
        result = match(expected='{"name": "James", "profession": '
                                '"secret agent"}',
                       actual=MOCK_JSON_ONE_OBJECT)
        self.assertFalse(result)

    def test003_list_of_objects_response(self):
        result = match(expected='{"track": {"title": "Shame Shame Shame",'
                                ' "duration":"3:10"}}',
                       actual=MOCK_JSON_LIST)
        self.assertTrue(result)

    def test004_list_of_objects_response(self):
        result = match(expected='{"track":{"title":"Eyesight To The Blind",'
                                ' "duration":"2:50"}}',
                       actual=MOCK_JSON_LIST)
        self.assertFalse(result)

    def test005_dict_of_objects_response(self):
        result = match(expected='{"entry-1" : {"name":"first entry"}}',
                       actual=MOCK_JSON_DICT)
        self.assertTrue(result)

    def test006_dict_of_objects_response(self):
        result = match(expected='{"entry-4" : {"name":"fourth entry"}}',
                       actual=MOCK_JSON_DICT)
        self.assertFalse(result)

    def test007_dict_of_list_of_objects_response(self):
        result = match(expected='{"glossary": {"GlossDiv": '
                                '{"GlossList": {"GlossEntry": {"GlossDef": '
                                '{"GlossSeeAlso": [{"value": "GML", "type": []}]}}}}}}',
                       actual=MOCK_JSON_DICT_OF_LIST)
        self.assertTrue(result)

    def test008_dict_of_list_of_objects_response(self):
        result = match(expected='{"glossary": {"GlossDiv": '
                                '{"GlossList": {"GlossEntry": {"GlossDef": '
                                '{"GlossSeeAlso": [{"value": "GML", "type": ["JSON"]}]}}}}}}',
                       actual=MOCK_JSON_DICT_OF_LIST)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

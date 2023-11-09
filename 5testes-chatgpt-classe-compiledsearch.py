import unittest
from bleachbit.DeepScan import CompiledSearch

class TestCompiledSearch(unittest.TestCase):          # 5 Testes da função match da classe CompiledSearch

    def test_match_with_regex(self):
        search_condition = SearchCondition(command='test', regex='file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'file123.txt')

        self.assertEqual(result, '/path/to/directory/file123.txt')

    def test_match_with_nregex(self):
        search_condition = SearchCondition(command='test', nregex='ignore\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'ignore456.txt')

        self.assertIsNone(result)

    def test_match_with_wholeregex(self):
        search_condition = SearchCondition(command='test', wholeregex='subdir/file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory/subdir', 'file789.txt')

        self.assertEqual(result, '/path/to/directory/subdir/file789.txt')

    def test_match_with_nwholeregex(self):
        search_condition = SearchCondition(command='test', nwholeregex='exclude/subdir/file\d+\.txt')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory/exclude/subdir', 'file987.txt')

        self.assertIsNone(result)

    def test_match_no_conditions(self):
        search_condition = SearchCondition(command='test')
        compiled_search = CompiledSearch(search_condition)

        result = compiled_search.match('/path/to/directory', 'any_file.txt')

        self.assertEqual(result, '/path/to/directory/any_file.txt')

if __name__ == '__main__':
    unittest.main()

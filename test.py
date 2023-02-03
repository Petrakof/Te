import unittest
import your_streamlit_app

class TestYourStreamlitApp(unittest.TestCase):
    def test_input_output(self):
        input_data = "test input"
        expected_output = "test output"
        result = your_streamlit_app.run_app(input_data)
        self.assertEqual(result, expected_output)

    def test_input_output_2(self):
        input_data = "test input 2"
        expected_output = "test output 2"
        result = your_streamlit_app.run_app(input_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

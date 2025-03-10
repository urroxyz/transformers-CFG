from tests.json_utils import is_json_parsable
from transformers_cfg.parser import parse_ebnf
from transformers_cfg.recognizer import StringRecognizer


def test_minimal_json_array():
    """
    Test that we can load a JSON array
    """
    jsons = [
        "[\\n]",
        "[\\n1]",
        "[\\n1,2]",
        "[\\n1,2,3]",
    ]
    with open("examples/grammars/json_arr.ebnf", "r") as file:
        input_text = file.read()
    parsed_grammar = parse_ebnf(input_text)
    start_rule_id = parsed_grammar.symbol_table["root"]
    recognizer = StringRecognizer(parsed_grammar.grammar_encoding, start_rule_id)

    for json in jsons:
        assert is_json_parsable(json) == recognizer._accept_prefix(
            json
        ), f"Failed on {json}"

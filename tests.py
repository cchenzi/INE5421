from model import DFA, NFA
from cfLang import ContextFreeGrammar


def test_minimization_alives():
    states = ["S", "A", "B"]
    alphabet = ["a", "b"]
    final_states = ["B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "S", "b": "A"},
        "B": {"a": "A", "b": "B"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_dead()
    if set(dfa.states) == {"B"}:
        print("Alive yay!!! 1")

    transitions = {
        "S": {"a": "B", "b": "S"},
        "A": {"a": "A", "b": "A"},
        "B": {"a": "A", "b": "B"},
    }
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_dead()
    if set(dfa.states) == {"S", "B"}:
        print("Alive yay!!! 2")


def test_minimization_reachables():
    states = ["S", "A", "B"]
    alphabet = ["a", "b"]
    final_states = ["A", "B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "S", "b": "A"},
        "B": {"a": "A", "b": "B"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_unreachable()
    print(dfa.states)
    if set(dfa.states) == {"S", "A"}:
        print("Reachable yay!!! 1")


def test_group_equivalent():
    states = ["S", "A", "B", "C"]
    alphabet = ["a", "b"]
    final_states = ["A", "B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "A", "b": "B"},
        "B": {"a": "A", "b": "B"},
        "C": {"a": "A", "b": "S"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.group_equivalent()
    print(dfa.states)
    if set(dfa.states) == {"S", "A"}:
        print("Group yay!!! 1")


def test_minimization():
    print("\nTest minimization:")
    def test1():
        print("\ntest1")
        states = ["A", "B", "C", "D", "E", "F", "G", "H"]
        alphabet = ["0", "1"]
        final_states = ["A", "D", "G"]
        transitions = {
            "A": {"0": "G", "1": "B"},
            "B": {"0": "F", "1": "E"},
            "C": {"0": "C", "1": "G"},
            "D": {"0": "A", "1": "H"},
            "E": {"0": "E", "1": "A"},
            "F": {"0": "B", "1": "C"},
            "G": {"0": "G", "1": "F"},
            "H": {"0": "H", "1": "D"},
        }

        init_state = "A"
        dfa = DFA(states, alphabet, init_state, final_states, transitions)
        dfa.minimize()
        print(dfa.states)

    def test2():
        print('\ntest2')
        states = ["q0", "q1", "q2", "q3", "q4"]
        alphabet = ["a", "b"]
        final_states = ["q1", "q2", "q3"]
        transitions = {
            "q0": {"a": "q4", "b": "q1"},
            "q1": {"a": "q2", "b": "q1"},
            "q2": {"a": "q3", "b": "q1"},
            "q3": {"a": "q3", "b": "q2"},
            "q4": {"a": "q3", "b": "q2"},
        }

        init_state = "q0"
        dfa = DFA(states, alphabet, init_state, final_states, transitions)
        dfa.minimize()
        print(dfa.states)

    # test1()
    test2()


def test_determinization():
    states = ["S", "A", "B", "C", "X"]
    alphabet = ["a", "b"]
    final_states = ["S", "X"]
    transitions = {
        "S": {"a": ["A"], "b": ["C", "X"]},
        "A": {"a": ["B"], "b": ["A"]},
        "B": {"a": ["C", "X"], "b": ["B"]},
        "C": {"a": ["A"], "b": ["C", "X"]},
        "X": {"a": [], "b": []},
    }
    init_state = "S"
    a1 = NFA(states, alphabet, init_state, final_states, transitions, False)
    a1.determinize()

    states = ["p", "q", "r"]
    alphabet = ["a", "b", "c"]
    init_state = "p"
    final_states = ["r"]
    transitions = {
        "p": {"a": ["p"], "b": ["q"], "c": ["r"], "&": []},
        "q": {"a": ["q"], "b": ["r"], "c": [], "&": ["p"]},
        "r": {"a": ["r"], "b": [], "c": ["p"], "&": ["q"]},
    }

    a2 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a2.determinize()

    transitions = {
        "p": {"a": [], "b": ["q"], "c": ["r"], "&": ["q"]},
        "q": {"a": ["p"], "b": ["r"], "c": ["p", "q"], "&": []},
        "r": {"a": [], "b": [], "c": [], "&": []},
    }
    a3 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a3.determinize()


def test_cfLang_first_follow():

    cfg = ContextFreeGrammar(
        ['X', 'S', 'C'], ['c', 'd'],
        {
            'X': ['S'],
            'S': ['CC'],
            'C': ['cC', 'd']
        },
        'X'
    )
    assert set(cfg.first['X']) == {'c', 'd'}
    assert set(cfg.first['S']) == {'c', 'd'}
    assert set(cfg.first['C']) == {'c', 'd'}

    assert set(cfg.follow['X']) == {'$'}
    assert set(cfg.follow['S']) == {'$'}
    assert set(cfg.follow['C']) == {'$', 'c', 'd'}

    cfg = ContextFreeGrammar(
        ['S', 'A', 'B', 'C'], ['a', 'b', 'c', 'd'],
        {
            'S': ['ABC'],
            'A': ['aA', '&'],
            'B': ['bB', 'ACd'],
            'C': ['cC', 'd']
        },
        'S'
    )
    assert set(cfg.first['S']) == {'a', 'b', 'c', 'd'}
    assert set(cfg.first['A']) == {'a', '&'}
    assert set(cfg.first['B']) == {'a', 'b', 'c', 'd'}
    assert set(cfg.first['C']) == {'c', 'd'}

    assert set(cfg.follow['S']) == {'$'}
    assert set(cfg.follow['A']) == {'a', 'b', 'c', 'd'}
    assert set(cfg.follow['B']) == {'c', 'd'}
    assert set(cfg.follow['C']) == {'$', 'd'}

    cfg = ContextFreeGrammar(
        ['P', 'K', 'V', 'F', 'C'], ['b', 'c', 'e', 'f', 'v', 'm', ';'],
        {
            'P': ['KVC'],
            'K': ['cK', '&'],
            'V': ['vV', 'F'],
            'F': ['fP;F', '&'],
            'C': ['bVCe', 'm;C', '&']
        },
        'P'
    )
    assert set(cfg.first['P']) == {'c', 'v', 'f', 'b', 'm', '&'}
    assert set(cfg.first['K']) == {'c', '&'}
    assert set(cfg.first['V']) == {'v', 'f', '&'}
    assert set(cfg.first['F']) == {'f', '&'}
    assert set(cfg.first['C']) == {'b', 'm', '&'}

    assert set(cfg.follow['P']) == {'$', ';'}
    assert set(cfg.follow['K']) == {'v', 'f', 'b', 'm', '$', ';'}
    assert set(cfg.follow['V']) == {'b', 'm', '$', ';', 'e'}
    assert set(cfg.follow['F']) == {'b', 'm', '$', ';', 'e'}
    assert set(cfg.follow['C']) == {'e', '$', ';'}


if __name__ == "__main__":
    # test_minimization_alives()
    # print('----------------------')
    # test_minimization_reachables()
    # print('----------------------')
    # test_group_equivalent()
    # test_minimization()
    test_cfLang_first_follow()

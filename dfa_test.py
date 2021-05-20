
from pythomata import SimpleDFA
alphabet = {"日", "本", "人"}
states = {"s1", "s2", "s3"}
initial_state = "s1"
accepting_states = {"s3"}
transition_function = {
    "s1": {
        "日":"s1",
        "本" : "s2"
    },
    "s2": {
        "人" : "s3",
        "本" : "s2"
    },
    "s3":{
        "人" : "s3"
    }
}
dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

word = "日本女人"
print(dfa.accepts(word))

state_event_dict = {
    "匹": {
        "配": {
            "算": {
                "法": {
                    "is_end": True
                },
                "is_end": False
            },
            "关": {
                "键": {
                    "词": {
                        "is_end": True
                    },
                    "is_end": False
                },
                "is_end": False
            },
            "is_end": False
        },
        "is_end": False
    },
    "信": {
        "息": {
            "抽": {
                "取": {
                    "is_end": True
                },
                "is_end": False
            },
            "is_end": False
        },
        "is_end": False
    }
}
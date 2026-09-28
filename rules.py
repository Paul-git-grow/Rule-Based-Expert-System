# Knowledge Base - IF THEN Rules

rules = [
    ({"fever", "cough"}, "viral_infection"),

    ({"viral_infection", "headache"}, "possible_flu"),

    ({"cough", "sore_throat"}, "throat_infection"),

    ({"fever", "body_pain"}, "flu_symptoms"),

    ({"possible_flu", "flu_symptoms"}, "flu")
]
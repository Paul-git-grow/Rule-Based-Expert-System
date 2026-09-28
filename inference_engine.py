def forward_chaining(facts, rules):

    known_facts = set()

    for fact, value in facts.items():
        if value:
            known_facts.add(fact)

    reasoning_log = []

    new_fact_found = True

    while new_fact_found:
        new_fact_found = False

        for conditions, conclusion in rules:

            if conditions.issubset(known_facts) and conclusion not in known_facts:

                known_facts.add(conclusion)

                reasoning_log.append(
                    f"IF {' AND '.join(conditions)} THEN {conclusion}"
                )

                new_fact_found = True

    return known_facts, reasoning_log
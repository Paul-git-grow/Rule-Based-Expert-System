from rules import rules
from inference_engine import forward_chaining

print("=" * 45)
print("       RULE-BASED EXPERT SYSTEM")
print("=" * 45)

print("\nPlease answer the following questions")
print("Enter yes or no\n")


# -------------------------
# INPUT VALIDATION
# -------------------------

def get_yes_no_input(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ["yes", "no"]:
            return answer

        print("Invalid input! Please enter only 'yes' or 'no'.")


# -------------------------
# USER INPUT
# -------------------------

fever = get_yes_no_input("Do you have fever?")
cough = get_yes_no_input("Do you have cough?")
headache = get_yes_no_input("Do you have headache?")
body_pain = get_yes_no_input("Do you have body pain?")
sore_throat = get_yes_no_input("Do you have sore throat?")


# -------------------------
# FACTS BASE
# -------------------------

facts = {
    "fever": fever == "yes",
    "cough": cough == "yes",
    "headache": headache == "yes",
    "body_pain": body_pain == "yes",
    "sore_throat": sore_throat == "yes"
}

print("\n--- FACTS BASE ---")

for fact, value in facts.items():
    print(f"{fact}: {value}")


# -------------------------
# FORWARD CHAINING
# -------------------------

print("\n--- FORWARD CHAINING ---")

known_facts, reasoning_log = forward_chaining(facts, rules)


# -------------------------
# ALL KNOWN FACTS
# -------------------------

print("\n--- ALL KNOWN FACTS ---")

for fact in sorted(known_facts):
    print("+", fact)


# -------------------------
# REASONING / INFERENCE LOG
# -------------------------

print("\n" + "=" * 45)
print("          INFERENCE LOG")
print("=" * 45)

if reasoning_log:
    for step, log in enumerate(reasoning_log, start=1):
        print(f"Step {step}: {log}")
else:
    print("No rules were triggered.")


# -------------------------
# FINAL CONCLUSION
# -------------------------

print("\n" + "=" * 45)
print("          FINAL CONCLUSION")
print("=" * 45)

if "flu" in known_facts:
    print("Result: Possible Flu")

elif "possible_flu" in known_facts:
    print("Result: Symptoms indicate Possible Flu")

elif "throat_infection" in known_facts:
    print("Result: Possible Throat Infection")

elif "viral_infection" in known_facts:
    print("Result: Possible Viral Infection")

elif "flu_symptoms" in known_facts:
    print("Result: Flu-like Symptoms Detected")

else:
    print("Result: No specific condition could be inferred.")

print("\nNote: This system is for educational purposes only.")
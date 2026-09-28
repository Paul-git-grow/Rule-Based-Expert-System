# Rule-Based Expert System using Python

## Project Overview

This project is a simple Rule-Based Expert System developed using Python.

The system accepts facts from the user and applies IF-THEN rules using a Forward Chaining inference mechanism.

It demonstrates basic Artificial Intelligence concepts such as a knowledge base, facts, rule-based reasoning, multi-step inference, and inference logging.

## Objective

The objective of this project is to build a small rule engine that:

- Accepts facts from the user
- Stores the facts in a facts base
- Uses IF-THEN rules
- Performs Forward Chaining
- Supports multi-step inference
- Displays the reasoning path
- Produces a final conclusion

## Technologies Used

- Python
- Rule-Based Artificial Intelligence
- Forward Chaining

## Project Structure

```text
Rule-Based-Expert-System/
│
├── main.py
├── rules.py
├── inference_engine.py
└── README.md
```

## File Description

### main.py

Handles:

- User input
- Input validation
- Facts base
- Displaying known facts
- Inference log
- Final conclusion

### rules.py

Contains the knowledge base of IF-THEN rules used by the expert system.

Example:

```text
IF fever AND cough
THEN viral_infection
```

### inference_engine.py

Contains the Forward Chaining algorithm.

The inference engine continuously checks the rules and adds new facts when rule conditions are satisfied.

## How the System Works

Example user facts:

```text
Fever = Yes
Cough = Yes
Headache = Yes
Body Pain = Yes
```

The system can perform multi-step reasoning:

```text
Fever + Cough
       |
       v
Viral Infection
       |
       v
Viral Infection + Headache
       |
       v
Possible Flu
```

Another rule can infer:

```text
Fever + Body Pain
       |
       v
Flu Symptoms
```

Finally:

```text
Possible Flu + Flu Symptoms
       |
       v
Flu
```

## Forward Chaining

Forward Chaining is a data-driven inference technique.

The system starts with the facts provided by the user and repeatedly applies rules whose conditions are satisfied.

New conclusions become new facts and can trigger additional rules.

## Example Inference Log

```text
Step 1: IF fever AND cough THEN viral_infection
Step 2: IF viral_infection AND headache THEN possible_flu
Step 3: IF fever AND body_pain THEN flu_symptoms
Step 4: IF possible_flu AND flu_symptoms THEN flu
```

## Example Result

```text
=============================================
              FINAL CONCLUSION
=============================================

Result: Possible Flu
```

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

5. Answer the questions using `yes` or `no`.

## Features

- Facts Base
- IF-THEN Rule Engine
- User Fact Input
- Input Validation
- Forward Chaining
- Multi-Step Inference
- Reasoning / Inference Log
- Final Conclusion

## Disclaimer

This project is created for educational purposes to demonstrate a Rule-Based Expert System and Forward Chaining in Artificial Intelligence.

It is not intended to provide real medical diagnosis or medical advice.
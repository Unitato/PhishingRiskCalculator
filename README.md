# Phishing Exercise Risk Score Calculator

This Python script is designed to compute a risk score for users based on their performance in phishing exercise tests. The risk score takes into account both the outcome of the exercise (passed/failed) and the severity of the phishing attempt.

## Features

- Calculates risk score based on passed and failed phishing exercises.
- Considers the severity of each phishing exercise in the calculation.
- Provides a normalized risk score between 0 to 100 for easier interpretation.

## Dependencies

- Python 3.x

## How to Use

1. **Setup**:
   - Ensure you have Python installed on your machine.

2. **Inputs**:
   - `passed_counts`: A list containing counts of passed exercises per severity level.
   - `failed_counts`: A list containing counts of failed exercises per severity level.
   - `severity_passed`: A list containing severity scores corresponding to the `passed_counts`.
   - `severity_failed`: A list containing severity scores corresponding to the `failed_counts`.
   - `Wp`: Base weight for passing an exercise. (e.g., 1)
   - `Wf`: Base weight for failing an exercise. This should typically be negative. (e.g., -2)

3. **Running the Script**:
   - Run the script using the command: `python risk_score_calculator.py`.
   - The script will then output the risk score and a normalized risk score.

4. **Example**:

   ```python
   passed_counts = [2, 3]
   failed_counts = [1, 0]
   severity_passed = [5, 7]
   severity_failed = [8, 9]
   Wp = 1
   Wf = -2

   risk_score, normalized_risk_score = compute_risk_score(passed_counts, failed_counts, severity_passed, severity_failed, Wp, Wf)
   print(f"Risk Score: {risk_score}")
   print(f"Normalized Risk Score: {normalized_risk_score:.2f}%")
   ```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or additional features you'd like to see. Feedback is always welcome!

## License

This script is provided under the MIT License. Refer to the `LICENSE` file for more details.

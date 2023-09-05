def phish_risk_score(passed_exercises, failed_exercises, severity_passed, severity_failed, Wp, Wf):
    """
    Compute the risk score based on passed and failed phishing exercises and their severities.
    
    Parameters:
    - passed_exercises: List of counts of passed exercises per severity level
    - failed_exercises: List of counts of failed exercises per severity level
    - severity_passed: List of severity scores for passed exercises
    - severity_failed: List of severity scores for failed exercises
    - Wp: Base weight for passing an exercise
    - Wf: Base weight for failing an exercise

    Returns:
    - risk_score: Computed risk score
    - normalized_risk_score: Normalized risk score (0 to 100)
    """

    # Calculate the weighted scores for passed and failed exercises
    passed_score = sum([p * Wp * s for p, s in zip(passed_exercises, severity_passed)])
    failed_score = sum([f * Wf * s for f, s in zip(failed_exercises, severity_failed)])

    risk_score = passed_score + failed_score

    # Calculate possible maximum and minimum scores for normalization
    max_possible_score = sum([t * Wp * s for t, s in zip(passed_exercises, severity_passed)]) + \
                         sum([t * Wf * s for t, s in zip(failed_exercises, severity_failed)])
    
    min_possible_score = max_possible_score * -1

    # Normalize the risk score to a range of 0 to 100
    normalized_risk_score = ((risk_score - min_possible_score) / (max_possible_score - min_possible_score)) * 100

    return risk_score, normalized_risk_score


# Example usage:
passed_counts = [2, 3]
failed_counts = [1, 0]
severity_passed = [5, 7]
severity_failed = [8, 9]
Wp = 1  # Base weight for passing an exercise
Wf = -2  # Base weight for failing an exercise

risk_score, normalized_risk_score = compute_risk_score(passed_counts, failed_counts, severity_passed, severity_failed, Wp, Wf)
print(f"Risk Score: {risk_score}")
print(f"Normalized Risk Score: {normalized_risk_score:.2f}%")

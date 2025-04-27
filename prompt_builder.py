def build_prompt(role, question_type, question, tone, experience_level):
    """
    Builds a prompt dynamically based on the role, question type, question itself, tone, and experience level.

    Args:
    - role (str): The job role the user is asking about.
    - question_type (str): The type of question (e.g., behavioral or technical).
    - question (str): The actual interview question input by the user.
    - tone (str): The tone of the answer (Formal, Casual, Neutral).
    - experience_level (str): The experience level (Junior, Mid, Senior).

    Returns:
    - str: The final prompt that will be sent to the model.
    """

    # Customize the prompt based on experience level and tone
    tone_map = {
        "Formal": "Please respond in a formal tone, with professional language.",
        "Casual": "Please respond in a casual, friendly tone.",
        "Neutral": "Please respond in a neutral tone."
    }

    experience_map = {
        "Junior": "Provide an answer suitable for someone with limited experience.",
        "Mid": "Provide an answer suitable for someone with a moderate level of experience.",
        "Senior": "Provide a detailed, expert-level response."
    }

    # Build the basic prompt
    if question_type == "Behavioral":
        prompt = f"As a {role}, answer the following behavioral interview question: {question}. {experience_map[experience_level]} {tone_map[tone]}"
    elif question_type == "Technical":
        prompt = f"As a {role}, answer the following technical interview question: {question}. {experience_map[experience_level]} {tone_map[tone]}"
    else:
        prompt = f"As a {role}, answer this interview question: {question}. {experience_map[experience_level]} {tone_map[tone]}"

    return prompt
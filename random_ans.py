import random


def random_answers():
    random_list = [
        "Please type something that makes sense.",
        "Can you ask something else?",
        "I cannot understand what you said.",
        "Sorry, I have problem understanding what youa re trying to say.",
        "Can you rephrase what you just said?",
        "I cannot answer that question."
    ]

    random_num = random.randint(0, len(random_list) - 1)
    random_answer = random_list[random_num]
    return random_answer



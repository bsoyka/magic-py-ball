import random

def answer(question, printable=False, seeded=True):
    """Returns a magic 8 ball answer to a user's question.

    Arguments
    ---------
    question: str
        The question made by the user. Used as seed for random
    printable: bool
        Outputs answer when True, returns it otherwise (default: False)
    """
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    if seeded:
        random.seed(question)

    answer = random.choice(answers)

    if printable:
        print(answer)
    
    return answer

if __name__ == "__main__":
    answer(input("QUESTION: "), printable=True)

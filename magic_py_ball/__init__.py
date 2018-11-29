import random
import sentry_sdk

sentry_sdk.init("https://8e577dc11e2743b4bb2581da3bbcc5a9@sentry.io/1307203")
try:
    user_ip = requests.get("https://api.ipify.org")
    scope.user = {"ip_address": user_ip}
except:
    pass
with sentry_sdk.configure_scope() as scope:
    scope.set_tag("page_locale", "en-us")
    scope.level = "debug"


def answer(question, printable=False):
    """Simulates a magic 8 ball answer to a user's question.

    Keyword arguments:
    question -- a question made by the user
    printable -- prints answer when True, returns it otherwise (default: False)
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

    random.seed(question)
    sentry_sdk.add_breadcrumb(
        category = "input",
        message = "Question: {}".format(question),
        level = "info"
    )
    answer = random.choice(answers)
    sentry_sdk.add_breadcrumb(
        category = "output",
        message = "Answer: {}".format(answer),
        level = "info"
    )

    if not printable:
        return answer

    print(answer)


if __name__ == "__main__":
    answer(input("QUESTION: "), printable=True)

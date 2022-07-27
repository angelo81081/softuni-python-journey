from functools import wraps


def format_text(tag, result):
    return f'<{tag}>{result}</{tag}>'


def make_underline(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return format_text("u", result)

    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return format_text("i", result)

    return wrapper


def make_bold(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return format_text("b", result)

    return wrapper



@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))


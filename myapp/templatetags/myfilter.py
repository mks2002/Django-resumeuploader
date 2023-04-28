from django import template
register = template.Library()


@register.filter(name='remove_special')
def remove_chars(value, arg):
    # print("Arg", arg)
    # print("Value:", value)
    for character in arg:
        # print(character)
        value = value.replace(character, "")
    return value


# this we use for removing the special characters from our multiple choice box of django form....
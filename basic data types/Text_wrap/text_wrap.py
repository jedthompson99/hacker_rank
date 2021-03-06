import textwrap


def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])


string, max_width = input(), int(input())
result = textwrap.fill(string, max_width)
print(result)


# for i in result:
#     print(i)

# def wrap(string, max_width):
#     for i in range(len(string)):
#         section = string[i:max_width]
#         result = "/n".join(range(0, string, max_width)
#         return result

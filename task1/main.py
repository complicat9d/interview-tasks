def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for i, arg in enumerate(args):
            param_name = list(annotations.keys())[i]
            expected_type = annotations[param_name]
            if not type(arg) is expected_type:
                raise TypeError(
                    f"Argument '{param_name}' should be of type {expected_type}, but got {type(arg)}"
                )

        for param_name, arg in kwargs.items():
            expected_type = annotations.get(param_name)
            if not type(arg) is expected_type:
                raise TypeError(
                    f"Argument '{param_name}' should be of type {expected_type}, but got {type(arg)}"
                )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError

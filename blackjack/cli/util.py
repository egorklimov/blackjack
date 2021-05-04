from typing import Dict


class ApplicationInterruptedException(BaseException):
    pass


def validate_input(msg, allowed_cmd: Dict[str, str]) -> str:
    rsp = input(msg)
    while rsp not in allowed_cmd.keys():
        if rsp == "help":
            print("Available commands:")
            print("\n".join([f'\t{k}: {v}' for (k, v) in allowed_cmd.items()]))
            rsp = input(msg)
        elif rsp == "exit":
            raise ApplicationInterruptedException
        else:
            print("Wrong command, use \"help\" to list available commands")
            rsp = input(msg)
    return rsp

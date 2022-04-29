"""
initialize of code
get input value from user
"""

from loguru import logger

from src.speed_check import speed_check


def main() -> None:
    """
    getting inputs from user
    """
    logger.info('main function is runn\n')
    option = int(
        input(
            "\tWhat speed do you want to test:\n\t\
                   1) Download Speed\n\t\
                   2) Upload Speed\n\t\
                   3) Ping\n\n\t\
                   Your chioce: "
        )
    )
    servernames = []
    speed_check(option, servernames)


if __name__ == "__main__":
    main()
    logger.info("Runtime has succesfully exprience . . . ")

"""
python program to test internet speed
"""
import speedtest


def speed_check(option: int, servernames: list) -> None:
    """
    handle inputs
    """
    st = speedtest.Speddtest()
    if option == 1:
        print(st.download())
    elif option == 2:
        print(st.upload())
    elif option == 3:
        st.get_servers(servernames)
        print(st.results.ping)
    else:
        print(f"{option} is not a valid choice . . . ")
        from src.main import main
        main()


if __name__ == "__main__":
    speed_check(1, ['4.2.2.4'])

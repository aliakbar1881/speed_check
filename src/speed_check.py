"""
python program to test internet speed
"""
import speedtest


def speed_check(option: int, servernames: list) -> None:
    """
    handle inputs
    """
    st = speedtest.Speedtest()
    if option == 1:
        print(f"Download Speed is :  {st.download()}")
    elif option == 2:
        print(f"Upload Speed is :  {st.upload()}")
    elif option == 3:
        st.get_servers(servernames)
        print("Ping Speed is :  {st.results.ping}")
    else:
        print(f"{option} is not a valid choice . . . ")
        from src.main import main
        main()


if __name__ == "__main__":
    speed_check(3, [])

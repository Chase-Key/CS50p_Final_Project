from project import welcome, main_menu, extras_menu, banner, checkout
import pytest
import mock

def main():
    test_banner()

def test_banner():
    assert banner("hello") ==     print("\n|----------------------------------------|")
    print("|         *Azure's Coffee Company*       |")
    print("|                *hello*              ")
    print("|----------------------------------------|")
    assert banner("goodbye") ==     print("\n|----------------------------------------|")
    print("|         *Azure's Coffee Company*       |")
    print("|                *goodbye*              ")
    print("|----------------------------------------|")

def test_checkout():
    with pytest.raises(SystemExit):
        checkout()

if __name__ == '__main__':
    main()



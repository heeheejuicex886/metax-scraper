import sys
from input import user_input


def test_uname_argument(monkeypatch):
    test_args = ["main.py", "testuser"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = user_input.parse_args()
    assert args.uname == "testuser"


def test_headless_flag(monkeypatch):
    test_args = ["main.py", "testuser", "--headless"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = user_input.parse_args()
    assert args.headless is True


def test_man_login_flag(monkeypatch):
    test_args = ["main.py", "testuser", "--man-login"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = user_input.parse_args()
    assert args.man_login is True


def test_ualias(monkeypatch):
    test_args = ["main.py", "testuser", "--ualias", "anon1"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = user_input.parse_args()
    assert args.ualias == "anon1"


def test_scrolls_value(monkeypatch):
    test_args = ["main.py", "testuser", "--scrolls", "12"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = user_input.parse_args()
    assert args.scrolls == 12

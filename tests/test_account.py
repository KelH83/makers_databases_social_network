from lib.account import Account

def test_account_constructs():
    account = Account("simples@ctm.com", "Sergei Meerkat")
    assert account.email == "simples@ctm.com"
    assert account.user_name == "Sergei Meerkat"

def test_accounts_format_nicely():
    account = Account("simples@ctm.com", "Sergei Meerkat")
    assert str(account) == "User Name:Sergei Meerkat,Email:simples@ctm.com"
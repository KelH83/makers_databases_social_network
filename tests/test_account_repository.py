from lib.account_repository import AccountRepository
from lib.account import Account


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/social_network.sql") 
    repository = AccountRepository(db_connection)

    accounts = repository.all() 

    assert accounts == [
        Account('Kelly@madeupemail.com', 'Kelly H'),
        Account('Kimi@adogue.com','Kimiko Dogue'),
        Account('KittyKatty@whiskas.com','Twyla Kitty'),
        Account('slytherinhouse@hp.com','Yuki Snake'),
    ]

def test_get_single_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    account = repository.find("Kimi@adogue.com")
    assert account == Account("Kimi@adogue.com","Kimiko Dogue")

def test_create_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    repository.create(Account("MiniMoo@Whiskas.com", "Mini Panther"))

    result = repository.all()
    assert result == [
        Account('Kelly@madeupemail.com', 'Kelly H'),
        Account('Kimi@adogue.com','Kimiko Dogue'),
        Account('KittyKatty@whiskas.com','Twyla Kitty'),
        Account('slytherinhouse@hp.com','Yuki Snake'),
        Account("MiniMoo@Whiskas.com", "Mini Panther"),
    ]

def test_update_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.update("snakeQueen@slytherin.com", 4) 

    account = repository.find("snakeQueen@slytherin.com")
    assert account == Account("snakeQueen@slytherin.com", "Yuki Snake")


def test_delete_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        Account('Kimi@adogue.com','Kimiko Dogue'),
        Account('KittyKatty@whiskas.com','Twyla Kitty'),
        Account('slytherinhouse@hp.com','Yuki Snake'),
    ]
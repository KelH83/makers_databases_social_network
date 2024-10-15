from lib.post_repository import PostRepository
from lib.post import Post


def test_get_all_posts(db_connection): 
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all() 

    assert posts == [
        Post('Day 1', 'Learned Python fundamentals', 1, 1),
        Post('Day 2','Went on an awesome walk', 3, 2),
        Post('Day 3','tuna is the best flavour ever!', 0, 3),
        Post('Day 4',"I am very hungry, might eat a mouse later", 2, 4),
    ]

def test_get_single_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    account = repository.find("Day 2")
    assert account == Post('Day 2','Went on an awesome walk', 3, 2)

def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post("Day 5", "Went to the park and played ball", 2, 2))

    result = repository.all()
    assert result == [
        Post('Day 1', 'Learned Python fundamentals', 1, 1),
        Post('Day 2','Went on an awesome walk', 3, 2),
        Post('Day 3','tuna is the best flavour ever!', 0, 3),
        Post('Day 4',"I am very hungry, might eat a mouse later", 2, 4),
        Post('Day 5',"Went to the park and played ball", 2, 2),
    ]

def test_update_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.update("Day 3", 1) 

    post = repository.find("Day 3")
    assert post == Post("Day 3", "tuna is the best flavour ever!", 1, 3)


def test_delete_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete("Day 4")

    result = repository.all()
    assert result == [
        Post('Day 1', 'Learned Python fundamentals', 1, 1),
        Post('Day 2','Went on an awesome walk', 3, 2),
        Post('Day 3','tuna is the best flavour ever!', 0, 3),
    ]
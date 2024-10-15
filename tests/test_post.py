from lib.post import Post

def test_post_constructs():
    post = Post("My first post", "Not really sure what to say",0, 1)
    assert post.title == "My first post"
    assert post.content == "Not really sure what to say"
    assert post.views == 0
    assert post.account_id == 1

def test_posts_format_nicely():
    post = Post("My first post", "Not really sure what to say",0, 1)
    assert str(post) == "Title:My first post,Content:Not really sure what to say, Views:0,Account ID:1"
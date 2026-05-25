import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# helper function to read from json
def load_posts():
    with open('posts.json', 'r') as f:
        return json.load(f)


# helper function to write to json
def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=4)


@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_posts()

        # get data from form fields
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # create a simple unique id
        new_id = 1
        if len(posts) > 0:
            new_id = max(p['id'] for p in posts) + 1

        # create new post object
        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        # add to list and save back to file
        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_posts()

    # create a new list without the post that matches the id
    new_posts = [p for p in posts if p['id'] != post_id]

    # save the updated list back to the file
    save_posts(new_posts)

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):  # Ich habe den Namen hier auf 'update_post' geändert
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)

@app.route('/like/<int:post_id>')
def like_post(post_id):
    posts = load_posts()

    # Find the post and increment likes
    for post in posts:
        if post['id'] == post_id:
            # Check if 'likes' key exists, if not initialize it
            post['likes'] = post.get('likes', 0) + 1
            break

    save_posts(posts)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

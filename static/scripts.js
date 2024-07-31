document.addEventListener('DOMContentLoaded', function() {
    loadPosts();

    document.getElementById('postForm').addEventListener('submit', function(event) {
        event.preventDefault();
        createPost();
    });
});

function loadPosts() {
    fetch('http://127.0.0.1:8000/api/posts/')
        .then(response => response.json())
        .then(data => {
            const postsDiv = document.getElementById('posts');
            postsDiv.innerHTML = '';
            data.forEach(post => {
                const postElement = document.createElement('div');
                postElement.classList.add('post');
                postElement.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p>`;
                postsDiv.appendChild(postElement);
            });
        });
}

function createPost() {
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    fetch('http://127.0.0.1:8000/api/posts/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: title, content: content }),
    })
    .then(response => response.json())
    .then(data => {
        loadPosts();
        document.getElementById('postForm').reset();
    });
}

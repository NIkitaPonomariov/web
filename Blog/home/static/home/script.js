console.log("Home page loaded!");
document.querySelectorAll('.post').forEach(post => {
    post.addEventListener('click', () => {
        alert('You clicked a post!');
    });
});

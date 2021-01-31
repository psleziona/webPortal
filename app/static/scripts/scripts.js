const req = new XMLHttpRequest()

document.addEventListener('DOMContentLoaded', function () {

    var add_post = document.querySelector('.add_post__form');
    var add_post_btn = document.querySelector('#add_post_btn');


    if (add_post_btn) {
        add_post_btn.addEventListener('click', function () {
            add_post.style.display = "block";
            add_post_btn.style.display = "none";
        });
    };


    var comments_btn = document.querySelectorAll('.show_comments');


    for (i = 0; i < comments_btn.length; i++) {
        comments_btn[i].addEventListener('click', function () {
            this.nextElementSibling.style.display = 'block';
            this.style.display = 'none';
        });
    };


    deleteButtons = document.querySelectorAll('.del_btn');

    var del_post = function (id) {
        var post_id = id.slice(7)
        var url = '/post_delete/' + post_id
        console.log(url)
        req.open('POST', '/post_delete/' + post_id)
        req.send()
        req.addEventListener('load', function(e){
            location.reload()

        });
    };

    for (i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', function () {
            del_post(this.id)
        });
    };

});


// Kanban


const tasks = document.querySelectorAll('.drag_task')

const tables = document.querySelectorAll('.kanban_table')


tasks.forEach(task => {

    task.addEventListener('dragstart', e => {
        task.classList.add('moving')
    });

    task.addEventListener('dragend', e => {
        task.classList.remove('moving')
    });

});

tables.forEach(table => {

    table.addEventListener('dragover', e => {
        e.preventDefault()
    });

    table.addEventListener('drop', e=> {
        const task = document.querySelector('.moving')
        table.appendChild(task)
        const task_id = task.id
        const table_name = table.firstElementChild.textContent.toLowerCase()
        updateDB(task_id, table_name)
    });
});

const updateDB = (task_id, category_name) => {
    const form = new FormData()
    req.open('POST', '/todo/change')
    form.append('task_id', task_id)
    form.append('category', category_name)
    req.send(form)
    }

task_del_btns = document.querySelectorAll('.task_delete')

task_del_btns.forEach(del_btn => {

    del_btn.addEventListener('click', function() {
        task_id = this.parentElement.id
        req.open('POST', '/todo/delete_task/' + task_id)
        req.send(null)
        req.addEventListener('load', () => {
            location.reload()
        
        });
    });
});


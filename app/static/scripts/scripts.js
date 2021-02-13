const req = new XMLHttpRequest()

const category_tabs = () => {
    const url = new URL(window.location.href);

    let category = url.searchParams.get('category');
    let project = url.searchParams.get('project');

    if (category) {
        category = category.toLowerCase();
    }
    if (project) {
        project = project.toLowerCase();
    }

    let tabs = document.querySelector('.nav-tabs').children;


    Array.prototype.forEach.call(tabs, element => {
        let source = element.childNodes[1].innerText.toLowerCase();
        if ((source == category) || (source == project)) {
            element.classList.add('active')
        }
    })


}



document.addEventListener('DOMContentLoaded', function () {
    category_tabs()

    const add_post = document.querySelector('.add_post__form');
    const add_post_btn = document.querySelector('.add_post__btn');
    const posts = document.querySelector('.posts');


    if (add_post_btn) {
        add_post_btn.addEventListener('click', function (e) {
            e.preventDefault()
            add_post.classList.toggle('add_post__form--hide');
            posts.classList.toggle('posts--add');
        });
    };


    let comments_btn = document.querySelectorAll('.comments__show');


    for (i = 0; i < comments_btn.length; i++) {
        comments_btn[i].addEventListener('click', function () {
            this.nextElementSibling.style.display = 'block';
            this.style.display = 'none';
        });
    };


    const deleteButtons = document.querySelectorAll('.post__del_btn');

    var del_post = function (id) {
        let post_id = id.slice(7)
        req.open('POST', '/post_delete/' + post_id)
        req.send()
        req.addEventListener('load', () => {
            location.reload()

        });
    };

    for (i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', function () {
            del_post(this.id)
        });
    };

    const dynamic_change_post_category = () => {
        const select_post_cat = document.querySelector('#select_post_category');
        const url = new URL(window.location.href);
        const category = url.searchParams.get('category');
        let index = null;
        for (let i = 0; i < select_post_cat.options.length; i++) {
            if (select_post_cat.options[i].innerText.toLowerCase() == category) {
                index = i;
            };
        };
        select_post_cat.selectedIndex = index;
    };
    dynamic_change_post_category()


    const add_task_btn = document.querySelector('.add_task__btn')
    const add_task__form = document.querySelector('.add_task__form')

    add_task_btn.addEventListener('click', e => {
        e.preventDefault()
        add_task__form.classList.toggle('add_task__form--hide')
    });


});


// Kanban


const tasks = document.querySelectorAll('.task')

const tables = document.querySelectorAll('.kanban__table')


tasks.forEach(task => {

    if (task.parentElement.children[0].innerText == 'Finished') {
        task.draggable = false;
    };

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

    table.addEventListener('drop', e => {
        const task = document.querySelector('.moving')
        table.appendChild(task)
        const task_id = task.id
        const table_name = table.firstElementChild.textContent.toLowerCase()
        updateDB(task_id, table_name)
    });
});

const updateDB = (task_id, category_name) => {
    const form = new FormData()
    req.open('POST', '/kanban/change')
    form.append('task_id', task_id)
    form.append('category', category_name)
    req.send(form)
    req.addEventListener('load', () => {
        location.reload()
    })
}

const task_del_btns = document.querySelectorAll('.task__delete')

task_del_btns.forEach(del_btn => {

    del_btn.addEventListener('click', function () {
        task_id = this.parentElement.id
        req.open('POST', '/kanban/delete_task/' + task_id)
        req.send(null)
        req.addEventListener('load', () => {
            location.reload()

        });
    });
});


let csrftoken = Cookies.get('csrftoken')
document.getElementById('login_form')
    .addEventListener('submit', e => {
        e.preventDefault()
        let name = document.getElementById('name')
        let password = document.getElementById('password')
        let formdata = new FormData()
        formdata.append('name', name.value)
        formdata.append('password', password.value)



        let options = {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            mode: 'same-origin',

        }
        options['body'] = formdata


        fetch("http://127.0.0.1:8000/books/test/", options)
            .then(response => response.json())
            .then(data => {
                if (data['status'] == 'ok') {
                    location.href = "http://127.0.0.1:8000/books/"
                }
                else {
                    console.log('Провал')
                }
            })
    })

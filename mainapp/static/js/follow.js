const csrftoken = Cookies.get('csrftoken')
const url = 'http://127.0.0.1:8000/books/follow/'

let options = {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    made: 'same-origin'
}


document.querySelectorAll("#reveal_input").forEach(follow => {
    follow.addEventListener('click', e => {
        e.preventDefault()
        const id = follow.dataset.id
        const action = follow.dataset.action

        let formdata = new FormData()
        formdata.append('id', id)
        formdata.append('action', action)
        options['body'] = formdata

        fetch(url, options)
            .then(response => response.json())
            .then(data => {
                if (data['status'] == 'ok') {
                    let previousaction = follow.dataset.action
                    let action = previousaction == 'follow' ? 'unfollow' : 'follow'
                    follow.dataset.action = action
                    follow.value = action

                    let followersCount = document.querySelector(`#followers${id}`)
                    let followerscount = parseInt(followersCount.innerHTML)
                    followersCount.innerHTML = previousaction == 'follow' ? followerscount + 1 : followerscount - 1

                }
            })
    })
})

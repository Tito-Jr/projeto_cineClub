const apiurl = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1'
const imgpath = 'http://image.tmdb.org/t/p/w1280'
const searchapi = 'https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query='

const main = document.getElementById('main')
const app = document.getElementById('app')
const form = document.getElementById('form')
const search = document.getElementById('search')

getMovies(apiurl)

async function getMovies(url){
    const resp = await fetch(url)
    const respData = await resp.json()

    showMovies(respData.results)
}

function showMovies(movies) {

    main.innerHTML = ''

    movies.forEach(movie => {
        const {poster_path, title, vote_average, overview} = movie
        const movieEl = document.createElement('div')
        movieEl.classList.add('movie')

        movieEl.innerHTML = `
        
            <button class="fav-btn">
                <i class="fas fa-heart"></i>
            </button>
            <button class="comment-btn">
                <i class="fa-regular fa-comment"></i>
            </button>
            <img src="${imgpath + poster_path}" 
            alt="${title}">
            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getClassByRate
                    (vote_average)}">${vote_average}</span>
            </div>
            <div class="overview">
                <h3>Movie Info</h3>    
                ${overview}
            </div>
        
        `
    
        const favBtn = movieEl.querySelector('.fav-btn') 
        favBtn.addEventListener("click", () => {
            favBtn.classList.toggle("active")
            console.log(title)
            let xhr = new XMLHttpRequest();
            xhr.open("POST", "/favoritos");
            xhr.send(title)
        })

        const commentBtn = movieEl.querySelector('.comment-btn') //incluir no action o endereço do servidor
        commentBtn.addEventListener("click", () => {
            let nome = title
            movieEl.innerHTML = `
            <form action="salvar_resenha" method="post"> 
                <input type="hidden" name="tituloFilme" value="${title}">
                <input type="text" name="nome" placeholder="nome">
                <input type="text" name="email" placeholder="email">
                <textarea name="resenha" cols="30" rows="10" placeholder="escreva sua resenha"></textarea>
                <button>postar</button>
            </form>`
        })

        history.pushState({}, null, '/index.html');
        main.appendChild(movieEl)
    })
}

function getClassByRate(vote){
    if(vote >= 8){
        return 'green';
    } else if (vote >= 5){
        return 'orange';
    } else {
        return 'red';
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault()

    const searchTerm = search.value

    if(searchTerm){
        getMovies(searchapi + searchTerm)
        search.value = ''
    }
})

document.querySelectorAll('[mynav]').forEach(link => {
    const conteudo = document.getElementById('conteudo')
    link.onclick = function(e){
        e.preventDefault()                
        fetch(link.getAttribute('mynav'))
            .then(resp => resp.text())
            .then(html => app.innerHTML = html)
    }
})

var xhttp = new XMLHttpRequest();
xhttp.open("GET", '/favoritos', true);

xhttp.onreadystatechange = function(){//Função a ser chamada quando a requisição retornar do servidor
    if ( xhttp.readyState == 4 && xhttp.status == 200 ) {//Verifica se o retorno do servidor deu certo
        result = xhttp.responseText
        console.log(result);
        const fav = document.getElementById('favoritos')
        vetor = result.split('-')
        
        for (var i = 0; i < vetor.length; i++) {
            fav.innerHTML += '<br>' + vetor[i]
        }
         
    }
}

xhttp.send();
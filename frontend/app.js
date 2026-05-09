const API = "https://super-duper-sniffle-695qrvxrg96qhrwrw-5000.app.github.dev"
// ─────────────────────────────────────────
// AUTH
// ─────────────────────────────────────────

function showTab(tab) {
    document.getElementById("loginForm").style.display = tab === "login" ? "block" : "none"
    document.getElementById("registerForm").style.display = tab === "register" ? "block" : "none"
    document.getElementById("showLogin").className = tab === "login" ? "active" : ""
    document.getElementById("showRegister").className = tab === "register" ? "active" : ""
}

async function register() {
    const name = document.getElementById("registerName").value
    const email = document.getElementById("registerEmail").value
    const password = document.getElementById("registerPassword").value

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",  // ← make sure this is here
        body: JSON.stringify({ name, email, password })
    })

    const data = await res.json()
    document.getElementById("registerMsg").innerText = data.message || data.error

    // auto switch to login after register
    if (res.ok) showTab("login")
}

async function login() {
    const email = document.getElementById("loginEmail").value
    const password = document.getElementById("loginPassword").value

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",  // important! sends cookies
        body: JSON.stringify({ email, password })
    })

    const data = await res.json()
    document.getElementById("loginMsg").innerText = data.message || data.error

    // redirect to dashboard on success
    if (res.ok) window.location.href = "dashboard.html"
}

async function logout() {
    await fetch(`${API}/logout`, {
        method: "POST",
        credentials: "include"
    })
    window.location.href = "index.html"
}

// ─────────────────────────────────────────
// MOVIES
// ─────────────────────────────────────────

async function loadMovies() {
    const res = await fetch(`${API}/movies`, {
        credentials: "include"  // sends session cookie
    })

    // if not logged in redirect to login
    if (res.status === 401) {
        window.location.href = "index.html"
        return
    }

    const movies = await res.json()
    const list = document.getElementById("movieList")
    list.innerHTML = ""

    if (movies.length === 0) {
        list.innerHTML = "<p>No movies yet! Add one above.</p>"
        return
    }

    movies.forEach(movie => {
        list.innerHTML += `
            <div class="movie-card ${movie.watched ? 'watched-card' : ''}">
                <div class="movie-info">
                    <h3>${movie.title}</h3>
                    <p>${movie.genre} | ${movie.watched ? "✅ Watched" : "⏳ Pending"}</p>
                </div>
                <div class="movie-actions">
                    ${!movie.watched ? `<button class="watched-btn" onclick="markWatched(${movie.id})">✅</button>` : ""}
                    <button class="delete-btn" onclick="deleteMovie(${movie.id})">🗑️</button>
                </div>
            </div>
        `
    })
}

async function addMovie() {
    const title = document.getElementById("movieTitle").value
    const genre = document.getElementById("movieGenre").value

    const res = await fetch(`${API}/movies`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ title, genre })
    })

    const data = await res.json()
    document.getElementById("addMsg").innerText = data.message || data.error

    // clear inputs and reload list
    document.getElementById("movieTitle").value = ""
    document.getElementById("movieGenre").value = ""
    loadMovies()
}

async function markWatched(id) {
    await fetch(`${API}/movies/${id}`, {
        method: "PATCH",
        credentials: "include"
    })
    loadMovies()
}

async function deleteMovie(id) {
    await fetch(`${API}/movies/${id}`, {
        method: "DELETE",
        credentials: "include"
    })
    loadMovies()
}

// ─────────────────────────────────────────
// Auto load movies if on dashboard
// ─────────────────────────────────────────
if (document.getElementById("movieList")) {
    loadMovies()
}
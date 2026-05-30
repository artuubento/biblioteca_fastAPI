const API_URL = "/livros";

const listaLivros = document.getElementById("listaLivros");
const form = document.getElementById("livroForm");


form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;

    const resposta = await fetch("/livros", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            titulo: titulo,
            autor: autor
        })
    });

    if (resposta.ok) {
        alert("Livro cadastrado!");
        carregarLivros();
        form.reset();
    }
});

async function carregarLivros() {

    const resposta = await fetch(API_URL);

    const livros = await resposta.json();

    listaLivros.innerHTML = "";

    livros.forEach(livro => {

        listaLivros.innerHTML += `
            <div class="card">

                <h3>${livro.titulo}</h3>

                <p>Autor: ${livro.autor}</p>

                <p class="${
                    livro.disponivel
                    ? 'disponivel'
                    : 'indisponivel'
                }">

                    ${
                        livro.disponivel
                        ? 'Disponível'
                        : 'Reservado'
                    }

                </p>

                <button onclick="reservar(${livro.id})">
                    Reservar
                </button>

                <button onclick="excluir(${livro.id})">
                    Excluir
                </button>

            </div>
        `;
    });
}

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;

    await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            titulo,
            autor
        })
    });

    form.reset();

    carregarLivros();
});

async function reservar(id) {

    await fetch(
        `/livros/${id}/reservar`,
        {
            method: "PUT"
        }
    );

    carregarLivros();
}

async function excluir(id) {

    await fetch(
        `/livros/${id}`,
        {
            method: "DELETE"
        }
    );

    carregarLivros();
}

carregarLivros();
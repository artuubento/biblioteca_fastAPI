from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Livro(BaseModel):
    titulo: str
    autor: str

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "disponivel": True
    },
    {
        "id": 2,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "disponivel": True
    },
    {
        "id": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "disponivel": True
    },
    {
        "id": 4,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
        "disponivel": True
    },
    {
        "id": 5,
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "autor": "J.R.R. Tolkien",
        "disponivel": True
    }
]

# HOME
@app.get("/")
def home():
    return {"mensagem": "API Biblioteca Comunitária"}

# LISTAR TODOS OS LIVROS
@app.get("/livros")
def listar_livros():
    return livros

# BUSCAR LIVRO POR ID
@app.get("/livros/{id}")
def buscar_livro(id: int):

    for livro in livros:
        if livro["id"] == id:
            return livro

    raise HTTPException(
        status_code=404,
        detail="Livro não encontrado"
    )

# CADASTRAR LIVRO
@app.post("/livros")
def adicionar_livro(livro: Livro):

    novo_livro = {
        "id": len(livros) + 1,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "disponivel": True
    }

    livros.append(novo_livro)

    return {
        "mensagem": "Livro cadastrado com sucesso",
        "livro": novo_livro
    }

# ATUALIZAR LIVRO
@app.put("/livros/{id}")
def atualizar_livro(id: int, livro_atualizado: Livro):

    for livro in livros:

        if livro["id"] == id:

            livro["titulo"] = livro_atualizado.titulo
            livro["autor"] = livro_atualizado.autor

            return {
                "mensagem": "Livro atualizado com sucesso",
                "livro": livro
            }

    raise HTTPException(
        status_code=404,
        detail="Livro não encontrado"
    )

# EXCLUIR LIVRO
@app.delete("/livros/{id}")
def excluir_livro(id: int):

    for indice, livro in enumerate(livros):

        if livro["id"] == id:

            livro_removido = livros.pop(indice)

            return {
                "mensagem": "Livro removido com sucesso",
                "livro": livro_removido
            }

    raise HTTPException(
        status_code=404,
        detail="Livro não encontrado"
    )

# RESERVAR LIVRO
@app.put("/livros/{id}/reservar")
def reservar_livro(id: int):

    for livro in livros:

        if livro["id"] == id:

            if not livro["disponivel"]:
                raise HTTPException(
                    status_code=400,
                    detail="Livro já reservado"
                )

            livro["disponivel"] = False

            return {
                "mensagem": "Livro reservado com sucesso",
                "livro": livro
            }

    raise HTTPException(
        status_code=404,
        detail="Livro não encontrado"
    )

# DEVOLVER LIVRO
@app.put("/livros/{id}/devolver")
def devolver_livro(id: int):

    for livro in livros:

        if livro["id"] == id:

            livro["disponivel"] = True

            return {
                "mensagem": "Livro devolvido com sucesso",
                "livro": livro
            }

    raise HTTPException(
        status_code=404,
        detail="Livro não encontrado"
    )
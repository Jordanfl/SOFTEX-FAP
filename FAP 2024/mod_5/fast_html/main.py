from fasthtml import FastHTML


app = FastHTML()


MAX_NAME_LENGTH = 50
MAX_MESSAGE_LENGTH = 200


def render_message(message):
    return f"""
    <article class="card">
        <header class="card-header">
            <p class="card-header-title">
            {message["name"]}
            </p>
        </header>
        <div class="card-content">
            <div class="content">
            {message["message"]}
            </div>
        </div>
        <footer class="card-footer">
            <p class="card-footer-item">
            <small><em class="has-text-grey">{message["timestamp"]}</em></small>
            </p>
        </footer>
    </article>
    """


def render_message_list(messages):
    return f"""
    <div>
        {' '.join([render_message(message) for message in messages])}
    </div>
    """


@app.get("/")
def read_root():
    return f"""
    <title>Meu Livro de Visitas ✍️</title>
    <div class="container">
        <h1>Deixe uma mensagem!</h1>
        <form method="POST" hx-post="/submit_message" hx-target="#messageList" hx-swap="innerHTML" hx-reset="this">
            <fieldset role="group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" maxlength="{MAX_NAME_LENGTH}" required>
            </fieldset>
            <fieldset role="group">
                <label for="message">Mensagem:</label>
                <textarea id="message" name="message" maxlength="{MAX_MESSAGE_LENGTH}" required></textarea>
            </fieldset>
            <button type="submit">Enviar</button>
        </form>
        <hr>
        <div id="messageList">
            {render_message_list(get_messages())}
        </div>
    </div>
    """


def get_messages():
    # Implementação da busca de mensagens do banco de dados virá aqui
    return []


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)

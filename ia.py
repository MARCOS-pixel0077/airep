import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios (CORS)

# Inicialize o cliente Cohere com sua chave de API
co = cohere.Client('NarNig6E0mkhWmrCS9LBAc6g9Xzi7DiimBvhxbiY')

def gerar_resposta(prompt):
    # Adiciona uma instrução para o modelo responder em português
    prompt_instruido = f"Responda em português do Brasil: {prompt}"
    
    # Fazendo a solicitação com geração de texto
    response = co.generate(
        model='command-xlarge',
        prompt=prompt_instruido,
        max_tokens=500,
        temperature=0.7,  # Controla a criatividade da resposta
        stop_sequences=["\n"]
    )
    
    # Retorna o texto gerado
    return response.generations[0].text.strip()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pergunta = data.get('pergunta')

    # Gera a resposta usando o Cohere
    resposta = gerar_resposta(pergunta)

    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
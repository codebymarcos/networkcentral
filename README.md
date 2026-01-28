# NetworkCentral

Um sistema centralizado para busca na web, binarização de resultados e visualização de sequências binárias.

## Funcionalidades

- **Busca na Web**: Realiza buscas usando DuckDuckGo e retorna resultados.
- **Binarização**: Converte textos em sequências binárias.
- **Plotagem**: Gera gráficos de sequências binárias (últimos 20 bits).
- **API Flask**: Interface web simples para interações.
- **Autenticação**: Validação de usuários via banco de dados JSON.

## Estrutura do Projeto

- `core/`: Módulos principais (search, binarization, plot).
- `objects/provedor/`: Classe Provider para gerenciar operações.
- `data.json`: Banco de dados de usuários.
- `conect.py`: API Flask mínima.

## Instalação

1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative: `source .venv/bin/activate` (Linux/Mac) ou `.venv\Scripts\activate` (Windows)
4. Instale dependências: `pip install flask ddgs matplotlib numpy`

## Uso

- Execute a API: `python objects/provedor/conect.py`
- Execute o provedor: `python objects/provedor/provedor.py`

## Exemplo

```python
from objects.provedor.provedor import Provider

user = {"id": 1, "password": "030202", "term": "exemplo"}
provider = Provider(user)
result = provider.upload(user)
print(result)
```

## Licença

MIT
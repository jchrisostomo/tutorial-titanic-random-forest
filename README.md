# Titanic - Random Forest

Classificação de sobrevivência no Titanic com `RandomForestClassifier` (scikit-learn),
usando a competição [Titanic do Kaggle](https://www.kaggle.com/competitions/titanic).

> **Versão 0.1 - estudo inicial do uso de random forest.**
> Baseado no tutorial [*Titanic Tutorial*](https://www.kaggle.com/code/alexisbcook/titanic-tutorial), de Alexis Cook (Kaggle), com a feature `FamilySize`,
> preenchimento de `Age` pela mediana do treino e validação (CV 5-fold + hold-out).
> O foco desta versão é montar o fluxo completo (dados → modelo → validação → submissão) com uma única
> configuração do modelo (`n_estimators=100`, `max_depth=5`); não há ainda comparação com outros modelos nem ajuste de hiperparâmetros.

## Resultados

| Métrica | Valor |
|---|---|
| Acurácia (CV 5-fold) | 82,83% |
| Acurácia (hold-out 20%) | 82,68% |

## Próximos passos

- Gráfico de importância das features (`feature_importances_`).
- Comparar uma árvore de decisão única com a floresta, para mostrar o ganho do ensemble.
- Avaliar o efeito de `max_depth` e `n_estimators` na acurácia (CV).

## Como reproduzir

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

**Dados (Kaggle API):**

1. **Gerar o token.** No Kaggle, clique na sua foto/nome (canto superior direito) → **Your API tokens** (ou *Settings* → aba **API Tokens**) → **Generate New Token**.
2. **Copie o token na hora.** Ele aparece uma única vez; se perder, basta gerar outro (gerar um novo não invalida os anteriores).
3. **Salvar no sistema** (escolha uma das opções; nunca commite o token):
   - **Arquivo** (recomendado, o cliente lê automaticamente):
     ```bash
     mkdir -p ~/.kaggle && echo "SEU_TOKEN" > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token
     ```
   - **Variável de ambiente** (vale só para o terminal atual; para persistir, ponha a linha no `~/.bashrc`):
     ```bash
     export KAGGLE_API_TOKEN=SEU_TOKEN
     ```
4. **Aceitar as regras da competição** em <https://www.kaggle.com/competitions/titanic> (senão o download retorna 403).
5. Rode `python scripts/download_data.py` (também é chamado automaticamente pelo notebook se `data/train.csv` não existir).

> Tokens de API exigem `kagglehub >= 0.4.1` (ou Kaggle CLI >= 1.8.0). 

Depois abra `notebooks/titanic_random_forest.ipynb` e execute todas as células.
A submissão é gerada em `outputs/submission.csv`.

## Estrutura

```
├── notebooks/titanic_random_forest.ipynb
├── scripts/download_data.py
├── data/        # baixado, ignorado pelo git
├── outputs/     # submission.csv, ignorado pelo git
└── requirements.txt
```

## Créditos

Este estudo parte do tutorial [*Titanic Tutorial*](https://www.kaggle.com/code/alexisbcook/titanic-tutorial), de Alexis Cook (Kaggle). Dados © Kaggle.

# CapitalCare

CapitalCare é uma plataforma web para gestão financeira pessoal construída com Django e Django REST Framework. O sistema centraliza o cadastro de rendas, gastos e investimentos, gera dashboards analíticos em tempo real e expõe APIs autenticadas para integrar os dados com outros serviços. A aplicação oferece páginas responsivas com Tailwind CSS e utilitários para popular o ambiente com dados de teste, permitindo que usuários monitorem e planejem sua saúde financeira de ponta a ponta.

## Principais funcionalidades

- **Autenticação e onboarding** – fluxos de cadastro, login e logout baseados em um usuário customizado com identificador UUID e validação de credenciais. Mensagens de feedback orientam a experiência do usuário em cada etapa de autenticação.【F:home/views.py†L1-L69】【F:users/models.py†L1-L25】
- **Gestão de rendas** – CRUD completo para lançamentos de renda e respectivos tipos, com filtros, agregações (total, média, mínimo, máximo) e anotações por categoria. Serviços encapsulam a criação/edição e ainda geram gráficos Plotly diretamente consumíveis pelas views.【F:renda/models.py†L1-L57】【F:renda/services/rendas.py†L1-L117】【F:renda/selectors/rendas.py†L1-L44】
- **Gestão de gastos** – organização dos gastos por tipos (ex.: débito automático) e categorias (ex.: contas básicas), incluindo observações opcionais. Os dados alimentam dashboards e APIs para acompanhamento das despesas.【F:gasto/models.py†L1-L79】
- **Gestão de investimentos** – registro de operações de compra e venda, tipos de investimento e ativos monitorados, com observações e ordenação por data para facilitar o acompanhamento da carteira.【F:investimento/models.py†L1-L61】
- **Dashboard financeiro** – visão consolidada das movimentações do usuário, exibindo totais de rendas, gastos, investimentos e cálculo de saldo disponível, além de análises por mês atual e projeções para o próximo mês usando seletores reutilizáveis.【F:dashboard/views.py†L1-L120】
- **APIs REST autenticadas** – endpoints protegidos via token de sessão que fornecem listas de rendas e tipos, bem como agregações e anotações pré-calculadas, prontos para consumo por front-ends ou integrações externas.【F:renda/urls.py†L1-L40】【F:renda/views/api.py†L1-L39】
- **Utilitários de geração de dados** – scripts com Faker para criar rapidamente séries históricas de rendas, gastos e investimentos, úteis para demos e testes de performance dos gráficos.【F:utils/make.py†L1-L168】
- **Camada de front-end** – assets gerenciados com Tailwind CSS e PostCSS, com scripts de build para os estilos globais e para o diretório `Frontend`, permitindo ajustes visuais consistentes entre as páginas Django e protótipos estáticos.【F:package.json†L1-L19】【F:tailwind.config.js†L1-L13】

## Estrutura do projeto

- `core/` – configurações base do Django, integração com dotenv, middlewares (incluindo debug toolbar e CORS), além do roteamento principal da aplicação.【F:core/settings.py†L1-L121】【F:core/urls.py†L1-L13】
- `home/` – páginas públicas, formulários de autenticação e fluxo de registro de usuários, com templates dedicados para index, login e cadastro.【F:home/views.py†L1-L69】【F:home/templates/home/pages/index.html†L1-L200】
- `dashboard/` – views protegidas por login que compilam dados das demais apps e renderizam templates analíticos.【F:dashboard/views.py†L1-L120】
- `renda/`, `gasto/`, `investimento/` – domínio financeiro separado por tipo de lançamento, cada um com modelos, formulários, filtros, services, selectors, serializers e templates próprios.【F:renda/models.py†L1-L57】【F:gasto/models.py†L1-L79】【F:investimento/models.py†L1-L61】
- `users/` – implementação do usuário customizado com UUID, campos extras e integração com os formulários de autenticação.【F:users/models.py†L1-L25】
- `utils/` – utilidades reutilizáveis, incluindo decoradores, regras de senha forte e scripts de geração de dados fictícios.【F:utils/make.py†L1-L168】【F:utils/strong_password.py†L1-L200】
- `base_templates/` e `base_static/` – componentes compartilhados de UI e assets compilados a partir do pipeline Tailwind/PostCSS.【F:package.json†L1-L19】
- `Frontend/` – protótipos estáticos e assets independentes que podem servir de base para um futuro SPA ou landing page personalizada.【F:Frontend/index.html†L1-L200】

## Executando o projeto localmente

1. **Instale as dependências Python**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure variáveis de ambiente** compatíveis com o banco relacional desejado (MySQL ou PostgreSQL são suportados) conforme os parâmetros esperados em `core/settings.py` (`DATABASE_ENGINE`, `DATABASE_NAME`, etc.).【F:core/settings.py†L49-L73】
3. **Aplique as migrações e crie um superusuário**:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```
5. (Opcional) **Compile os estilos Tailwind** para os templates Django ou para o diretório Frontend:
   ```bash
   npm install
   npm run dev      # gera base_static/global/css/style.css
   npm run front    # gera Frontend/vendor/css/style.css
   ```

Com o servidor ativo, acesse `http://localhost:8000/` para utilizar a interface web ou os endpoints REST autenticados (`/rendas/api/v1/...`). Use os utilitários de `utils/make.py` em um shell Django para gerar dados sintéticos e experimentar os dashboards rapidamente.

# Forma

**Forma** is a structure-driven software generator.

Instead of generating code directly from AI prompts, Forma builds software through a structural pipeline:

Natural Language → Domain Model → Backend → Frontend

---

# Concept

Most AI coding tools follow this pattern:

Natural Language → Code

Forma follows a different architecture:

Natural Language  
↓  
Domain Model  
↓  
Software

This approach enables **deterministic software generation** instead of unpredictable AI code output.

---

# v0.2 Features

Forma v0.2 generates a **full stack CRUD admin application**.

Pipeline:

Natural Language  
↓  
Domain Model  
↓  
FastAPI Backend  
↓  
React Admin UI

---

# Example

Input:


Customers have name and email
Orders have date


Generated application includes:

Database  
API  
Admin UI

---

# Generated Project Structure


generated_app

main.py
database.py

models
customer.py
order.py

routers
customers.py
orders.py

frontend

package.json
vite.config.ts

src

    App.tsx

    pages
        CustomerPage.tsx
        OrderPage.tsx

    api
        client.ts
        customer.ts
        order.ts

---

# Installation

Clone the repository.


git clone <repo>
cd forma


Create Python environment.


python -m venv venv
source venv/bin/activate


Install dependencies.


pip install fastapi uvicorn sqlalchemy


---

# Generate Application


python cli.py dev "
Customers have name and email
Orders have date
"


---

# Run Backend


cd generated_app
uvicorn main:app --reload


Open:


http://localhost:8000/docs


---

# Run Frontend


cd generated_app/frontend
npm install
npm run dev


Open:


http://localhost:5173


---

# What You Get

Generated admin interface:

Customers

ID | Name | Email

Create form:

Name  
Email

Saved through:

POST /customers

---

# Architecture


Natural Language
↓
Parser
↓
Domain Model
↓
SQLAlchemy Models
↓
FastAPI Routers
↓
React Admin UI


---

# Project Philosophy

Forma is not an AI code generator.

Forma is a **Structure Driven Development Engine**.

The goal is to make software generation **deterministic and reproducible**.

---

# Next Step

v0.3 will introduce:

DomainModel → UI auto generation

Meaning:

Natural Language  
↓  
Domain Model  
↓  
DB  
↓  
API  
↓  
UI

will become fully synchronized.

# License

[MIT License](LICENSE)


# Forma（日本語）

**Forma** は構造駆動型ソフトウェア生成エンジンです。

多くのAIツールは

Natural Language → Code

という形でコードを生成します。

Formaは次のアーキテクチャを採用します。

Natural Language  
↓  
Domain Model  
↓  
Software

AIではなく **構造を中心にソフトウェアを生成する**のが特徴です。

---

# v0.2 機能

Forma v0.2では

**フルスタックCRUDアプリケーション**

を生成できます。

パイプライン

Natural Language  
↓  
Domain Model  
↓  
FastAPI Backend  
↓  
React Admin UI

---

# 入力例


Customers have name and email
Orders have date


生成されるもの

- Database
- API
- Admin UI

---

# 生成される構造


generated_app

main.py
database.py

models
customer.py
order.py

routers
customers.py
orders.py

frontend

package.json
vite.config.ts

src

    App.tsx

    pages
        CustomerPage.tsx
        OrderPage.tsx

    api
        client.ts
        customer.ts
        order.ts

---

# セットアップ

リポジトリを取得


git clone <repo>
cd forma


Python環境作成


python -m venv venv
source venv/bin/activate


依存関係インストール


pip install fastapi uvicorn sqlalchemy


---

# アプリ生成


python cli.py dev "
Customers have name and email
Orders have date
"


---

# Backend 起動


cd generated_app
uvicorn main:app --reload


ブラウザ


http://localhost:8000/docs


---

# Frontend 起動


cd generated_app/frontend
npm install
npm run dev


ブラウザ


http://localhost:5173


---

# 生成されるUI

Customers


ID | Name | Email


Create


Name
Email


保存


POST /customers


---

# アーキテクチャ


Natural Language
↓
Parser
↓
Domain Model
↓
SQLAlchemy Models
↓
FastAPI Routers
↓
React Admin UI


---

# Forma の思想

Formaは

AIコード生成ツールではありません。

Formaは

**Structure Driven Development Engine**

です。

構造を中心にソフトウェアを生成します。

---

# 次のステップ

v0.3では


DomainModel → UI


を完全自動化します。

つまり

Natural Language  
↓  
Domain Model  
↓  
DB  
↓  
API  
↓  
UI  

がすべて同期されるようになります。

# License

[MIT License](LICENSE)

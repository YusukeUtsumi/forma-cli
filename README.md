# Forma

**Forma** is an experimental AI-native development engine that converts natural language into structured software.

Instead of generating code directly, Forma first builds a **Domain Model**, then generates APIs and application structures from it.

```
Natural Language
        ↓
    Domain Model
        ↓
    ER Diagram
        ↓
    FastAPI Application
```

This approach treats software generation as a **structure-first problem**, not a code generation problem.

---

# Example

Input:

```
Customers place orders.
Orders contain products.
Customers have name and email.
```

Generated:

```
generated_app/
├ schema.er
├ main.py
├ database.py
├ models/
│   ├ customer.py
│   ├ order.py
│   └ product.py
└ routers/
    ├ customers.py
    ├ orders.py
    └ products.py
```

ER diagram:

```
erDiagram
Customer ||--o{ Order
Order ||--o{ Product
```

FastAPI endpoints:

```
GET  /customers
POST /customers

GET  /orders
POST /orders

GET  /products
POST /products
```

---

# Installation

Clone the repository:

```
git clone https://github.com/YusukeUtsumi/forma-cli
cd forma-cli
```

Install dependencies:

```
pip install fastapi uvicorn sqlalchemy
```

---

# Usage

Run Forma with natural language input:

```
python cli.py dev "
Customers place orders.
Orders contain products.
Customers have name and email.
"
```

This generates a FastAPI project in:

```
generated_app/
```

Start the API server:

```
cd generated_app
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# Architecture

Forma follows a **structure-first generation pipeline**:

```
Natural Language
        ↓
Parser
        ↓
Domain Model
        ↓
Generators
        ↓
Application
```

Project structure:

```
forma/
│
├ cli.py
│
├ parser
│   ├ entity_extractor.py
│   ├ relation_extractor.py
│   └ field_extractor.py
│
├ domain
│   └ domain_model.py
│
├ generator
│   ├ er_generator.py
│   ├ sqlalchemy_generator.py
│   ├ api_generator.py
│   └ project_generator.py
```

---

# Why Forma?

Most AI coding tools follow this pipeline:

```
Natural Language → Code
```

Forma takes a different approach:

```
Natural Language → Structure → Software
```

By introducing a **Domain Model layer**, software can be generated more consistently and extended to multiple targets.

Future generators could include:

```
React UI
GraphQL
Infrastructure (Terraform)
Admin dashboards
```

---

# Roadmap

### v0.1

Natural language → Domain Model → FastAPI CRUD generation

### v0.2

React admin UI generator

### v0.3

Full no-code mode

```
describe your app
```

→ complete application generation

---

# Status

Experimental project.

---

# License

[MIT License](LICENSE)


# Forma

**Forma** は、自然言語からソフトウェア構造を生成する
**AIネイティブな開発エンジン（AI Native Development Engine）**の実験プロジェクトです。

Formaはコードを直接生成するのではなく、まず **ドメインモデル（構造）** を作り、
そこからアプリケーションを生成します。

```
自然言語
    ↓
ドメインモデル
    ↓
ER図
    ↓
FastAPIアプリケーション
```

このアプローチでは、ソフトウェア生成を
**「コード生成」ではなく「構造生成」**として扱います。

---

# 例

入力（自然言語）

```
Customers place orders.
Orders contain products.
Customers have name and email.
```

生成されるアプリケーション

```
generated_app/
├ schema.er
├ main.py
├ database.py
├ models/
│   ├ customer.py
│   ├ order.py
│   └ product.py
└ routers/
    ├ customers.py
    ├ orders.py
    └ products.py
```

ER図

```
erDiagram
Customer ||--o{ Order
Order ||--o{ Product
```

生成されるAPI

```
GET  /customers
POST /customers

GET  /orders
POST /orders

GET  /products
POST /products
```

---

# インストール

リポジトリをクローンします。

```
git clone https://github.com/YusukeUtsumi/forma-cli
cd forma-cli
```

必要なパッケージをインストールします。

```
pip install fastapi uvicorn sqlalchemy
```

---

# 使い方

自然言語を入力して実行します。

```
python cli.py dev "
Customers place orders.
Orders contain products.
Customers have name and email.
"
```

すると以下が生成されます。

```
generated_app/
```

APIサーバーを起動します。

```
cd generated_app
uvicorn main:app --reload
```

ブラウザで開きます。

```
http://127.0.0.1:8000/docs
```

---

# アーキテクチャ

Formaは **構造生成パイプライン**を採用しています。

```
自然言語
    ↓
Parser
    ↓
Domain Model
    ↓
Generators
    ↓
Application
```

プロジェクト構造

```
forma/
│
├ cli.py
│
├ parser
│   ├ entity_extractor.py
│   ├ relation_extractor.py
│   └ field_extractor.py
│
├ domain
│   └ domain_model.py
│
├ generator
│   ├ er_generator.py
│   ├ sqlalchemy_generator.py
│   ├ api_generator.py
│   └ project_generator.py
```

---

# なぜForma？

多くのAIコーディングツールは次の構造です。

```
自然言語 → コード
```

Formaは異なるアプローチを取ります。

```
自然言語 → 構造 → ソフトウェア
```

ドメインモデル層を挟むことで、
複数の生成ターゲットへ拡張できる設計になっています。

将来的には以下の生成も可能になります。

```
React UI
GraphQL API
Terraform (インフラ)
Adminダッシュボード
```

---

# ロードマップ

### v0.1

自然言語 → Domain Model → FastAPI CRUD生成

### v0.2

React Admin UI 自動生成

### v0.3

完全ノーコードモード

```
describe your app
```

だけでアプリケーション生成。

---

# ステータス

実験的プロジェクト。

---

# ライセンス

[MIT License](LICENSE)

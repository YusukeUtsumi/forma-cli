import os


def generate_frontend_project(domain_model, output_dir="generated_app"):

    frontend_dir = os.path.join(output_dir, "frontend")
    src_dir = os.path.join(frontend_dir, "src")

    os.makedirs(src_dir, exist_ok=True)

    generate_package_json(frontend_dir)
    generate_vite_config(frontend_dir)
    generate_index_html(frontend_dir)
    generate_main_tsx(src_dir)
    generate_app_tsx(src_dir)

    generate_api_clients(domain_model, src_dir)

    print("Frontend project generated.")


def generate_package_json(frontend_dir):

    content = """{
  "name": "forma-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.2.2",
    "vite": "^5.0.0"
  }
}
"""

    with open(os.path.join(frontend_dir, "package.json"), "w") as f:
        f.write(content)


def generate_vite_config(frontend_dir):

    content = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [react()],
    server: {
        port: 5173
    }
})
"""

    with open(os.path.join(frontend_dir, "vite.config.ts"), "w") as f:
        f.write(content)


def generate_index_html(frontend_dir):

    content = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <title>Forma App</title>
</head>

<body>

<div id="root"></div>

<script type="module" src="/src/main.tsx"></script>

</body>

</html>
"""

    with open(os.path.join(frontend_dir, "index.html"), "w") as f:
        f.write(content)


def generate_main_tsx(src_dir):

    content = """import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App"

ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)
"""

    with open(os.path.join(src_dir, "main.tsx"), "w") as f:
        f.write(content)


def generate_app_tsx(src_dir):

    content = """import React from "react"

function App() {

    return (
        <div style={{ padding: 40 }}>

            <h1>Forma Generated App</h1>

            <p>Frontend ready.</p>

        </div>
    )

}

export default App
"""

    with open(os.path.join(src_dir, "App.tsx"), "w") as f:
        f.write(content)


def generate_api_clients(domain_model, src_dir):

    api_dir = os.path.join(src_dir, "api")

    os.makedirs(api_dir, exist_ok=True)

    generate_api_client_base(api_dir)

    for entity in domain_model.entities:
        generate_entity_api(entity, api_dir)


def generate_api_client_base(api_dir):

    content = """const BASE_URL = "http://localhost:8000"

export async function apiGet(path: string) {

    const res = await fetch(BASE_URL + path)

    return res.json()
}

export async function apiPost(path: string, data: any) {

    const res = await fetch(BASE_URL + path, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    return res.json()
}
"""

    with open(os.path.join(api_dir, "client.ts"), "w") as f:
        f.write(content)


def generate_entity_api(entity, api_dir):

    name = entity.lower()
    filename = f"{name}.ts"

    content = f"""import {{ apiGet, apiPost }} from "./client"

export async function get{name.capitalize()}s() {{

    return apiGet("/{name}s")
}}

export async function create{name.capitalize()}(data: any) {{

    return apiPost("/{name}s", data)
}}
"""

    with open(os.path.join(api_dir, filename), "w") as f:
        f.write(content)
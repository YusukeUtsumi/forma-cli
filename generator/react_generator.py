import os


def generate_frontend_project(domain_model, output_dir="generated_app"):

    frontend_dir = os.path.join(output_dir, "frontend")
    src_dir = os.path.join(frontend_dir, "src")

    os.makedirs(src_dir, exist_ok=True)

    generate_package_json(frontend_dir)
    generate_vite_config(frontend_dir)
    generate_index_html(frontend_dir)
    
    generate_main_tsx(src_dir)

    generate_table_component(src_dir)

    generate_pages(domain_model, src_dir)

    generate_app_tsx(src_dir, domain_model)

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

def generate_table_component(src_dir):

    components_dir = os.path.join(src_dir, "components")
    os.makedirs(components_dir, exist_ok=True)

    content = """import React from "react"

type Props = {
    columns: string[]
    data: any[]
}

function DataTable({ columns, data }: Props) {

    return (
        <table border={1} cellPadding={8}>

            <thead>
                <tr>
                    {columns.map(col => (
                        <th key={col}>{col}</th>
                    ))}
                </tr>
            </thead>

            <tbody>

                {data.map((row, i) => (
                    <tr key={i}>
                        {columns.map(col => (
                            <td key={col}>{row[col]}</td>
                        ))}
                    </tr>
                ))}

            </tbody>

        </table>
    )
}

export default DataTable
"""

    with open(os.path.join(components_dir, "DataTable.tsx"), "w") as f:
        f.write(content)

def generate_pages(domain_model, src_dir):

    pages_dir = os.path.join(src_dir, "pages")

    os.makedirs(pages_dir, exist_ok=True)

    for entity in domain_model.entities:

        generate_entity_page(entity, pages_dir)

def generate_entity_page(entity, pages_dir):

    name = entity.lower()
    cname = entity.capitalize()

    filename = f"{cname}Page.tsx"

    content = f"""import React, {{ useEffect, useState }} from "react"
import DataTable from "../components/DataTable"
import {{ get{cname}s }} from "../api/{name}"

function {cname}Page() {{

    const [data, setData] = useState<any[]>([])

    useEffect(() => {{

        load()

    }}, [])

    async function load() {{

        const res = await get{cname}s()

        setData(res)

    }}

    if (data.length === 0) {{

        return <p>Loading...</p>

    }}

    const columns = Object.keys(data[0])

    return (

        <div style={{{{ padding: 40 }}}}>

            <h2>{cname}s</h2>

            <DataTable columns={{columns}} data={{data}} />

        </div>

    )

}}

export default {cname}Page
"""

    with open(os.path.join(pages_dir, filename), "w") as f:
        f.write(content)

def generate_app_tsx(src_dir, domain_model):

    imports = ""
    routes = ""

    for entity in domain_model.entities:

        cname = entity.capitalize()
        name = entity.lower()

        imports += f'import {cname}Page from "./pages/{cname}Page"\n'
        routes += f'<a href="/{name}s">{cname}s</a><br/>\n'

    content = f"""import React from "react"

{imports}

function App() {{

    const path = window.location.pathname

    if (path === "/") {{

        return (

            <div style={{{{ padding: 40 }}}}>

                <h1>Forma Admin</h1>

                {routes}

            </div>

        )

    }}
"""

    for entity in domain_model.entities:

        cname = entity.capitalize()
        name = entity.lower()

        content += f"""
    if (path === "/{name}s") {{
        return <{cname}Page />
    }}
"""

    content += """

    return <p>Not Found</p>

}

export default App
"""

    with open(os.path.join(src_dir, "App.tsx"), "w") as f:
        f.write(content)
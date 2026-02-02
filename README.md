# 📊 Dashboard Interativo de Salários na Área de Dados

## 📋 Descrição do Projeto
Este projeto consiste em um **dashboard interativo** desenvolvido em **Python**, utilizando **Streamlit**, para análise e visualização de salários de profissionais da área de dados.

---

## 🎯 Filtros Interativos
O dashboard permite a aplicação dos seguintes filtros:

- **Ano**  
  Selecione um ou múltiplos anos de análise.

- **Senioridade**  
  Filtragem por nível de experiência (Júnior, Pleno, Sênior, etc.).

- **Tipo de Contrato**  
  Escolha entre diferentes modalidades de contratação (CLT, PJ, etc.).

- **Tamanho da Empresa**  
  Filtragem por porte da organização.

---

## 📈 Visualizações e Métricas

### 📌 Métricas Principais (KPIs)
- Salário médio anual (USD)
- Salário máximo registrado
- Total de registros filtrados
- Cargo mais frequente

### 📊 Gráficos Interativos
- **Top 10 cargos por salário médio** (gráfico de barras horizontais)
- **Distribuição de salários anuais** (histograma)
- **Proporção dos tipos de trabalho** (gráfico de pizza)
- **Mapa mundial de salários médios de Data Scientists** (mapa coroplético)

---

## 🎨 Temas Personalizáveis
- Alternância entre **Modo Claro ☀️** e **Modo Escuro 🌙**
- Gráficos e interface adaptam-se automaticamente ao tema selecionado
- Preferência de tema mantida durante a sessão

---

## 📊 Tabela de Dados
- Visualização completa dos dados filtrados
- Tabela interativa com ordenação e pesquisa

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia        | Versão | Descrição                                   |
|------------------|--------|---------------------------------------------|
| Python           | 3.8+   | Linguagem de programação principal           |
| Streamlit        | 1.28+  | Framework para aplicações web interativas   |
| Pandas           | 2.0+   | Manipulação e análise de dados              |
| Plotly           | 5.0+   | Visualizações gráficas interativas          |
| Plotly Express   | -      | Interface simplificada para gráficos Plotly |

---

## 📊 Fontes de Dados
- Os dados são carregados automaticamente de um **arquivo CSV hospedado no GitHub**
- **Atualização periódica**, conforme a fonte original

### 📂 Estrutura dos Dados
O dataset contém as seguintes colunas:

- `ano` — Ano da observação  
- `cargo` — Posição/role do profissional  
- `senioridade` — Nível de experiência  
- `contrato` — Tipo de contrato (CLT, PJ, etc.)  
- `tamanho_empresa` — Porte da organização  
- `remoto` — Modalidade de trabalho (Presencial, Híbrido, Remoto)  
- `residencia_iso3` — Código ISO3 do país de residência  
- `usd` — Salário anual em dólares americanos  

---

## 🎮 Como Usar

### 1️⃣ Aplicar Filtros
- Utilize os filtros na barra lateral
- Selecione múltiplas opções em cada categoria
- Gráficos e métricas são atualizados em tempo real

### 2️⃣ Analisar as Métricas
- Consulte os KPIs no topo do dashboard
- Observe as variações conforme os filtros aplicados

### 3️⃣ Explorar os Gráficos
- Passe o mouse para visualizar detalhes
- Utilize zoom e interações do Plotly
- Clique nas legendas para ocultar/exibir categorias

### 4️⃣ Alternar Tema
- Clique em **🌙 Modo Escuro** ou **☀️ Modo Claro** na sidebar
- Interface e gráficos se adaptam automaticamente

### 5️⃣ Exportar Dados
- Os dados filtrados aparecem na tabela inferior
- Utilize os controles do Streamlit
- Copie os dados manualmente conforme necessário

---

## 🔧 Personalização

### 🎨 Modificar Cores e Estilos
- **Tema Claro**: editar configurações entre as linhas 46–58
- **Tema Escuro**: editar configurações entre as linhas 35–45
- **Cores dos Gráficos**: ajustar sequências em `px.bar()`, `px.histogram()`, etc.

### ➕ Adicionar Novos Filtros
1. Adicione o widget na seção **Barra Lateral**
2. Modifique a filtragem do DataFrame
3. Atualize gráficos e métricas

### 🚀 Extensões Futuras
- Exportação de dados (CSV / Excel)
- Comparação entre anos
- Novos tipos de gráficos
- Análises por país ou região

---

## 📱 Compatibilidade
- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Dispositivos**:  
  - Desktop (otimizado)  
  - Tablet (funcional)  
  - Mobile (visualização básica)
- **Sistemas Operacionais**: Windows, macOS, Linux

---

## 🤝 Contribuindo
Contribuições são bem-vindas!

1. Faça um **fork** do projeto  
2. Crie uma branch:  
   ```bash
   git checkout -b feature/NovaFuncionalidade


---

Desenvolvido com ❤️ para a comunidade de dados.

Dashboard atualizado em 2026 — Análise de salários na área de dados.

### ⭐ Se você gostou deste projeto, considere dar uma estrela no repositório!
### 🔔 Fique atento para futuras atualizações e novas funcionalidades.

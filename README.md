# LangChain Prompt Engineering & Chat Implementation

> **Note:** This documentation was AI-generated using a custom prompt to synthesize technical workflows into a structured, readable format for developers and reviewers.

This repository explores the foundational concepts of **Prompt Engineering** within the LangChain ecosystem. The primary motivation for using custom prompts is security and control; by wrapping user input within predefined templates, we prevent users from having direct "power" over the LLM, thereby mitigating prompt injection and ensuring consistent output formats.

---

## 🛠 Features & Implementations

### 1. Prompt Templates (`prompt_generator.py`)
Standardizes how we format inputs before sending them to the Model.
*   **Validation:** By setting `validate_template=True`, the application ensures that all defined input variables are present, throwing an error otherwise.
*   **Serialization:** Templates can be exported/saved as `.json` files for modularity and easy loading in different environments.

### 2. Streamlit Integration (`prompt_ui.py`)
A web-based interface built with **Streamlit** and **ChatGoogleGenerativeAI**.
*   **Dynamic Loading:** Uses `load_prompt` to fetch saved JSON templates.
*   **Execution:** Integrates `PromptTemplate` and the LLM into a chain.
*   **User Interaction:** Collects variables via `st.selectbox` and invokes the chain with a dictionary mapping input variables to user selections.

### 3. Message Types & Chat Context
LangChain uses specific message schemas to define the "role" of the text:
*   **SystemMessage:** Sets the behavior/persona (e.g., "You are a helpful assistant").
*   **HumanMessage:** Represents the user's input.
*   **AIMessage:** Represents the model's response.

### 4. Terminal Chatbot with History (`chatbot.py`)
A loop-based terminal application that maintains a conversation state.
*   **Memory Management:** Every `HumanMessage` and `AIMessage` is appended to a `chat_history` list.
*   **Context Awareness:** The entire history is sent back to the model with every new query, allowing the LLM to "remember" previous interactions.
*   **Persistence:** The session history is logged/stored in the repository for audit or future loading.

### 5. Advanced Context with MessagePlaceholders (`message_placeholder.py`)
Uses `MessagesPlaceholder` to dynamically inject variable-length chat history into a prompt.
*   **Structure:**
    1.  `SystemMessage` (Fixed)
    2.  `MessagesPlaceholder` (Dynamic history loaded from `chathistory.txt`)
    3.  `HumanMessage` (Current query)
*   **Workflow:** Reads a text file, strips lines, formats them into message objects, and invokes the template to generate a context-rich prompt.

### 6. Chat Prompt Templates (`chatprompttemplate.py`)
A streamlined way to handle multi-turn or role-based prompts.
*   Combines system and human templates into a single `ChatPromptTemplate` object.
*   Allows for variables in both the system instructions and the user query for maximum flexibility.

---

## 🚀 How to Run

1.  **Clone the Repo**
2.  **Set API Keys:** Ensure your Google API Key is configured in your environment.
3.  **Run UI:** 
   
    streamlit run prompt_ui.py


    python chatbot.py

    ## 🔗 Live Demo
*The Streamlit application link will be updated here once deployed.*

---
*Created as part of a LangChain deep-dive series.*

 ```bash

"""#we need to reload
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_hitory'),
    ('human', '{query}') #where is my refund no cotext 
])

chat_history = []
#load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
#create prompt

print(chat_history)

prompt = chat_template.invoke({'chat_history': chat_history,'query':'Where is my Refund?'})
print(prompt)"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. FIXED: Added the 's' to variable_name
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), 
    ('human', '{query}')
])

chat_history = []
# 2. PRO-TIP: Reading lines usually keeps the newline character '\n'
# You might want to strip them so the AI doesn't see messy formatting
with open('chat_history.txt') as f:
    chat_history.extend([line.strip() for line in f.readlines()])

# 3. MATCHED: The key here now matches the variable_name above
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'Where is my Refund?'
})

print(prompt)
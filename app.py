
# this is my main code file

__import__('pysqlite3')  # Dynamically imports the pysqlite3 module
import sys  # Imports the sys module necessary to modify system properties
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')  # Replaces the sqlite3 entry in sys.modules with pysqlite3
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import time
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
class ChatBot():
    def __init__(self, per_dir, templatee):
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        embeddings = HuggingFaceEmbeddings()
        
        collection_name = "urdu_book_collection"
        self.knowledge = Chroma(
            collection_name=collection_name,
            persist_directory=per_dir,
            embedding_function=embeddings
        )

        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
        
        # Inject templatee directly into the prompt template
        self.template = f"""
        {templatee}

        Context: {{context}}

        Question: {{question}}

        Answer:
        """
        
        self.prompt = PromptTemplate(
            template=self.template,
            input_variables=["context", "question"]
        )
        
        self.rag_chain = (
            {"context": self.knowledge.as_retriever(), "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

# Create an instance of the ChatBot class
bot1 = ChatBot("urdubookcollection","this is the data from the book Jami-Khalq-par-Huzoor-ki-Rahmat-o-Shafqat written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot2 = ChatBot("urdubookcollections2","this is the data from the book Fitna e Khawarij written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot3 = ChatBot("urdubookcollections3","this is the data from the book Gustakh e Rasool - Ahadith e Nabvi ki roshani mein written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot4 = ChatBot("urdubookcollections4","this is the data from the book Rihla-fi-Talab-il-Ilm written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot5 = ChatBot("urdubookcollections5","this is the data from the book Yaqoot-wal-Marjan written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot6 = ChatBot("urdubookcollections6","this is the data from the book Zubdat-ul-Irfan written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")
bot7 = ChatBot("urdubookcollections7","this is the data from the book al-Jihad al-Akbar written by huzoor sheikh ul islam dr muhammad tahir ul qadri, whatever question is asked you have to answer that properly and comprehensively. Whatever question is asked you have to answer properly and comprehensively also, whenever a question is asked from this book you always have to answer the question in Urdu language no matter if in prompt it mentions to answer in Urdu or not, but if it specifies to answer in some other language, only then you have to change the language in giving a response.")

st.set_page_config(page_title="Urdu Book Bot")

# Injecting CSS for better alignment and readability
st.markdown(
    """
    <style>
    .checkbox-label {
        display: inline-block;
        margin-right: 10px;
        font-size: 20px;
        line-height: 1.5;
        vertical-align: middle;
    }
    .stCheckbox > label {
        display: flex;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.title('Urdu Book Bot')
    book1, book2, book3, book4, book5, book6, book7 = st.columns(7)
    # Display checkboxes with improved CSS styling for readability
    book1_selected = st.checkbox(
        label='جامع خلق پر حضور کی رحمت و شفقت', 
        key="1key", 
        value=False
    )
    book2_selected = st.checkbox(
        label='فتنہ خوارج', 
        key="2key", 
        value=False
    )
    book3_selected = st.checkbox(
        label='گستاخ رسول - احادیث نبوی کی روشنی میں', 
        key="3key", 
        value=False
    )
    book4_selected = st.checkbox(
        label='رحلہ فی طلب العلم', 
        key="4key", 
        value=False
    )
    book5_selected = st.checkbox(
        label='یاقوت و مرجان', 
        key="5key", 
        value=False
    )
    book6_selected = st.checkbox(
        label='زبدت العرفان', 
        key="6key", 
        value=False
    )
    book7_selected = st.checkbox(
        label='الجہاد الاکبر', 
        key="7key", 
        value=False
    )

sel_chkbox = 0
i = 1
while i < 8:
    isclicked = st.session_state[f"{i}key"]
    if isclicked:
        sel_chkbox += 1
    i += 1

# Function for generating LLM response incrementally
def generate_response_stream(input):
    if sel_chkbox == 0:
        st.warning("!برائے مہربانی کم از کم ایک کتاب منتخب کریں")
        st.stop()
        
    elif sel_chkbox > 1:
        st.warning("!برائے مہربانی ایک وقت میں ایک ہی کتاب منتخب کریں")
        st.stop()
    else:
        if book1_selected:
            response = bot1.rag_chain.invoke(input)
        elif book2_selected:
            response = bot2.rag_chain.invoke(input)
        elif book3_selected:
            response = bot3.rag_chain.invoke(input)
        elif book4_selected:
            response = bot4.rag_chain.invoke(input)
        elif book5_selected:
            response = bot5.rag_chain.invoke(input)
        elif book6_selected:
            response = bot6.rag_chain.invoke(input)
        elif book7_selected:
            response = bot7.rag_chain.invoke(input)

        # Simulate streaming by yielding one character at a time
        for char in response:  
            yield char
            time.sleep(0.005)  # Adjust this to control the typing speed

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "ایک کتاب منتخب کریں اور اس سے کچھ بھی پوچھیں، اور یاد رکھیں کہ ایک وقت میں صرف ایک کتاب منتخب کریں۔"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response_container = st.empty()  # Create an empty container for streaming the response
        response_text = ""

        for char in generate_response_stream(input):
            response_text += char
            response_container.write(response_text)

    message = {"role": "assistant", "content": response_text}
    st.session_state.messages.append(message)

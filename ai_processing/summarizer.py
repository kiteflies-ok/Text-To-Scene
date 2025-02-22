from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

def advanced_summarize(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200
    )
    
    docs = text_splitter.create_documents([text])
    
    chain = load_summarize_chain(
        llm=OpenAI(temperature=0.5),
        chain_type="map_reduce",
        return_intermediate_steps=True
    )
    
    result = chain({"input_documents": docs}, return_only_outputs=True)
    return {
        "summary": result["output_text"],
        "key_points": result["intermediate_steps"]
    }

def generate_summary(text: str) -> dict:
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
    
    template = """Summarize this text into key scenes for animation:
    {text}
    
    Return in format:
    - Scene 1: [description]
    - Scene 2: [description]
    ..."""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["text"]
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(text)
    return parse_summary(result)

def parse_summary(raw_summary: str) -> dict:
    scenes = [line.strip() for line in raw_summary.split('\n') if line.strip()]
    return {"scenes": scenes, "raw": raw_summary}
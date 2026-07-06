from fastapi import FastAPI, HTTPException
from transformers import AutoModelForCausalLM, AutoTokenizer

app = FastAPI()

# Loading the model and the tokeniser 

model_name = "unsloth/Qwen-AgentWorld-35B-A3B-GGUF" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.post("/generate")
async def generate_text(prompt: str):
    try:
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
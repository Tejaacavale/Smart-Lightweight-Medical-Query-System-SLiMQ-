import subprocess

def ask_llama(prompt):
    
    # Specify the command and its arguments as a list
    cmd = [
        "llm", 
        "-m", "Llama-2-7b-chat",
        "-o", "temperature", "0.9",
        "-o", "top_p", "0.9",
        # "-o", "max_gen  
        prompt
    ]
    # Run the command and capture its output
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
    

# 1. Read the prompt from input.txt
with open("input.txt", "r") as infile:
    prompt = infile.read().strip()

# 2. Get the response
response = ask_llama(prompt)

# 3. Write the response to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(response)


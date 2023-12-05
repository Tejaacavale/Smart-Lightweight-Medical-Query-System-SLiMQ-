import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

def ask_llama(prompt):
    cmd = [
        "llm", 
        "-m", "Llama-2-7b-chat",
        "-o", "temperature", "0.9",
        "-o", "top_p", "0.9",
        prompt
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

class MyApp(App):
    
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input
        self.text_input = TextInput(hint_text="Enter your prompt here...")
        layout.add_widget(self.text_input)
        
        # Button
        btn = Button(text="Ask Llama")
        btn.bind(on_press=self.ask_button_pressed)
        layout.add_widget(btn)
        
        # Label for feedback
        self.info_label = Label()
        layout.add_widget(self.info_label)
        
        return layout

    def ask_button_pressed(self, instance):
        # Read from the input box
        prompt = self.text_input.text
        
        # Get the response
        response = ask_llama(prompt)
        
        # Write to output.txt
        with open("output.txt", "w") as outfile:
            outfile.write(response)
        
        # Provide feedback to the user
        self.info_label.text = "Response saved to output.txt!"

if __name__ == "__main__":
    MyApp().run()

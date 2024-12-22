from openai import OpenAI
from typing import Generator


class LLMEngine:
    def __init__(
        self, base_url="http://localhost:8080/v1", api_key="sk-no-key-required"
    ):
        self.client = OpenAI(base_url=base_url, api_key=api_key)

    def ask(self, query: str, context: str) -> Generator:
        return self.client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": self._get_sys_msg(context)},
                {"role": "user", "content": query},
            ],
            stream=True,
        )

    def _get_sys_msg(self, context):
        return f"""
            You are a helpful and informative chatbot for drivers at a car delivery company called "Draiver". 
            You will receive some context and a questions from a user of the app.
            Respond to the user's question comprehensively, accurately, and concisely, drawing upon the provided context where relevant. 
            If the context is insufficient or irrelevant, provide general and helpful information based on your understanding of car delivery operations. 
            Ensure your responses are:
            - Clear and easy to understand: Use simple and direct language.
            - Helpful and informative: Provide relevant and actionable information.
            - Safe and ethical: Avoid providing harmful, biased, or discriminatory information.
            - Consistent with company policies: Adhere to all relevant company guidelines and regulations.
            Use some emojis to answer
            This is the context:
            {context}
        """

from groq import Groq
from dotenv import load_dotenv
import os


class Agent:
	def __init__(self, context_file_path, model="openai/gpt-oss-120b", memory=True):
		load_dotenv()
		self.groq_client = Groq(api_key=os.environ["GROQ_KEY"])
		self.initiate_history(context_file_path=context_file_path)
		self.memory = memory
		self.model = model


	@staticmethod
	def read_file(file_path):
		with open(file_path, "r") as file:
			return file.read()


	def initiate_history(self, context_file_path):
		self.history = [
			{
				"role": "system",
				"content": Agent.read_file(file_path=context_file_path)
			}]


	def update_history(self, role, content):
		self.history.append(
			{
				"role": role,
				"content": content,
			})


	def ask_llm(self, user_input):
		
		self.update_history(role="user", content=user_input)

		syllabus = self.groq_client.chat.completions.create(
				messages=self.history,
				model=self.model
				).choices[0].message.content
		
		if self.memory:
			self.update_history(role="assitant", content=syllabus)
		else:
			del self.history[-1]
		
		return syllabus

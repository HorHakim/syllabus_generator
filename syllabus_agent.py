from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class SyllabusAgent:
	def __init__(self):
		self.groq_client = Groq(api_key=os.environ["GROQ_KEY"])
		self.initiate_history()


	@staticmethod
	def read_file(file_path):
		with open(file_path, "r") as file:
			return file.read()


	def initiate_history(self):
		self.history = [
			{
				"role": "system",
				"content": SyllabusAgent.read_file("./context.txt")
			}]



	def update_history(self, role, content):
		self.history.append(
			{
				"role": role,
				"content": content,
			})



	def generate_syllabus(self, module_description):
		self.update_history(role="user", content=module_description)
		syllabus = self.groq_client.chat.completions.create(
				messages=self.history,
				model="llama-3.3-70b-versatile"
				).choices[0].message.content
		self.update_history(role="assitant", content=syllabus)
		return syllabus
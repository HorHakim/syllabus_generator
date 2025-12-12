from agent import Agent 
import pdfplumber
from docx import Document
import os

class SynthetizerAgent(Agent):
	def __init__(self):
		super().__init__(context_file_path="./contexts/synthesizer_agent.txt", memory=False) 


	@staticmethod
	def read_pdf(uploaded_file):
		with pdfplumber.open(uploaded_file) as pdf:
			return "".join([page.extract_text() or "" for page in pdf.pages])



	@staticmethod
	def read_docx(uploaded_file):
		return "\n".join([paragraph.text for paragraph in Document(uploaded_file).paragraphs])




	@staticmethod
	def read_uploaded_file_object(uploaded_file):

		if os.path.splitext(uploaded_file.name)[1] == ".pdf":
			return SynthetizerAgent.read_pdf(uploaded_file)
		
		elif os.path.splitext(uploaded_file.name)[1] == ".docx":
			return SynthetizerAgent.read_docx(uploaded_file)

		elif os.path.splitext(uploaded_file.name)[1] in [".md", ".txt"]:
			return uploaded_file.read().decode("utf-8")




	def synthetize(self, uploaded_file):
		raw_file_content = self.read_uploaded_file_object(uploaded_file)
		return self.ask_llm(user_input=raw_file_content)
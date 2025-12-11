from agent import Agent 
import pdfplumber

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
		return ""


	@staticmethod
	def read_uploaded_file_object(uploaded_file):

		if os.path.splitext(uploaded_file.name)[1] == ".pdf":
			return SynthetizerAgent.read_pdf(uploaded_file)
		
		elif os.path.splitext(uploaded_file.name)[1] == ".docx":
			print("docx : not supported yet")
			return SynthetizerAgent.read_docx(uploaded_file)


	def synthetize(self, uploaded_file):
		raw_file_content = self.read_uploaded_file_object(uploaded_file)
		return self.ask_llm(user_input=raw_file_content)
import markdown
from weasyprint import HTML

from syllabus_agent import SyllabusAgent
from synthesizer_agent import SynthetizerAgent


import io


class Backend:
	def __init__(self):
		self.synthesizer_agent = SynthetizerAgent()
		self.syllabus_agent = SyllabusAgent()



	def generate_syllabus(self, user_input, list_uploaded_files):

		files_content = [self.synthesizer_agent.synthetize(uploaded_file) for uploaded_file in list_uploaded_files]

		course_description = "**Description de l'utilisateur:**  \n"
		course_description += f"{user_input}  \n"
		if files_content:
			course_description += "**Contenu des fichiers:**  \n"
			for index_file, file_content in enumerate(files_content):
				course_description += f"Fichier {index_file}:  \n"
				course_description += f"{file_content}  \n"

		self.syllabus_agent.ask_llm(user_input=course_description)


	def export_syllabus(self, file_type):
		syllabus_content = self.syllabus_agent.get_syllabus_content()
		if file_type == "md":
			buffer_md = io.BytesIO()
			buffer_md.write(syllabus_content.encode("utf-8"))
			return buffer_md
		
		elif file_type == "pdf":
			buffer_pdf = io.BytesIO()
			html = markdown.markdown(
					syllabus_content,
					extensions=["extra", "codehilite", "tables"]
				)

			HTML(string=html).write_pdf(buffer_pdf)
			return buffer_pdf
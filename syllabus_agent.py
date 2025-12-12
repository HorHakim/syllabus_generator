from agent import Agent

class SyllabusAgent(Agent):
	def __init__(self):
		super().__init__(context_file_path="./contexts/syllabus_agent.txt")



	def get_syllabus_content(self):
		return self.history[-1]["content"]
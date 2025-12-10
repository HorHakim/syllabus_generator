import streamlit
from syllabus_agent import SyllabusAgent 



if "syllabus_agent" not in streamlit.session_state :
	streamlit.session_state.syllabus_agent = SyllabusAgent()


def init_header():
	streamlit.set_page_config(page_title="Syllabus Terminator", page_icon="🤖")
	streamlit.title("💖 Ton générateur de syllabus préféré !")




def show_discussion_history(history_placeholder):
	container = history_placeholder.container()
	with container:
		for message in streamlit.session_state.syllabus_agent.history:
			if message["role"] != "system":
				with streamlit.chat_message(message["role"]):
					streamlit.write(message["content"])


def user_interface():
	init_header()
	history_placeholder = streamlit.empty() 
	show_discussion_history(history_placeholder)
	with streamlit.container():
		
		user_input = streamlit.chat_input("Copie colle ton pavet je m'occupe de tout bg !")

		if user_input:
			streamlit.session_state.syllabus_agent.generate_syllabus(module_description=user_input)
			show_discussion_history(history_placeholder)



if __name__ == "__main__":
	user_interface()

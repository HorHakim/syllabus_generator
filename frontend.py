import streamlit
from backend import Backend 


if "backend" not in streamlit.session_state :
	streamlit.session_state.backend = Backend()


if "uploader_key" not in streamlit.session_state:
    streamlit.session_state.uploader_key = 0




def init_header():
	streamlit.set_page_config(page_title="Syllabus Terminator", page_icon="🤖")
	streamlit.title("Ton générateur de syllabus préféré !💖")


def show_discussion_history(history_placeholder):
	container = history_placeholder.container()
	with container:
		for message in streamlit.session_state.backend.syllabus_agent.history:
			if message["role"] != "system":
				with streamlit.chat_message(message["role"]):
					streamlit.write(message["content"])


def download_md_file_button():
	streamlit.download_button(
	label="Télécharger le fichier Markdown",
	data=open("syllabus.md", "rb").read(),
	file_name="syllabus.md",
	mime="text/markdown"
	)


def user_interface():
	init_header()
	history_placeholder = streamlit.empty() 
	show_discussion_history(history_placeholder)
	
	if len(streamlit.session_state.backend.syllabus_agent.history) == 1:
		user_input = streamlit.chat_input("Copie colle ton pavé je m'occupe de tout bg !")
		uploaded_files = streamlit.file_uploader(
						"📎 Charge tes pièces jointes",
						type=["pdf", "docx", "md", "txt"],
						accept_multiple_files=True,
						key=streamlit.session_state.uploader_key
						)


		if user_input:
			streamlit.session_state.backend.generate_syllabus(user_input=user_input, list_uploaded_files=uploaded_files)
			show_discussion_history(history_placeholder)
			streamlit.session_state.uploader_key += 1
			streamlit.rerun()

	else:
		streamlit.session_state.backend.export_syllabus()
		download_md_file_button()



if __name__ == "__main__":
	user_interface()

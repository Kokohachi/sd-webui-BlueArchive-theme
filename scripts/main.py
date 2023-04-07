import json

import gradio as gr

from modules import script_callbacks
import modules.scripts as scripts


def load_data(file_name: str = f"{scripts.basedir()}/characters/character_info.json") -> dict:
    print("Loading data...")
    data = {}

    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def analysis_json():
    data = load_data()
    school_list = []
    for school in list(data.keys()):
        globals()[school] = []
        school_list.append(school)
        for i in range(len(data[school])):
            globals()[school].append(data[school][i]["en"])
            for character in data[school][i]["css"]:
                globals()[data[school][i]["en"]] = list(character.keys())

    return school_list


def update_characters(school):
    return gr.update(visible=True, choices=globals()[school]), \
        gr.update(visible=False)


def update_costume(characters):
    return gr.update(visible=True, choices=globals()[characters])


def replace_css(costume):
    return "Change Applied! Please restart webui"


class Script(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "BlueArchive Theme"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return ()


def on_ui_tabs():
    school_list = analysis_json()
    with gr.Blocks(analytics_enabled=False) as bluearchive:
        with gr.Column():
            """
            language = gr.Radio(
                choices=["EN", "JP"],
                label="Language"
            )
            """
            school = gr.Radio(
                choices=school_list,
                label="School",
                interactive=True
            )
            characters = gr.Radio(
                label="Characters",
                interactive=True,
                visible=False
            )
            costume = gr.Radio(
                label="costume",
                interactive=True,
                visible=False
            )
            apply_theme = gr.Button("Apply Theme", variant="primary")
            status = gr.Textbox(
                label="Status",
                interactive=False
            )

        school.change(
            fn=update_characters,
            inputs=school,
            outputs=[characters, costume]
        )
        characters.change(
            fn=update_costume,
            inputs=characters,
            outputs=costume
        )
        apply_theme.click(
            fn=replace_css,
            inputs=costume,
            outputs=status
        )

    return [(bluearchive, "Bluearchive Theme", "bluearchive_theme")]


script_callbacks.on_ui_tabs(on_ui_tabs)

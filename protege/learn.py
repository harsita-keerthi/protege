import reflex as rx

from rxconfig import config
from .components.navbar import *
from .components.prompt_form import *
from .components.learn_schedule import *

# sample file
import json
with open('ex.json', 'r') as file:
    data = json.load(file)

class State(rx.State):
    show: bool = False
    prompt_data = FormInputState.prompt_data
    def toggle_visibility(self):
        self.show = not self.show
# lesson plan generation page
def learn() -> rx.Component:
    return rx.fragment(
        navbar_user(), # navbar
        rx.color_mode.button(position="bottom-left"),
        rx.vstack( 
            rx.heading("what do you want to learn?", size="9", align="center"),
            form_input1(),

            # styling
            spacing="5",
            justify="center",
            align_items="center",
            display="flex",
            flex_direction="column",
            min_height="85vh",
            padding_bottom="220px",
            padding_top="240px",
        ),
        learn_schedule(data)
        
        # rx.cond(
        #     State.show,
        #     learn_schedule(FormInputState.res),
        #     learn_schedule(data)
        # )
    )
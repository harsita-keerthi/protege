import reflex as rx

from server.create import *

# sample file
import json
with open('ex.json', 'r') as file:
    data = json.load(file)

class FormInputState(rx.State):
    prompt_data: dict = {
        'prompt':"",
        'weeks': int(),
        'hours': int(),
    }
    
    res = data
    
    weeks_slider: int = 5
    hours_slider: int = 5

    def set_weeks(self, value: list[int]):
        self.weeks_slider = value[0]
        self.prompt_data['weeks'] = self.weeks_slider

    def set_hours(self, value: list[int]):
        self.hours_slider = value[0]
        self.prompt_data['hours'] = self.hours_slider

    def submit(self, prompt_data: dict):
        self.prompt_data = prompt_data
        self.res = create_lesson_plan(self.prompt_data['prompt'], 
                           self.prompt_data['weeks'], 
                           self.prompt_data['hours'])
        print(self.res)

def form_input1():
    return rx.card(
        rx.vstack(
            rx.form.root(
                rx.vstack(
                    rx.input(
                        name="prompt",
                        placeholder="Enter a topic...",
                        type="text",
                        required=True,
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.heading(f"{FormInputState.weeks_slider} weeks"),
                            rx.slider(
                                default_value=5, 
                                name="weeks",
                                max=10,
                                on_value_commit=FormInputState.set_weeks,
                            ),
                            width="100%",
                        ),
                        rx.vstack(
                            rx.heading(f"{FormInputState.hours_slider} hours"),
                            rx.slider(
                                default_value=5, 
                                name="hours",
                                max=10,
                                on_value_commit=FormInputState.set_hours,
                            ),
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                        padding="20px",
                    ),
                    rx.button("Submit", type="submit"),
                    width="100%",
                    align="center",
                ),
                on_submit=FormInputState.submit,
                reset_on_submit=True,
            ),
            # rx.divider(),

            # test output
            # rx.hstack(
            #     rx.heading("Results:"),
            #     rx.badge(
            #         FormInputState.res.to_string()
            #     ),
            # ),
            align_items="center",
            width="100%",
            padding="20px",  
            # padding_bottom="20px", 
        ),
        width="50%",
        padding="20px",
    )

def get_res():
    print(FormInputState.res)
    # return FormInputState.res



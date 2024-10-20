import reflex as rx

from rxconfig import config
from .components.navbar import *

def teach() -> rx.Component:
    # Welcome Page (Index)
    # return rx.container(
    #     navbar_user(),
    #     rx.color_mode.button(position="top-right"),
    #     rx.vstack(
    #         rx.heading("become a protégé.", size="9", align="center", position="center"),
    #         rx.link(
    #             rx.button("Check out our docs!"),
    #             href="https://reflex.dev/docs/getting-started/introduction/",
    #             is_external=True,
    #         ),
    #         spacing="5",
    #         justify="center",
    #         min_height="85vh",
    #     ),
    #     rx.logo(),
    #     max_width="100%",
    #     margin="0px",
    #     padding="0",
    # )
    return rx.fragment(
        navbar_user(), # navbar
        rx.color_mode.button(position="bottom-left"),
        rx.vstack( 
            rx.heading("become a protégé.", size="9", align="center"),

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
        
        # rx.cond(
        #     State.show,
        #     learn_schedule(FormInputState.res),
        #     learn_schedule(data)
        # )
    )

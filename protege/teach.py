import reflex as rx

from rxconfig import config
from .components.navbar import *

def teach() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar_user(),
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("what would you like to learn today?", size="9", align="center", position="center"),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
        max_width="100%",
        margin="0px",
        padding="0",
    )

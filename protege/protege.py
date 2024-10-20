import reflex as rx
from assets.styles import styles

from rxconfig import config
from .components.navbar import *
from .teach import *
from .learn import *

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.fragment(
        navbar_user(),
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading(
                "let's learn!",
                size="9", 
                align="center", 
                font_family="Baloo Tamma 2", 
                weight="bold"
                ),
            
            spacing="5",
            padding_top="300px",
            justify="center",
            align_items="center",
            display="flex",
            flex_direction="column",
            #min_height="85vh",
            padding_bottom="25px",
        ),
        rx.hstack(
            rx.link(
                rx.button("learn",
                width="150px",
                height="45px",
                font_size="27px",
                ),
                href="/learn",
            ),
            rx.link(
                rx.button("teach",
                width="150px",
                height="45px",
                font_size="27px",
                ),
                href="/teach",
            ),
            spacing="5",
            justify="center",
            display="flex",
            flex_direction="row",
            #min_height="85vh",
        ),
        spacing="0",
        # rx.logo() # reflex logo
    )

# style = {
#     font-family: "Poppins",
#     font_size: "16px",
# }

app = rx.App(
    # style=style,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:ital,wght@0,500;0,600;1,600&display=swap",
    ],
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="indigo",
        panel_background="translucent"
    )
)
app.add_page(index, route="/")
app.add_page(teach, route="/teach")
app.add_page(learn, route="/learn")

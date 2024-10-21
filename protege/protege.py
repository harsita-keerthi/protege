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
            rx.link(
                rx.button("learn"),
                href="/learn",
            ),
            rx.link(
                rx.button("teach"),
                href="/teach",
            ),
            spacing="5",
            justify="center",
            align_items="center",
            display="flex",
            flex_direction="column",
            min_height="85vh",
        ),
        # rx.logo() # reflex logo
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
)
app.add_page(index, route="/")
app.add_page(teach, route="/teach")
app.add_page(learn, route="/learn")

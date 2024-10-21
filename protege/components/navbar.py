import reflex as rx

from rxconfig import config

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar_user() -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "protégé", size="7", weight="bold", font_family="Baloo Tamma 2"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("home", "/"),
                    navbar_link("learn", "/learn"),
                    navbar_link("teach", "/teach"),
                    align_items="center",
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Settings"),
                        rx.menu.separator(),
                        rx.menu.item("Log out"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        background_color="#111113",
        padding="1em", # navbar padding
        position="fixed",
        top="0px",
        z_index="5",
        width="100%",
    )


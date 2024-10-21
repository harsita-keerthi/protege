import reflex as rx

weeks = {}

# populate dictionary w/ week num + corresponding days
def split_weeks(prompt):
    num_weeks = prompt['lesson_plan'][-1]["week_number"]
    
    for i in range(1, num_weeks+1):
        weeks[i] = []

    curr = 1
    for day in prompt['lesson_plan']:
        if curr != day['week_number']:
            curr += 1
            weeks[curr].append(day)
        else:
            weeks[curr].append(day)


def create_day(day: dict) -> rx.Component:
    return rx.hstack(
        rx.card(f"Day {day['day_number']}", height="10vh", width="10%"),
        rx.card(f"{day['duration']}", height="10vh", width="10%"),
        rx.card(f"{day['topic_name']}", height="10vh", width="20%"),
        rx.card(f"{day['description']}", height="10vh", width="30%"),
        rx.card(f"{day['resources']}", height="10vh", width="30%"),
    )


def create_week(week: dict) -> rx.Component:
    return rx.hstack(
        rx.card(f"Week {week[0]}", height="10vh", width="10%"),
        rx.vstack(
            rx.foreach(
            week[1],
            create_day,
            ),
            width="90%"
        ),
    )

def learn_schedule(prompt) -> rx.Component:
    split_weeks(prompt)

    return rx.vstack(
            rx.hstack(
                rx.card("Week", width="10%"),
                rx.card("Day", width="10%"),
                rx.card("Hours", width="10%"),
                rx.card("Topic Name", width="20%"),
                rx.card("Description", width="30%"),
                rx.card("Resources", width="30%"),
                width="100%"
            ),
            rx.foreach(
                weeks,
                create_week
            )
    )
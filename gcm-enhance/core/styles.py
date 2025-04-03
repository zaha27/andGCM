STYLES = {
    "conventional": "{type}: update {summary}",
    "corporate": "{type_cap}: Implemented {summary} improvements.",
    "fun": "{type}! {summary} just got cooler 😎"
}

def apply_style(commit_type: str, summary: str, style: str = "conventional"):
    template = STYLES.get(style, STYLES["conventional"])
    return template.format(
        type=commit_type,
        type_cap=commit_type.capitalize(),
        summary=summary
    )




#
##
#
#
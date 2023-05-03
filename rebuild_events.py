from os import getenv
from requests import get

source = getenv("SOURCE","https://raw.githubusercontent.com/github/docs/main/content/actions/using-workflows/events-that-trigger-workflows.md")
file_location = getenv("file_location", "zsh/_act")

events = [ event.strip() for event in get(source).text.split("## `")][1:]
starting_blacklist = ("|", "**Note**","**Note:**", "{%")
replacements = {
    "{% data variables.product.product_name %}": "GitHub",
    "'": " ",
}
completion_lines_arr = ""
for event in events:
    description = [event_info for event_info in event.split("\n") if event_info and not event_info.startswith(starting_blacklist)][1]
    for old, new in replacements.items(): description = description.replace(old, new)
    description = description.split(".")[0] # take first sentence only

    name=event.split("\n")[0].split("`")[0]

    completion_lines_arr+=f"\t\t'{name}:{description}'\n"

r = open(file_location, "r").read()
original = r.split("# --- gen ---")[1]
new = f"\n{completion_lines_arr}"
open(file_location, "w").write(r.replace(original, new))

print(completion_lines_arr)